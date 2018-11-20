from pathlib import Path
import os

import click


def print_msg_success(msg):
    click.secho(msg, fg='green')


def print_msg_error(msg):
    click.secho(msg, fg='red')


def print_msg(msg):
    click.echo(msg)


def print_cmds(lst):
    click.secho("RESULTS", underline=True, bold=True)
    for cmd, desc in lst:
        cmd_str = click.style(cmd, fg="blue")
        if desc == '':
            click.echo('{}\n'.format(cmd_str))
        else:
            click.echo(
                '{} - {}\n'.format(
                    cmd_str,
                    click.style(desc, fg="cyan")
                )
            )


def get_db_filename():
    filepath = Path(os.getenv('QC_DB_DIR', '~')
                    ).expanduser() / '.qc-commands.db'
    filename = str(filepath)

    return filename
