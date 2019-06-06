from setuptools import setup
import glossarybot

setup(
    name='Glossary bot for Discord',
    keywords='Glossary-bot',
    version=glossarybot.version,
    url=glossarybot.source_url,
    license='GPLv3+',
    packages=['glossary-bot'],
    install_requires=[
        'discord.py>=1.1.0',
    ],
    dependency_links=[
        'discord.py'
    ],
    entry_points={
        'console_scripts': [
            'glossarybot = glossarybot.__main__:main'
        ]
    },
)
