# AtCoder AC解答自動収集・GitHubアップロードシステム

## 1. 概要

本システムは、AtCoderで提出した解答のうち **AC（Accepted）となった解答をコンテスト単位で一括取得し、GitHub上の解答リポジトリへ保存・管理するためのシステム**である。

ユーザーは現在、Zed上で`atcoder_codetest.py`を編集し、問題を解いている。

```text
AtCoder/
└── atcoder_codetest.py
```

`atcoder_codetest.py`は問題ごとに使い回され、主に`main()`関数を書き換えることで解答を作成する。

解答の提出はブラウザ上のAtCoderから行い、テストケースの実行および、すべてのテストケースを通過した場合の自動提出には **AtCoder Easy Test v2** を使用する。

本システムは提出処理そのものには介入せず、コンテストやADTの学習終了後に指定したコンテストの提出履歴を取得し、ACとなった解答をGitHubリポジトリへ一括保存する。

---

## 2. 目的

本システムの目的は以下の通りである。

* AtCoderでACした解答を自動的にGitHubへ保存する
* コンテスト終了後にまとめて処理できるようにする
* 現在の`atcoder_codetest.py`を使い回す開発スタイルを変更しない
* 実際にAtCoderへ提出したコードを保存する
* 同じ問題を複数回解いた場合、それぞれの解答履歴を保存する
* ABC、ARCなどの通常コンテストに対応する
* ADTで出題された過去の問題にも対応する
* 同じ提出を複数回アップロードしない
* 解答の提出日時や提出IDなどの履歴を保存する
* 保存後にGitHubへ自動でcommitおよびpushする

---

## 3. システム全体像

通常の開発・提出フローは以下の通りとする。

```text
┌───────────────┐
│ Zed           │
│               │
│ atcoder_      │
│ codetest.py   │
└───────┬───────┘
        │
        │ main()を編集
        ▼
┌───────────────┐
│ AtCoder       │
│ ブラウザ      │
└───────┬───────┘
        │
        │ テストケース実行
        ▼
┌──────────────────┐
│ AtCoder Easy     │
│ Test v2          │
└───────┬──────────┘
        │
        │ 全テストケース通過
        ▼
┌───────────────┐
│ 自動提出      │
└───────────────┘
```

コンテストまたはADTの学習終了後、以下の処理を実行する。

```text
python upload_contest.py <contest_id>
```

実行後の処理は以下の通りである。

```text
コンテストIDを入力
        │
        ▼
AtCoderの提出履歴を取得
        │
        ▼
指定コンテストの提出を抽出
        │
        ▼
ACのみを抽出
        │
        ▼
提出IDが既に保存済みか確認
        │
        ├── 保存済み
        │      │
        │      └── スキップ
        │
        └── 未保存
               │
               ▼
        AtCoderから提出コードを取得
               │
               ▼
        problem_idから保存先を決定
               │
               ▼
        解答ファイルとして保存
               │
               ▼
        メタデータを更新
               │
               ▼
        Gitへ追加
               │
               ▼
        git commit
               │
               ▼
        git push
```

---

## 4. 基本的な利用方法

### 4.1 通常のABC

例えばABC300を解いた場合、以下のコマンドを実行する。

```bash
python upload_contest.py abc300
```

システムはABC300に対する自分の提出履歴を取得し、ACとなった解答を保存する。

---

### 4.2 ARC

ARC180を解いた場合は以下のように実行する。

```bash
python upload_contest.py arc180
```

---

### 4.3 ADT

ADTで解いた場合は、実際に参加したADTのコンテストIDを指定する。

例：

```bash
python upload_contest.py adt_all_20260811_1
```

ADTの場合でも、保存先はADTのコンテストIDではなく、**元の問題IDを基準として決定する**。

---

### 4.4 未アップロードAC解答の一括処理 (`all`)

過去のすべてのAC解答のうち、未保存の解答を一括でアップロードしたい場合は、コンテストIDに `all` を指定して実行する。

```bash
python upload_contest.py all
```

全コンテストの提出データから `result == "AC"` かつ未登録の提出IDを自動抽出し、各問題ごとのディレクトリへ古い順に一括保存およびGit Pushを行う。

---

## 5. ディレクトリ構成

