import requests
from bs4 import BeautifulSoup
import click


@click.group()
def cli():
    pass


@click.command()
def print_all():
    pass


@click.command()
def get_all():
    pass


if __name__ == '__main__':
    cli()
