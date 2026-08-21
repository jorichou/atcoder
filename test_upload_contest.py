import json
import os
import shutil
import tempfile
import unittest
from unittest.mock import MagicMock, patch

from upload_contest import (
    AtCoderAPI,
    ConfigManager,
    GitManager,
    LanguageUtils,
    ProblemParser,
    RollbackManager,
    SubmissionStorage,
    format_iso_timestamp,
)



class TestProblemParser(unittest.TestCase):
    def test_abc(self):
        c_type, c_name, p_name = ProblemParser.parse_problem_id("abc348_d")
        self.assertEqual(c_type, "ABC")
        self.assertEqual(c_name, "ABC348")
        self.assertEqual(p_name, "D")

    def test_arc(self):
        c_type, c_name, p_name = ProblemParser.parse_problem_id("arc180_b")
        self.assertEqual(c_type, "ARC")
        self.assertEqual(c_name, "ARC180")
        self.assertEqual(p_name, "B")

    def test_agc(self):
        c_type, c_name, p_name = ProblemParser.parse_problem_id("agc001_c")
        self.assertEqual(c_type, "AGC")
        self.assertEqual(c_name, "AGC001")
        self.assertEqual(p_name, "C")

    def test_ahc(self):
        c_type, c_name, p_name = ProblemParser.parse_problem_id("ahc001_a")
        self.assertEqual(c_type, "AHC")
        self.assertEqual(c_name, "AHC001")
        self.assertEqual(p_name, "A")

    def test_past(self):
        c_type, c_name, p_name = ProblemParser.parse_problem_id("past202004_a")
        self.assertEqual(c_type, "PAST")
        self.assertEqual(c_name, "PAST202004")
        self.assertEqual(p_name, "A")

    def test_edpc(self):
        c_type, c_name, p_name = ProblemParser.parse_problem_id("dp_a")
        self.assertEqual(c_type, "EDPC")
        self.assertEqual(c_name, "EDPC")
        self.assertEqual(p_name, "A")

    def test_typical90(self):
        c_type, c_name, p_name = ProblemParser.parse_problem_id("typical90_a")
        self.assertEqual(c_type, "TYPICAL90")
        self.assertEqual(c_name, "TYPICAL90")
        self.assertEqual(p_name, "A")


class TestSubmissionStorage(unittest.TestCase):
    def setUp(self):
        self.test_dir = tempfile.mkdtemp()
        self.processed_file = os.path.join(self.test_dir, "data", "processed_submissions.json")
        self.solutions_dir = os.path.join(self.test_dir, "solutions")
        self.storage = SubmissionStorage(
            processed_file=self.processed_file,
            solutions_dir=self.solutions_dir,
        )

    def tearDown(self):
        shutil.rmtree(self.test_dir)

    def test_load_and_save_processed_ids(self):
        self.assertEqual(self.storage.load_processed_ids(), set())
        self.storage.save_processed_ids({101, 102, 103})
        self.assertEqual(self.storage.load_processed_ids(), {101, 102, 103})

    def test_save_solution_and_metadata(self):
        # 1回目の保存
        rel_path1, fname1 = self.storage.save_solution(
            contest_type="ABC",
            contest_name="ABC348",
            problem_name="D",
            problem_id="abc348_d",
            submission_id=123456789,
            submitted_at="2026-08-11T14:32:15+09:00",
            submitted_contest="abc348",
            language="Python (CPython)",
            code="print('Hello 1')",
        )
        self.assertEqual(fname1, "01.py")
        self.assertTrue(os.path.exists(os.path.join(self.solutions_dir, "ABC", "ABC348", "D", "01.py")))

        # metadata.json の検証
        meta_path = os.path.join(self.solutions_dir, "ABC", "ABC348", "D", "metadata.json")
        self.assertTrue(os.path.exists(meta_path))
        with open(meta_path, "r", encoding="utf-8") as f:
            meta = json.load(f)
        self.assertEqual(meta["problem_id"], "abc348_d")
        self.assertEqual(len(meta["solutions"]), 1)
        self.assertEqual(meta["solutions"][0]["submission_id"], 123456789)

        # 2回目の保存 (C++で解いた場合)
        rel_path2, fname2 = self.storage.save_solution(
            contest_type="ABC",
            contest_name="ABC348",
            problem_name="D",
            problem_id="abc348_d",
            submission_id=124000123,
            submitted_at="2026-08-20T19:15:22+09:00",
            submitted_contest="adt_all_20260811_1",
            language="C++ (GCC 12.2.0)",
            code="int main() {}",
        )
        self.assertEqual(fname2, "02.cpp")
        self.assertTrue(os.path.exists(os.path.join(self.solutions_dir, "ABC", "ABC348", "D", "02.cpp")))

        with open(meta_path, "r", encoding="utf-8") as f:
            meta = json.load(f)
        self.assertEqual(len(meta["solutions"]), 2)
        self.assertEqual(meta["solutions"][1]["file"], "02.cpp")
        self.assertEqual(meta["solutions"][1]["submitted_contest"], "adt_all_20260811_1")