リポジトリの基本構成を以下のようにする。

```text
AtCoder/
├── atcoder_codetest.py
├── upload_contest.py
│
├── data/
│   └── processed_submissions.json
│
└── solutions/
    ├── ABC/
    │   ├── ABC300/
    │   │   ├── A/
    │   │   │   ├── 01.py
    │   │   │   ├── 02.py
    │   │   │   └── metadata.json
    │   │   │
    │   │   ├── B/
    │   │   │   ├── 01.py
    │   │   │   └── metadata.json
    │   │   │
    │   │   └── C/
    │   │       ├── 01.py
    │   │       └── metadata.json
    │   │
    │   └── ABC348/
    │       └── D/
    │           ├── 01.py
    │           ├── 02.py
    │           └── metadata.json
    │
    └── ARC/
        └── ARC180/
            └── A/
                ├── 01.py
                └── metadata.json
```

---

## 6. 解答の保存単位

解答は以下の単位で管理する。

```text
問題
└── AC提出
    ├── 01.py
    ├── 02.py
    └── 03.py
```

例えばABC300のA問題を複数回解いて、それぞれACした場合、

```text
solutions/
└── ABC/
    └── ABC300/
        └── A/
            ├── 01.py
            ├── 02.py
            └── 03.py
```

のように保存する。

### 保存番号のルール

| ファイル    | 意味           |
| ------- | ------------ |
| `01.py` | 最初に保存したAC解答  |
| `02.py` | 2回目に保存したAC解答 |
| `03.py` | 3回目に保存したAC解答 |

保存番号は問題ごとに連番とする。

---

## 7. 同じ問題を複数回解いた場合

同じ問題に対して複数のAC提出が存在する場合、すべて別の解答として保存する。

例えば、

```text
ABC348 D
```

を最初に通常のABCで解いた場合、

```text
solutions/ABC/ABC348/D/01.py
```

に保存する。

その後、ADTで同じ問題を再び解いてACした場合、

```text
solutions/ABC/ABC348/D/02.py
```

に保存する。

さらに別の日に再度解いた場合、

```text
solutions/ABC/ABC348/D/03.py
```

に保存する。

この仕様により、同じ問題に対する複数回の挑戦と、自身の解法の変化を記録できる。

---

## 8. ADTへの対応

ADTでは、複数の過去コンテストから問題が選択される。

例えば、

```text
提出先コンテスト
adt_all_20260811_1
```

に対して、問題IDが以下のようになっている場合を考える。

```text
abc348_d
abc200_c
abc250_b
```

保存先はADTではなく、それぞれの問題が元々属しているコンテストを基準とする。

```text
abc348_d
↓
solutions/ABC/ABC348/D/

abc200_c
↓
solutions/ABC/ABC200/C/

abc250_b
↓
solutions/ABC/ABC250/B/
```

したがって、

```bash
python upload_contest.py adt_all_20260811_1
```

を実行すると、

```text
solutions/
└── ABC/
    ├── ABC348/
    │   └── D/
    │       └── 01.py
    │
    ├── ABC200/
    │   └── C/
    │       └── 01.py
    │
    └── ABC250/
        └── B/
            └── 01.py
```

のように保存する。

---

## 9. 保存先の決定方法

保存先は提出先の`contest_id`ではなく、問題IDである`problem_id`を基準とする。

例えば、

```text
problem_id = abc348_d
```

の場合、

```text
abc348
```

をコンテストID、

```text
d
```

を問題番号として扱う。

変換結果は以下の通りとする。

```text
abc348_d
↓
contest_type = ABC
contest_name = ABC348
problem_name = D
```

保存先は、

```text
solutions/ABC/ABC348/D/
```

となる。

---

## 10. 対応する問題ID

基本的には以下のような問題IDを処理対象とする。

```text
abc300_a
arc180_b
agc001_c
```

それぞれ以下のように保存する。

```text
abc300_a
→ solutions/ABC/ABC300/A/

arc180_b
→ solutions/ARC/ARC180/B/

agc001_c
→ solutions/AGC/AGC001/C/
```

将来的には、Typical90、Educational DP Contest、PASTなど、通常の形式と異なる問題IDにも対応できるよう拡張可能な設計とする。

---

