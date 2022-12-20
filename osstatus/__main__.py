import click
import requests
from bs4 import BeautifulSoup


@click.group()
@click.pass_context
def cli(ctx):
    """ get error code information from the OSStatus website """
    ctx.ensure_object(dict)
    response = requests.get("https://www.osstatus.com/search/results?platform=all&framework=all&search=")
    soup = BeautifulSoup(response.text, 'html.parser')
    tbody = soup.find('tbody')
    trs = tbody.find_all('tr')
    ctx.obj['table_rows'] = trs


@cli.command()
@click.pass_context
def print_all(ctx):
    """ print all errors to stdout """
    for tr in ctx.obj['table_rows']:
        print(tr)


@cli.command()
@click.pass_context
def get_all(ctx):
    """ return all errors """
    return ctx.obj['table_rows']


if __name__ == '__main__':
    cli()
