import requests
from bs4 import BeautifulSoup
import click



def cli(ctx, directory):
    """ Parse .mobileconfig files in a given directory """
    ctx.ensure_object(dict)
    ctx.obj['directory'] = directory


@click.group()
@click.pass_context
def cli(ctx):
    ctx.ensure_object(dict)
    response = requests.get("https://www.osstatus.com/search/results?platform=all&framework=all&search=")
    soup = BeautifulSoup(response.text, 'html.parser')
    tbody = soup.find('tbody')
    trs = tbody.find_all('tr')
    ctx.obj['table_rows'] = trs


@click.command()
@click.pass_context
def print_all(ctx):
    for tr in ctx.obj['table_rows']:
        print(tr)


@click.command()
@click.pass_context
def get_all(ctx):
    return ctx.obj['table_rows']


if __name__ == '__main__':
    cli()
