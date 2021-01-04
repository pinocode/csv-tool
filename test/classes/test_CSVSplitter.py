from unittest import TestCase

from classes.CSVSplitter import CSVSplitter


class TestCSVSplitter(TestCase):
    def test_read_source_return_exepected_amount_of_columns_in_row(self):
        source_file_path = "./../data/valtuusasiat.csv"
        expected_len = 3

        new_files = CSVSplitter.split_source_file(source_file_path, [1, 5, 9], ";")

        actual_len = len(new_files[0].split(";"))
        self.assertEqual(expected_len, actual_len)

    def test_read_source_without_delimiters_uses_semicolon_as_delimiter(self):
        source_file_path = "./../data/valtuusasiat.csv"
        expected_len = 3

        new_files = CSVSplitter.split_source_file(source_file_path, [1, 5, 9], "")

        actual_len = len(new_files[0].split(";"))
        self.assertEqual(expected_len, actual_len)

    def test_read_source_with_empty_pick_columns_list_returns_all_colus_picked(self):
        source_file_path = "./../data/valtuusasiat.csv"
        expected_len = 11

        new_files = CSVSplitter.split_source_file(source_file_path, [], "")

        actual_len = len(new_files[0].split(";"))
        self.assertEqual(expected_len, actual_len)