## 11. AC提出の取得

指定されたコンテストIDに対して、自分の提出履歴を取得する。

例えば、

```bash
python upload_contest.py abc300
```

を実行した場合、

```text
contest_id == "abc300"
```

である提出を抽出する。

その中から、

```text
result == "AC"
```

である提出のみを保存対象とする。

対象外の結果は保存しない。

```text
WA
TLE
MLE
RE
CE
WJ
```

などは保存対象外とする。

---

## 12. 重複判定

同じ提出を複数回保存しないため、提出IDを利用して重複判定を行う。

例えば、

```text
Submission ID: 123456789
```

がすでに保存済みの場合、

```bash
python upload_contest.py abc300
```

を再実行しても再保存しない。

一方で、

```text
Submission ID: 123456999
```

が同じ問題に対する新しいAC提出であれば、新しい解答として保存する。

したがって、判定基準は以下とする。

```text
同じ問題ID
    ×
保存済みと判定する

同じ提出ID
    ○
保存済みと判定する
```

つまり、**問題IDではなく提出IDによって重複を判定する**。

---

## 13. 保存済み提出の管理

保存済みの提出IDは以下のファイルで管理する。

```text
data/processed_submissions.json
```

例：

```json
{
    "processed_submission_ids": [
        123456789,
        123456800,
        123456999
    ]
}
```

処理の流れは以下の通りである。

```text
提出情報を取得
        │
        ▼
submission_idを取得
        │
        ▼
processed_submissions.jsonを確認
        │
        ├── 存在する
        │       │
        │       └── スキップ
        │
        └── 存在しない
                │
                ▼
            解答を保存
                │
                ▼
            submission_idを追加
```

---

## 14. 提出コードの取得

保存するコードは、現在の`atcoder_codetest.py`から取得しない。

AtCoderに実際に提出されたコードを取得する。

理由は、提出後にユーザーが次の問題を解くために、

```text
atcoder_codetest.py
```

を書き換える可能性があるためである。

例えば、

```text
12:00 ABC300 Aを提出
12:01 B問題を解き始める
12:02 atcoder_codetest.pyを書き換える
12:03 upload_contest.pyを実行
```

という場合でも、保存するのは、

```text
12:00にABC300 AとしてAtCoderへ提出したコード
```

でなければならない。

そのため、AtCoderの提出ページから実際の提出コードを取得する。

---

## 15. メタデータの保存

各問題のディレクトリには、`metadata.json`を作成する。

例：

```json
{
    "problem_id": "abc348_d",
    "solutions": [
        {
            "file": "01.py",
            "submission_id": 123456789,
            "submitted_at": "2026-08-11T14:32:15+09:00",
            "submitted_contest": "abc348",
            "language": "Python (CPython)"
        },
        {
            "file": "02.py",
            "submission_id": 124000123,
            "submitted_at": "2026-08-20T19:15:22+09:00",
            "submitted_contest": "adt_all_20260811_1",
            "language": "Python (CPython)"
        }
    ]
}
```

これにより、同じ問題を複数回解いた場合でも、

* いつ解いたか
* どのコンテストまたはADTで解いたか
* AtCoder上の提出ID
* 使用した言語
* 対応する保存ファイル

を確認できる。

---

## 16. Gitへの保存

すべてのAC解答の取得と保存が完了した後、一括でGit操作を行う。

処理は以下の通りとする。

```text
git add <追加・変更されたファイル>

git commit -m "Add solutions for ABC300"

git push
```

ADTの場合は、

```text
git commit -m "Add solutions from adt_all_20260811_1"
```

などとする。

コンテスト内に新しい保存対象が存在しない場合は、commitおよびpushを行わない。

---

## 17. 実行例

### ABCの場合

```bash
python upload_contest.py abc300
```

出力例：

```text
=== Upload AtCoder Solutions ===

Target Contest: ABC300

Fetching submissions...

[ABC300 A]
Submission ID: 123456789
Status: AC
→ Saving as solutions/ABC/ABC300/A/01.py

[ABC300 B]
Submission ID: 123456800
Status: AC
→ Saving as solutions/ABC/ABC300/B/01.py

[ABC300 C]
Submission ID: 123456900
Status: AC
→ Saving as solutions/ABC/ABC300/C/01.py

Updating metadata...

Git commit...
Git push...

Completed!
```

