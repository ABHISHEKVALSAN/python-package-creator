from io import open
from setuptools import setup
import sys
import pylibgen

setup(
    name='pylibgen',
    version=pylibgen.__version__,
    description='A python package that facilitates creating other python package',
    python_requires='>=3.0',
    keywords='python library package tool generator templates',
    packages=[
        'pylibgen',
        'pylibgen.template.init.app',
        'pylibgen.template.init.app.predictor',
        'pylibgen.template.init.app.loader',
        'pylibgen.template.init.app.transformers',
        'pylibgen.template.init.app.evaluate',
        'pylibgen.template.init.tests.unit',
        'pylibgen.template',
        'pylibgen.config',
        'pylibgen.handlers',
        'pylibgen.handlers.init',
        'pylibgen.handlers.env',
        'pylibgen.handlers.pip',
        'pylibgen.handlers.python_cli',
        'pylibgen.handlers.generate',
        'pylibgen.handlers.app_server',
        'pylibgen.handlers.deployment',
        'pylibgen.handlers.evaluate',
        'pylibgen.handlers.runner',
        'pylibgen.handlers.upload',
        'pylibgen.handlers.convert',
        'pylibgen.handlers.tag_deployment',
        'pylibgen.utils'
    ],
    zip_safe=True,
    install_requires=[
        "flask",
        "inflection",
        "gunicorn",
        "pandas",
        "requests",
        "simplejson",
        "setuptools>=39.2.0",
        "cython==0.29.13",
        "joblib",
    ],
    package_data={
        '': [
            'config/*',
            'template/*'
        ]
    },
    entry_points={
        'console_scripts': [
            'pylibgen=pylibgen.__main__:main',
        ],
    },
)
