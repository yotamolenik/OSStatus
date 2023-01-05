import click
import requests
from bs4 import BeautifulSoup


def tat_smaller(tag1, tag2):
    pass

@click.group()
@click.pass_context
def cli(ctx):
    """ get error code information from the OSStatus website """
    ctx.ensure_object(dict)
    response = requests.get('https://www.osstatus.com/search/results?platform=all&framework=all&search=')
    soup = BeautifulSoup(response.text, 'html.parser')
    tbody = soup.find('tbody')
    trs = tbody.find_all('tr')
    # trs.sort()
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


@cli.command()
@click.argument('code', type=int)
def get_code_info(code):
    """ get information about a single error code """
    response = requests.get(f'https://www.osstatus.com/search/results?platform=all&framework=all&search={code}')
    soup = BeautifulSoup(response.text, 'html.parser')
    tbody = soup.find('tbody')
    trs = tbody.find_all('tr')
    for tr in trs:
        td_list = tr.find_all('td')
        num_td = td_list[3]
        num_str = num_td.get_text()
        print(int(num_str))
        print(type(int(num_str)))


if __name__ == '__main__':
    cli()