---

### ADTの場合

```bash
python upload_contest.py adt_all_20260811_1
```

出力例：

```text
=== Upload AtCoder Solutions ===

Target Contest:
ADT_ALL_20260811_1

Fetching submissions...

[ABC348 D]
Submission ID: 123456789
Status: AC
→ Saving as solutions/ABC/ABC348/D/02.py

[ABC200 C]
Submission ID: 123456800
Status: AC
→ Saving as solutions/ABC/ABC200/C/01.py

[ABC250 B]
Submission ID: 123456900
Status: AC
→ Saving as solutions/ABC/ABC250/B/01.py

Updating metadata...

Git commit...
Git push...

Completed!
```

---

## 18. エラー処理

以下のケースを考慮する。

### 18.1 指定されたコンテストが存在しない

```text
ERROR:
Contest "abc999999" was not found.
```

---

### 18.2 AC提出が存在しない

```text
No accepted submissions found.
```

この場合、Git操作は行わない。

---

### 18.3 すべて保存済み

```text
No new accepted submissions found.
```

この場合もGit操作は行わない。

---

### 18.4 提出コードの取得に失敗

特定の提出コードの取得に失敗した場合、その提出をスキップせず、エラーとして表示する。

```text
Failed to fetch submission: 123456789
```

他の提出については可能な限り処理を継続する。

---

### 18.5 GitHubへのpushに失敗

`git push`が失敗した場合、保存した解答ファイルやメタデータはローカルに残る。

次回実行時に同じ解答を再取得しないよう、提出IDの管理タイミングには注意する。

原則として、

```text
コード保存
↓
metadata更新
↓
git add
↓
git commit
↓
git push
↓
processed_submissions.jsonを更新
```

の順序とする。

これにより、push失敗時に「GitHubへ保存されていないにもかかわらず、保存済みとして扱われる」状態を防ぐ。

---

## 19. 処理対象外

初期バージョンでは以下を対象外とする。

* WAなどの不正解提出の保存
* AC前の試行回数の保存
* 提出コードの差分解析
* 解答アルゴリズムの自動分類
* 問題文や制約の保存
* 解説の自動生成
* AtCoderへの自動提出

これらは将来的な拡張機能とする。

---

## 20. 将来的な拡張案

### 20.1 解答ごとの差分表示

同じ問題の、

```text
01.py
02.py
03.py
```

について、どのようにコードが変化したか確認できるようにする。

---

### 20.2 解き直し回数の可視化

各問題について、

```text
ABC348 D

1回目：2026-08-01
2回目：2026-08-11
3回目：2026-08-20
```

のような履歴を自動生成する。

---

### 20.3 READMEの自動生成

リポジトリ全体のREADMEに、

```text
Solved Problems

ABC: 150
ARC: 30
AGC: 5

Total AC Records: 220
```

などの統計情報を自動生成する。

---

### 20.4 コンテスト以外の一括取得

例えば、

```bash
python upload_problem.py abc348_d
```

によって、特定の問題だけのAC履歴をすべて取得できるようにする。

---

### 20.5 日付範囲による取得

例えば、

```bash
python upload_date.py 2026-08-01 2026-08-31
```

のように指定期間中のACをまとめて保存できるようにする。

---

## 21. 最終仕様

本システムは以下のコマンドを基本インターフェースとする。

```bash
python upload_contest.py <contest_id>
```

処理対象は、

```text
指定コンテストに対する自分の提出
```

であり、その中から、

```text
AC
かつ
未保存の提出ID
```

のみを抽出する。

保存先は、

```text
提出先のcontest_id
```

ではなく、

```text
problem_id
```

から決定する。

したがって、通常のABCだけでなく、ADTから解いた問題についても、

```text
元の問題が属するコンテスト
```

に分類して保存する。

同じ問題を複数回解いた場合は、提出IDごとに別の解答として保存する。

```text
ABC348/D/
├── 01.py
├── 02.py
└── 03.py
```

これにより、現在の`atcoder_codetest.py`を使い回す開発スタイルを維持したまま、AtCoderにおける解答履歴をGitHub上へ体系的に蓄積することを目指す。