class TestLanguageUtils(unittest.TestCase):
    def test_get_extension(self):
        self.assertEqual(LanguageUtils.get_extension("Python (CPython 3.11.4)"), ".py")
        self.assertEqual(LanguageUtils.get_extension("Python (PyPy 3.10-v7.3.12)"), ".py")
        self.assertEqual(LanguageUtils.get_extension("C++ (GCC 12.2.0)"), ".cpp")
        self.assertEqual(LanguageUtils.get_extension("C++ 20 (gcc 12.2)"), ".cpp")
        self.assertEqual(LanguageUtils.get_extension("C (GCC 12.2.0)"), ".c")
        self.assertEqual(LanguageUtils.get_extension("C# (.NET 7.0.7)"), ".cs")
        self.assertEqual(LanguageUtils.get_extension("Java (OpenJDK 17)"), ".java")
        self.assertEqual(LanguageUtils.get_extension("Rust (rustc 1.70.0)"), ".rs")
        self.assertEqual(LanguageUtils.get_extension("Go (1.20.6)"), ".go")
        self.assertEqual(LanguageUtils.get_extension("JavaScript (Node.js 18.16.1)"), ".js")
        self.assertEqual(LanguageUtils.get_extension("TypeScript (5.1.6)"), ".ts")
        self.assertEqual(LanguageUtils.get_extension("Ruby (3.2.2)"), ".rb")
        self.assertEqual(LanguageUtils.get_extension("Kotlin (1.8.20)"), ".kt")
        self.assertEqual(LanguageUtils.get_extension("UnknownLang"), ".txt")


class TestRollbackManager(unittest.TestCase):
    def setUp(self):
        self.test_dir = tempfile.mkdtemp()
        self.processed_file = os.path.join(self.test_dir, "data", "processed_submissions.json")
        self.solutions_dir = os.path.join(self.test_dir, "solutions")
        self.storage = SubmissionStorage(
            processed_file=self.processed_file,
            solutions_dir=self.solutions_dir,
        )

    def tearDown(self):
        shutil.rmtree(self.test_dir)

    def test_rollback_on_failure(self):
        self.storage.save_processed_ids({100})
        rollback_mgr = RollbackManager(self.storage)

        # 新規解答の保存
        self.storage.save_solution(
            contest_type="ABC",
            contest_name="ABC300",
            problem_name="A",
            problem_id="abc300_a",
            submission_id=999,
            submitted_at="2026-08-21T00:00:00+09:00",
            submitted_contest="abc300",
            language="Python",
            code="print(1)",
            rollback_mgr=rollback_mgr,
        )
        self.storage.save_processed_ids({100, 999})

        sol_file = os.path.join(self.solutions_dir, "ABC", "ABC300", "A", "01.py")
        meta_file = os.path.join(self.solutions_dir, "ABC", "ABC300", "A", "metadata.json")
        self.assertTrue(os.path.exists(sol_file))
        self.assertTrue(os.path.exists(meta_file))

        # ロールバック実行 (Git操作なしでファイル系ロールバック検証)
        rollback_mgr.rollback()

        self.assertFalse(os.path.exists(sol_file))
        self.assertFalse(os.path.exists(meta_file))
        self.assertEqual(self.storage.load_processed_ids(), {100})


class TestTimestampFormat(unittest.TestCase):

    def test_format_iso_timestamp(self):
        ts = 1786426335  # 2026-08-11 14:32:15 JST approximate timestamp
        formatted = format_iso_timestamp(ts)
        self.assertIn("+09:00", formatted)


class TestAllContestsMode(unittest.TestCase):
    def setUp(self):
        self.test_dir = tempfile.mkdtemp()
        self.processed_file = os.path.join(self.test_dir, "data", "processed_submissions.json")
        self.solutions_dir = os.path.join(self.test_dir, "solutions")

    def tearDown(self):
        shutil.rmtree(self.test_dir)

    @patch("upload_contest.AtCoderAPI.fetch_submission_code")
    @patch("upload_contest.AtCoderAPI.fetch_user_submissions")
    @patch("upload_contest.GitManager.commit_and_push")
    @patch("upload_contest.ConfigManager.get_user_id")
    def test_main_all_contests(self, mock_get_user_id, mock_git, mock_fetch_subs, mock_fetch_code):
        from upload_contest import main

        mock_get_user_id.return_value = "dummy_user"
        mock_fetch_subs.return_value = [
            {"id": 1, "contest_id": "abc300", "problem_id": "abc300_a", "result": "AC", "epoch_second": 1000},
            {"id": 2, "contest_id": "arc180", "problem_id": "arc180_a", "result": "AC", "epoch_second": 2000},
            {"id": 3, "contest_id": "abc300", "problem_id": "abc300_b", "result": "WA", "epoch_second": 3000},
        ]
        mock_fetch_code.return_value = "print('AC')"
        mock_git.return_value = (True, True)

        with patch("upload_contest.PROCESSED_SUBMISSIONS_FILE", self.processed_file), \
             patch("upload_contest.SOLUTIONS_DIR", self.solutions_dir), \
             patch("sys.argv", ["upload_contest.py", "all"]):
            main()

        # Check solutions created for both abc300 and arc180 AC submissions
        abc_file = os.path.join(self.solutions_dir, "ABC", "ABC300", "A", "01.py")
        arc_file = os.path.join(self.solutions_dir, "ARC", "ARC180", "A", "01.py")
        self.assertTrue(os.path.exists(abc_file))
        self.assertTrue(os.path.exists(arc_file))

        # Check git commit message called with "ALL CONTESTS"
        mock_git.assert_called_once()
        self.assertEqual(mock_git.call_args[0][0], "ALL CONTESTS")


if __name__ == "__main__":
    unittest.main()

