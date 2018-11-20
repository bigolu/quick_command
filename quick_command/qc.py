from .qcdb import QCDB
from .util import print_msg_error, print_msg_success, print_cmds, print_msg, \
    get_db_filename

from pick import pick
import click

DB = QCDB(get_db_filename())


@click.group()
def qc():
    """quick-command: a cli for remembering commands"""
    pass


@qc.command()
def add():
    """add a new command"""
    cmd = click.prompt('command')
    desc = click.prompt('description (leave blank to omit)', default='')
    DB.put(cmd, desc)
    print_msg_success('saved!')


@qc.command()
def rm():
    """remove a command """
    records = DB.getall()
    option, index = pick(
        [cmd for cmd, _ in records],
        'choose a command to remove'
    )
    if DB.delete(option):
        print_msg_success('removed!')
    else:
        print_msg_error('something went wrong :/')


@qc.command()
@click.argument('cmd', required=False)
def find(cmd):
    """find a command by name or description"""
    records = None
    if cmd is not None:
        records = DB.get_by_cmd(cmd)
    else:
        desc = click.prompt('Enter description')
        records = DB.get_by_desc(desc)
    if len(records) == 0:
        print_msg_error('No commands found.')
    else:
        print_cmds(records)


@qc.command()
def list():
    """prints all commands"""
    print_cmds(DB.getall(True))


@qc.command()
def db():
    """print path to db"""
    print_msg(get_db_filename())
