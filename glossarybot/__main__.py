import logging
import aiohttp
import importlib
import argparse

from discord.ext.commands import Bot

import glossarybot

import glossarybot

logger = logging.getLogger(__name__)

description = """
    One of the shiniest possible bot for discord: Glossary bot.

    Made from a pirated version of a good ol' Pimoroni Robot

    Version {version}

    Commands should be prefixed with '{prefix}' and are not case sensitive.

    The source code for the Glossary-bot can be found here:
        {base_url}

    The original Pimoroni source can be found here:
        {pimodispo_url}
"""

ORIGIN_URL = "https://github.com/ali1234/pimodisco"

extensions = [
    'pimodisco.filter',
    'pimodisco.checks',
    'pimodisco.commands',
]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--config', required=True, is_config_file=True, help='Config file path.')

    loaded_extensions = [importlib.import_module(e) for e in extensions]
    for e in loaded_extensions:
        if e.setup_args:
            e.setup_args(parser)

    args = parser.parse_args()

    bot = Bot(
                command_prefix=args.prefix, formatter=glossarybot.Formatter(),
                description=description.format(version=glossarybot.version,
                                               prefix=args.prefix,
                                               base_url=glossarybot.source_url,
                                               pimodiso_url=ORIGIN_URL)
             )

    with aiohttp.ClientSession() as session:
        bot.aiohttp = session
        for e in loaded_extensions:
            e.setup(bot, args)
        bot.run(args.token)


if __name__ == '__main__':
    main()



