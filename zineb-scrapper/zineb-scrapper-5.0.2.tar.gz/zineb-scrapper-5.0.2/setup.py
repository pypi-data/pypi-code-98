#!/usr/bin/env python

import re
from os import path

import setuptools

ROOT = path.abspath(path.dirname(__file__))


def read_files(filename):
    with open(path.join(ROOT, filename), 'r', encoding='utf-8') as f:
        data = f.read()
        return data


def get_version(filename):
    data = read_files(filename)
    is_match = re.match(r"^__version__.*['](.*)[']", data)
    if not is_match:
        raise ValueError('Could not get version')
    return is_match.group(1)


classifiers = [
    'Development Status :: 3 - Alpha',

    'Environment :: Console',

    'License :: OSI Approved :: MIT License',

    'Operating System :: POSIX',
    'Operating System :: Unix',
    'Operating System :: MacOS :: MacOS X',
    'Operating System :: Microsoft :: Windows :: Windows 10',

    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.9',

    'Natural Language :: English',

    'Intended Audience :: Developers',
    'Intended Audience :: Science/Research',

    'Topic :: Internet',
    'Topic :: Internet :: WWW/HTTP',
    'Topic :: Software Development :: Libraries :: Application Frameworks',
    'Topic :: Software Development :: Libraries :: Python Modules'
]

install_requires = [
    'beautifulsoup4>=4.9.3',
    # 'numpy==1.19.3',
    'numpy',
    'requests',
    'Pillow>=8.0.1',
    'jupyter',
    'pandas',
    # 'PyDispatcher',
    'w3lib',
    # 'nltk',
    'pyyaml',
    # 'scikit-learn'
]

setuptools.setup(
    name='zineb-scrapper',
    # packages: [],
    # version='3.0.0',
    version=get_version('version.py'),
    author='John Pendenque',
    author_email='pendenquejohn@gmail.com',
    classifiers=classifiers,
    description='Advanced web scrapper for machine learning and data science buit around BeautifulSoup and Pandas',
    install_requires=install_requires,
    keywords=['python', 'web scrapping', 'scrapping'],
    license='MIT',
    long_description=read_files('README.md'),
    long_description_content_type='text/markdown',
    python_requires='>=3.9',
    project_urls={
        'Source': 'https://github.com/Zadigo/zineb/'
    }
)
