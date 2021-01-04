from classes.CSVSplitter import CSVSplitter


class CSVMerger:
    """
    Class for merging two or more CSV files.
    """

    @staticmethod
    def merge_csv_files(source_1_lines: list, source_2_lines: list, delimiter: str = ";") -> list:
        """
        Merge tw or more CSV files lines.

        :param source_1_lines: lines of the source files as list
        :param source_2_lines: lines of the source files as list
        :param delimiter: delimiter to use to seaparate columns
        :return: new merged lines as single list
        """
        if not delimiter:
            delimiter = ";"
        print(source_1_lines)
        new_lines = []
        column_count = len(source_1_lines)
        for index in range(column_count):
            new_line = source_1_lines[index].replace("\n", delimiter) + source_2_lines[index]
            new_lines.append(new_line)

        return new_lines
