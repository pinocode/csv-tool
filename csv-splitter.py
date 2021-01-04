import click

from classes.CSVSplitter import CSVSplitter


@click.command()
@click.option("--source", "-s", "source", help="Source csv file to parse from.")
@click.option("--output", "-o", "output", help="Output csv file path.")
@click.option("--delimiter", "-d", "delimiter", default=";",
              help="delimiter char that the source file uses. Defaults to ;")
@click.option("--pick-columns", "-p", "pick_columns", default=[], multiple=True, type=int,
              help="Columns as numbers that are included in the output csv file.")
@click.option("--verbose", "-v", "verbose", is_flag=True, help="Show the new rows that are created.")
def split_csv(source, output, pick_columns, verbose, delimiter):
    pick_columns = list(pick_columns)
    new_lines = splitter.split_source_file(source, pick_columns, delimiter)

    if verbose:
        for row in new_lines:
            click.echo(f"{row}\n\t")
        click.echo(f"picked columns: {pick_columns}")
    splitter.create_output_file(output, new_lines)
    click.echo(f"created new csv file: {output}")


if __name__ == '__main__':
    splitter = CSVSplitter()
    split_csv()
