# -*- coding: utf-8 -*-

import click
import asyncio
from pyasyncmail import pyasyncmail 
from pyasyncmail.pyasyncmail import main_mail


@click.command()
def main(args=None):
    """Console script for pyasyncmail"""
    click.echo("Will start sending to all the people")
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main_mail())
    click.echo("all mails sent")


if __name__ == "__main__":
    main()

