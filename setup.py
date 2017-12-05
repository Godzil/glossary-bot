from setuptools import setup
from pimodisco import version, source_url

setup(
    name='pimodisco',
    keywords='Pimoroni Discord Bot',
    version=version,
    url=source_url,
    license='GPLv3+',
    packages=['pimodisco'],
    package_data={'pimodisco': ['data/badwords.txt']},
    install_requires=[
        'discord', 'algoliasearch', 'markdown', 'pyyaml', 'inflection'
    ],
    entry_points={
        'console_scripts': [
            'pimodisco = pimodisco.__main__:main'
        ]
    },
)
