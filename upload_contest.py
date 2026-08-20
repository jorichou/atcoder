#!/usr/bin/env python3
"""
AtCoder AC解答自動収集・GitHubアップロードシステム
spec.md に基づき、指定されたコンテストのAC提出を取得してローカル保存・Git commit/pushを行います。
"""

import argparse
import datetime
import json
import os
import re
import subprocess
import sys
from typing import Any, Dict, List, Optional, Set, Tuple
import requests
from bs4 import BeautifulSoup

CONFIG_FILE = "config.json"
DATA_DIR = "data"
PROCESSED_SUBMISSIONS_FILE = os.path.join(DATA_DIR, "processed_submissions.json")
SOLUTIONS_DIR = "solutions"

DEFAULT_HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/120.0.0.0 Safari/537.36"
    )
}


class ConfigManager:
    """ユーザー設定情報の取得・保存を行う"""

    @staticmethod
    def get_user_id(cli_user_id: Optional[str] = None, config_path: str = CONFIG_FILE) -> str:
        if cli_user_id:
            return cli_user_id.strip()

        env_user_id = os.environ.get("ATCODER_USER_ID")
        if env_user_id:
            return env_user_id.strip()

        if os.path.exists(config_path):
            try:
                with open(config_path, "r", encoding="utf-8") as f:
                    data = json.load(f)
                    user_id = data.get("atcoder_user_id", "").strip()
                    if user_id:
                        return user_id
            except Exception:
                pass

        user_id = input("Enter your AtCoder user ID: ").strip()
        if not user_id:
            print("ERROR: AtCoder user ID cannot be empty.")
            sys.exit(1)

        try:
            config_data = {}
            if os.path.exists(config_path):
                try:
                    with open(config_path, "r", encoding="utf-8") as f:
                        config_data = json.load(f)
                except Exception:
                    config_data = {}
            config_data["atcoder_user_id"] = user_id
            with open(config_path, "w", encoding="utf-8") as f:
                json.dump(config_data, f, indent=4, ensure_ascii=False)
        except Exception as e:
            print(f"Warning: Failed to save config: {e}")

        return user_id


class ProblemParser:
    """problem_id からコンテスト分類・問題構造をパースする"""

    SPECIAL_CONTEST_MAP = {
        "dp": ("EDPC", "EDPC"),
        "typical90": ("TYPICAL90", "TYPICAL90"),
    }

    @classmethod
    def parse_problem_id(cls, problem_id: str) -> Tuple[str, str, str]:
        """
        problem_id (例: 'abc348_d', 'arc180_b', 'agc001_c', 'dp_a') から
        (contest_type, contest_name, problem_name) のタプルを返す。
        """
        if "_" in problem_id:
            contest_part, task_part = problem_id.rsplit("_", 1)
            problem_name = task_part.upper()

            # Special map check (e.g. dp_a, typical90_a)
            if contest_part.lower() in cls.SPECIAL_CONTEST_MAP:
                c_type, c_name = cls.SPECIAL_CONTEST_MAP[contest_part.lower()]
                return c_type, c_name, problem_name

            # Match standard contest prefix + digits (e.g. abc348, arc180, agc001, ahc001, past202004)
            match = re.match(r"^([a-zA-Z]+)(\d+.*)$", contest_part)
            if match:
                prefix, num = match.groups()
                contest_type = prefix.upper()
                contest_name = f"{contest_type}{num.upper()}"
                return contest_type, contest_name, problem_name

            # Alphabet prefix only
            contest_type = contest_part.upper()
            contest_name = contest_part.upper()
            return contest_type, contest_name, problem_name

        # Fallback if no '_'
        name = problem_id.upper()
        return "OTHER", name, name


class AtCoderAPI:
    """AtCoder / AtCoder Problems から提出データやコードを取得する"""

    @staticmethod
    def fetch_user_submissions(user_id: str) -> List[Dict[str, Any]]:
        url = f"https://kenkoooo.com/atcoder/atcoder-api/v3/user/submissions?user={user_id}&from_second=0"
        res = requests.get(url, headers=DEFAULT_HEADERS, timeout=15)
        res.raise_for_status()
        return res.json()

    @staticmethod
    def fetch_submission_code(submitted_contest: str, submission_id: int) -> Optional[str]:
        url = f"https://atcoder.jp/contests/{submitted_contest}/submissions/{submission_id}"
        res = requests.get(url, headers=DEFAULT_HEADERS, timeout=15)
        if res.status_code != 200:
            return None

        soup = BeautifulSoup(res.text, "html.parser")
        code_elem = soup.find(id="submission-code")
        if not code_elem:
            code_elem = soup.find("pre")
        if not code_elem:
            return None

        return code_elem.get_text()

    @staticmethod
    def check_contest_exists(contest_id: str) -> bool:
        url = f"https://atcoder.jp/contests/{contest_id}"
        res = requests.get(url, headers=DEFAULT_HEADERS, timeout=15)
        return res.status_code == 200


