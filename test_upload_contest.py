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
    ProblemParser,
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

        # 2回目の保存 (ADTなどから同じ問題を解いた場合)
        rel_path2, fname2 = self.storage.save_solution(
            contest_type="ABC",
            contest_name="ABC348",
            problem_name="D",
            problem_id="abc348_d",
            submission_id=124000123,
            submitted_at="2026-08-20T19:15:22+09:00",
            submitted_contest="adt_all_20260811_1",
            language="Python (CPython)",
            code="print('Hello 2')",
        )
        self.assertEqual(fname2, "02.py")
        self.assertTrue(os.path.exists(os.path.join(self.solutions_dir, "ABC", "ABC348", "D", "02.py")))

        with open(meta_path, "r", encoding="utf-8") as f:
            meta = json.load(f)
        self.assertEqual(len(meta["solutions"]), 2)
        self.assertEqual(meta["solutions"][1]["file"], "02.py")
        self.assertEqual(meta["solutions"][1]["submitted_contest"], "adt_all_20260811_1")


class TestTimestampFormat(unittest.TestCase):
    def test_format_iso_timestamp(self):
        ts = 1786426335  # 2026-08-11 14:32:15 JST approximate timestamp
        formatted = format_iso_timestamp(ts)
        self.assertIn("+09:00", formatted)


if __name__ == "__main__":
    unittest.main()
