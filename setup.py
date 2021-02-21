import os
from setuptools import setup


setup(
    name = 'word2num_de',
    packages = ['word2num_de'],
    version = '0.1',
    license=open('LICENSE').read(),
    description = 'Transforms written numbers in German to numbers.',
    author = 'Kaoru S.',
    author_email = '',
    url = 'https://github.com/kaorusss/word2num-de',
    download_url = 'https://github.com/kaorusss/word2num/archive/v_01.tar.gz',
    keywords = ['numbers', 'convert', 'words', 'german', 'transform'],
    classifiers=[
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'Programming Language :: Python :: 3'
    ],
)