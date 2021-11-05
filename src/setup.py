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
    packages=[],
    zip_safe=True,
    install_requires=[],
    package_data={},
    entry_points={
        'console_scripts': [
            'pylibgen=pylibgen.__main__:main',
        ],
    },
)
