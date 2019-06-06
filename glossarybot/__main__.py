import logging
logger = logging.getLogger(__name__)

import aiohttp
from importlib import import_module
from configargparse import ArgumentParser
from discord.ext.commands import Bot

from pimodisco import source_url, version as version__
from pimodisco.formatter import Formatter


description="""
    A good ol' Pimoroni Robot (Pirated, of course)
    Version {}

    Commands should be prefixed with '{}' and are not case sensitive.

    The source code for the Pimoroni Bot can be found here:
        {}
"""

extensions = [
    'pimodisco.filter',
    'pimodisco.checks',
    'pimodisco.commands',
    'pimodisco.github',
    'pimodisco.pinout',
    'pimodisco.product',
    'pimodisco.youtube',
]


def main():
    parser = ArgumentParser()
    parser.add_argument('-c', '--config', required=True, is_config_file=True, help='Config file path.')
    parser.add_argument('-t', '--token', metavar='DISCORD_BOT_TOKEN', required=True, env_var='DISCORD_BOT_TOKEN', help='Discord bot token.')
    parser.add_argument('-p', '--prefix', metavar='COMMAND_PREFIX', default='!', env_var='COMMAND_PREFIX', help='Command prefix.')

    loaded_extensions = [import_module(e) for e in extensions]
    for e in loaded_extensions:
        e.setup_args(parser)

    args = parser.parse_args()

    bot = Bot(
                command_prefix=args.prefix, formatter=Formatter(),
                description=description.format(version__, args.prefix, source_url)
             )

    with aiohttp.ClientSession() as session:
        bot.aiohttp = session
        for e in loaded_extensions:
            e.setup(bot, args)
        bot.run(args.token)

if __name__ == '__main__':
    main()



