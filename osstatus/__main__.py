import json
from dataclasses import asdict
from enum import Enum

import click
from pygments import formatters, highlight, lexers

from osstatus import cache


def default_json_encoder(obj):
    if isinstance(obj, Enum):
        return str(obj)
    raise TypeError()


def print_json(buf, colored=True, default=default_json_encoder):
    formatted_json = json.dumps(buf, sort_keys=True, indent=4, default=default)
    if colored:
        colorful_json = highlight(formatted_json, lexers.JsonLexer(),
                                  formatters.TerminalTrueColorFormatter(style='stata-dark'))
        print(colorful_json)
    else:
        print(formatted_json)


@click.group()
def cli():
    """ query error codes """
    pass


@cli.command('all')
@click.option('--color/--no-color', default=True, help='colored output')
def all_(color: bool):
    """ get all possible errors codes """
    result = []
    for options in cache.get_all_errors_codes().values():
        for option in options:
            result.append(asdict(option))
    print_json(result, colored=color)


@cli.command()
@click.argument('value', type=click.INT)
@click.option('--color/--no-color', default=True, help='colored output')
def code(value: int, color: bool):
    """ get all possible errors codes by error code """
    result = []
    for entry in cache.get_possible_error_codes(value):
        result.append(asdict(entry))
    print_json(result, colored=color)


@cli.command()
@click.argument('name')
@click.option('--color/--no-color', default=True, help='colored output')
def symbol(name: str, color):
    """ get all possible errors codes by symbol name """
    result = []
    for options in cache.get_all_errors_codes().values():
        for option in options:
            if option.name != name:
                continue
            result.append(asdict(option))
    print_json(result, colored=color)


if __name__ == '__main__':
    cli()
