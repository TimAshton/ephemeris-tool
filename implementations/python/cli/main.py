#main.py

import click

from Vocab import Vocab
from LiveView import LiveView

@click.command()
@click.argument("tool")
@click.version_option("0.0.1", prog_name="Ephemeris Tool")
def cli(tool):
    if tool == "vocab":
        app = Vocab()
    else:
        app = LiveView()
    

if __name__ == "__main__":
    cli()