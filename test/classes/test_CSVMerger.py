from unittest import TestCase

from classes.CSVMerger import CSVMerger


class TestCSVMerger(TestCase):
    def test_merge_csv_files_should_return_a_list_with_concatenated_strings(self):
        source_1_lines = ['jee', ';', 'jaa', ';', 'joo', '\n']
        source_2_lines = ['1', ';', '2', ';', '3', '\n']
        expected_output = ['jee1', 'jaa2', 'joo3']

        result = CSVMerger.merge_csv_files(source_1_lines, source_2_lines, ";")

        self.assertEqual(result, expected_output)
