import click

from classes.CSVMerger import CSVMerger
from classes.CSVSplitter import CSVSplitter


@click.command()
@click.option("--source1", "-s1", "source", type=str, help="Source csv file to parse from.")
@click.option("--source1", "-s1", "source", type=str, help="Source csv file to parse from.")
@click.option("--output", "-o", "output", help="Output csv file path.")
@click.option("--delimiter", "-d", "delimiter", default=";",
              help="delimiter char that the source file uses. Defaults to ;")
@click.option("--verbose", "-v", "verbose", is_flag=True, help="Show the new rows that are created.")
def merge_csv(source, output, verbose, delimiter):
    sources = list(source)
    read_sources = {}
    for index, source in sources:
        new_lines = splitter.split_source_file(source, [], delimiter)
        read_sources.update(index, new_lines)

    merged_new_lines = CSVMerger.merge_csv_files(read_sources, delimiter)

    if verbose:
        for row in merged_new_lines:
            click.echo(f"{row}\n\t")
    splitter.create_output_file(output, merged_new_lines)
    click.echo(f"created new csv file: {output}")


if __name__ == '__main__':
    splitter = CSVSplitter()
    merger = CSVMerger()
    merge_csv()
