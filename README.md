# AtCoder AC解答自動収集・GitHubアップロードシステム

AtCoderで提出した解答のうち **AC（Accepted）となった解答をコンテスト単位で一括取得し、構造化してGitHubへ保存・管理するシステム** です。

通常のABC/ARC/AGC等のコンテストに加え、**ADT（AtCoder Daily Training）で解いた問題についても元のコンテスト・問題別に自動分類** して永続化します。

---

## 🌟 特徴

* 🤖 **AC解答の自動収集**: 指定したコンテストの自分の全提出からAC（正解）データのみを自動抽出して保存。
* 📁 **問題別の自動分類**: ADTなどで提出された問題も元のコンテスト（例: `ABC348 D`）のディレクトリ構造へ自動割り振り。
* 🔄 **解答履歴のナンバリング**: 同じ問題を複数回解いた場合も `01.py`, `02.py` の連番ファイルとして保存し、解法の変化を記録。
* 📝 **メタデータの自動保存**: 各問題フォルダに `metadata.json` を生成し、提出日時（JST）、提出ID、使用言語、提出先コンテスト等を記録。
* 🚫 **重複防止機能**: `data/processed_submissions.json` で提出IDを追跡し、重複アップロードを防止。
* 🚀 **Git連携の自動化**: 保存完了後に `git commit` 及び `git push` を一括自動実行。

---

## 📁 ディレクトリ構成

```text
AtCoder/
├── atcoder_codetest.py       # 問題を解く際に使用するテンプレートファイル
├── upload_contest.py          # 解答取得・アップロード用メインスクリプト
├── test_upload_contest.py     # ユニットテストスクリプト
├── config.json                # 設定ファイル（AtCoderユーザーID等）
├── requirements.txt           # 依存パッケージ一覧
│
├── data/
│   └── processed_submissions.json  # 保存済み提出IDの管理用ファイル
│
└── solutions/                 # 保存された解答コード群
    ├── ABC/
    │   ├── ABC300/
    │   │   ├── A/
    │   │   │   ├── 01.py
    │   │   │   └── metadata.json
    │   │   └── B/
    │   │       ├── 01.py
    │   │       └── metadata.json
    │   └── ABC348/
    │       └── D/
    │           ├── 01.py
    │           ├── 02.py
    │           └── metadata.json
    └── ARC/
        └── ARC180/
            └── A/
                ├── 01.py
                └── metadata.json
```

---

## ⚙️ セットアップ

### 1. 依存ライブラリのインストール

Python 3.10 以上がインストールされている環境で、必要なパッケージをインストールします。

```bash
pip install -r requirements.txt
```

*(主要な依存パッケージ: `requests`, `beautifulsoup4`)*

### 2. 設定ファイル (`config.json`) の準備

プロジェクトルートに `config.json` を作成し、ご自身の AtCoder ユーザーIDを設定します。

```json
{
    "atcoder_user_id": "[ご自身の AtCoder ユーザーID]"
}
```

※ `config.json` が未作成の場合は、スクリプト実行時に対話形式でユーザーIDの入力と自動保存が行われます。

---

## 🚀 使い方

`upload_contest.py` に対象のコンテストIDを指定して実行します。

### 1. 通常のABC / ARC / AGC / AHC

```bash
# ABC300 のAC解答を取得・保存
python upload_contest.py abc300

# ARC180 のAC解答を取得・保存
python upload_contest.py arc180
```

### 2. ADT (AtCoder Daily Training)

ADTのコンテストIDを指定して実行すると、出題された各問題が**元々属していたコンテスト配下**に自動分類されます。

```bash
python upload_contest.py adt_all_20260811_1
```

### 💡 オプション引数

* `--user <USER_ID>`: `config.json` の設定をオーバーライドして別のユーザーIDを指定します。
* `--no-push`: 解答の取得・保存およびメタデータ更新のみを行い、`git push`（および `git commit`）をスキップします。

```bash
# Git push を行わずにテスト実行する場合
python upload_contest.py abc300 --no-push
```

---

## 📊 metadata.json の仕様例

各問題の保存先ディレクトリ（例: `solutions/ABC/ABC348/D/metadata.json`）には、以下のようなメタデータが保存されます。

```json
{
    "problem_id": "abc348_d",
    "solutions": [
        {
            "file": "01.py",
            "submission_id": 78377026,
            "submitted_at": "2026-08-11T14:32:15+09:00",
            "submitted_contest": "abc348",
            "language": "Python (PyPy 3.11-v7.3.20)"
        },
        {
            "file": "02.py",
            "submission_id": 78434988,
            "submitted_at": "2026-08-20T19:15:22+09:00",
            "submitted_contest": "adt_all_20260811_1",
            "language": "Python (PyPy 3.11-v7.3.20)"
        }
    ]
}
```

---

## 🧪 テストの実行

ユニットテストを実行してロジックの正常性を検証できます。

```bash
python -m unittest test_upload_contest.py
```