class SubmissionStorage:
    """保存済み提出IDの管理、ファイル保存、メタデータ更新を行う"""

    def __init__(
        self,
        processed_file: str = PROCESSED_SUBMISSIONS_FILE,
        solutions_dir: str = SOLUTIONS_DIR,
    ):
        self.processed_file = processed_file
        self.solutions_dir = solutions_dir

    def load_processed_ids(self) -> Set[int]:
        if os.path.exists(self.processed_file):
            try:
                with open(self.processed_file, "r", encoding="utf-8") as f:
                    data = json.load(f)
                    return set(data.get("processed_submission_ids", []))
            except Exception:
                return set()
        return set()

    def save_processed_ids(self, ids: Set[int]) -> None:
        os.makedirs(os.path.dirname(self.processed_file), exist_ok=True)
        data = {"processed_submission_ids": sorted(list(ids))}
        with open(self.processed_file, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)

    def save_solution(
        self,
        contest_type: str,
        contest_name: str,
        problem_name: str,
        problem_id: str,
        submission_id: int,
        submitted_at: str,
        submitted_contest: str,
        language: str,
        code: str,
    ) -> Tuple[str, str]:
        """
        解答コードと metadata.json を保存し、(保存相対パス, ファイル名) を返す。
        """
        problem_dir = os.path.join(
            self.solutions_dir, contest_type, contest_name, problem_name
        )
        os.makedirs(problem_dir, exist_ok=True)

        # 既存ファイルから連番を算出
        existing_numbers = []
        for fname in os.listdir(problem_dir):
            match = re.match(r"^(\d+)\.py$", fname)
            if match:
                existing_numbers.append(int(match.group(1)))

        next_idx = max(existing_numbers, default=0) + 1
        filename = f"{next_idx:02d}.py"
        file_path = os.path.join(problem_dir, filename)

        # 解答コード書き込み
        with open(file_path, "w", encoding="utf-8", newline="\n") as f:
            f.write(code)

        # metadata.json 更新
        meta_path = os.path.join(problem_dir, "metadata.json")
        meta_data: Dict[str, Any] = {"problem_id": problem_id, "solutions": []}
        if os.path.exists(meta_path):
            try:
                with open(meta_path, "r", encoding="utf-8") as f:
                    meta_data = json.load(f)
            except Exception:
                meta_data = {"problem_id": problem_id, "solutions": []}

        meta_data["problem_id"] = problem_id
        if "solutions" not in meta_data:
            meta_data["solutions"] = []

        meta_data["solutions"].append(
            {
                "file": filename,
                "submission_id": submission_id,
                "submitted_at": submitted_at,
                "submitted_contest": submitted_contest,
                "language": language,
            }
        )

        with open(meta_path, "w", encoding="utf-8") as f:
            json.dump(meta_data, f, indent=4, ensure_ascii=False)

        rel_path = os.path.relpath(file_path, ".").replace("\\", "/")
        return rel_path, filename


class GitManager:
    """Git操作を行う"""

    @staticmethod
    def commit_and_push(contest_target_display: str, target_dir: str = SOLUTIONS_DIR) -> bool:
        if not os.path.exists(target_dir):
            return True

        # git status で変更があるか確認
        status_proc = subprocess.run(
            ["git", "status", "--porcelain"],
            capture_output=True,
            text=True,
            check=False,
        )
        if not status_proc.stdout.strip():
            return True

        # git add
        add_proc = subprocess.run(["git", "add", target_dir], check=False)
        if add_proc.returncode != 0:
            print("Git add failed.")
            return False

        # コミットメッセージ構築
        # ABC300 や ARC180 などの場合は "Add solutions for ABC300"
        # ADT などの場合は "Add solutions from adt_all_..."
        if re.match(r"^(ABC|ARC|AGC|AHC)\d+$", contest_target_display, re.IGNORECASE):
            commit_msg = f"Add solutions for {contest_target_display.upper()}"
        else:
            commit_msg = f"Add solutions from {contest_target_display.lower()}"

        print("Git commit...")
        commit_proc = subprocess.run(
            ["git", "commit", "-m", commit_msg], check=False
        )
        if commit_proc.returncode != 0:
            print("Git commit failed.")
            return False

        print("Git push...")
        push_proc = subprocess.run(["git", "push"], check=False)
        if push_proc.returncode != 0:
            print("Git push failed.")
            return False

        return True


