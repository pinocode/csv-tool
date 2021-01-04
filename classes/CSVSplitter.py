class CSVSplitter:
    """Class for splitting csv files and picking columns"""
    i = 12345

    @staticmethod
    def create_output_file(output_path: str, lines: list = []):
        with open(output_path, 'w') as output_file:
            output_file.writelines(lines)

    @staticmethod
    def split_source_file(source: str, pick_columns: list = [], delimiter: str = ";") -> list:
        """
        Returns a subset of user selected columns of given CSV sourcefile.

        Reads an input csv-file row by row and picks columns selected by the user.
        Returns a list of rows created by concatenating the columns picked to a single line.
        If picked column numbers are not given, all columns are included.

        :param source: source file to read from
        :param delimiter: delimiter that the source file uses
        :param pick_columns: list of column index that are meant to be in the created csv output file
        :return new_lines: a list of rows that were constructed from the columns user picked
        """
        if not delimiter:
            delimiter = ";"

        new_lines = []
        with open(source) as source_file:
            # read lines from file
            for row in source_file:
                picked_columns = CSVSplitter.split_row(pick_columns, row, delimiter)
                new_lines.append(delimiter.join(picked_columns) + "\n")

        return new_lines

    @staticmethod
    def split_row(pick_columns: list, row: str, delimiter: str) -> list:
        """
        :param delimiter:
        :param pick_columns:
        :param row:
        :return: list of columns
        """

        if not delimiter:
            delimiter = ";"
        # split row
        columns = row.split(delimiter)
        # if columns is meant to be preserved, put it in new lines
        picked_columns = []
        for index, word in enumerate(columns):
            if index in list(pick_columns) or not pick_columns:
                picked_columns.append(word)

        return picked_columns