def format_iso_timestamp(epoch_second: int) -> str:
    tz_jst = datetime.timezone(datetime.timedelta(hours=9))
    dt = datetime.datetime.fromtimestamp(epoch_second, tz=tz_jst)
    return dt.isoformat(timespec="seconds")


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Upload AC submissions for an AtCoder contest."
    )
    parser.add_argument("contest_id", help="Contest ID (e.g. abc300, arc180, adt_all_20260811_1)")
    parser.add_argument("--user", help="AtCoder User ID", default=None)
    parser.add_argument(
        "--no-push", help="Skip git push", action="store_true"
    )
    args = parser.parse_args()

    target_contest = args.contest_id.strip()
    target_contest_lower = target_contest.lower()
    user_id = ConfigManager.get_user_id(args.user)

    display_contest = target_contest.upper() if not target_contest_lower.startswith("adt_") else target_contest.upper()

    print("=== Upload AtCoder Solutions ===")
    print()
    print(f"Target Contest: {display_contest}")
    print()
    print("Fetching submissions...")
    print()

    # 提出一覧取得
    try:
        all_submissions = AtCoderAPI.fetch_user_submissions(user_id)
    except Exception as e:
        print(f"ERROR: Failed to fetch submissions from AtCoder Problems API: {e}")
        sys.exit(1)

    # 対象コンテストの抽出
    contest_submissions = [
        s for s in all_submissions if s.get("contest_id", "").lower() == target_contest_lower
    ]

    if not contest_submissions:
        # コンテスト自体の存在チェック
        if not AtCoderAPI.check_contest_exists(target_contest_lower):
            print(f'ERROR:\nContest "{target_contest}" was not found.')
            sys.exit(1)
        else:
            print("No accepted submissions found.")
            sys.exit(0)

    ac_submissions = [s for s in contest_submissions if s.get("result") == "AC"]
    if not ac_submissions:
        print("No accepted submissions found.")
        sys.exit(0)

    # 重複判定
    storage = SubmissionStorage()
    processed_ids = storage.load_processed_ids()

    new_ac_submissions = [
        s for s in ac_submissions if s.get("id") not in processed_ids
    ]

    if not new_ac_submissions:
        print("No new accepted submissions found.")
        sys.exit(0)

    # 昇順ソート（古い提出から保存）
    new_ac_submissions.sort(key=lambda s: s.get("id", 0))

    newly_saved_ids: Set[int] = set()

    for sub in new_ac_submissions:
        sub_id = sub["id"]
        prob_id = sub.get("problem_id", "")
        submitted_contest = sub.get("contest_id", target_contest_lower)
        epoch_sec = sub.get("epoch_second", 0)
        language = sub.get("language", "Python")

        c_type, c_name, p_name = ProblemParser.parse_problem_id(prob_id)

        print(f"[{c_name} {p_name}]")
        print(f"Submission ID: {sub_id}")
        print("Status: AC")

        # ソースコード取得
        code = AtCoderAPI.fetch_submission_code(submitted_contest, sub_id)
        if code is None:
            print(f"Failed to fetch submission: {sub_id}")
            print()
            continue

        submitted_at_str = format_iso_timestamp(epoch_sec)

        rel_path, _ = storage.save_solution(
            contest_type=c_type,
            contest_name=c_name,
            problem_name=p_name,
            problem_id=prob_id,
            submission_id=sub_id,
            submitted_at=submitted_at_str,
            submitted_contest=submitted_contest,
            language=language,
            code=code,
        )

        print(f"→ Saving as {rel_path}")
        print()
        newly_saved_ids.add(sub_id)

    if not newly_saved_ids:
        print("No solutions were successfully fetched.")
        sys.exit(0)

    print("Updating metadata...")
    print()

    # Git操作
    if not args.no_push:
        git_success = GitManager.commit_and_push(display_contest)
        if git_success:
            # push成功後にprocessed_submissions.jsonを更新
            storage.save_processed_ids(processed_ids | newly_saved_ids)
            print("Completed!")
        else:
            print("Warning: Git commit/push failed. Processed IDs were not updated.")
            sys.exit(1)
    else:
        storage.save_processed_ids(processed_ids | newly_saved_ids)
        print("Completed! (Git push skipped by --no-push)")


if __name__ == "__main__":
    main()
