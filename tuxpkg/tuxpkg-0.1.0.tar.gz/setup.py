#!/usr/bin/env python
# setup.py generated by flit for tools that don't yet use PEP 517

from distutils.core import setup

packages = \
['tuxpkg']

package_data = \
{'': ['*'], 'tuxpkg': ['data/*']}

entry_points = \
{'console_scripts': ['tuxpkg = tuxpkg.__main__:main']}

setup(name='tuxpkg',
      version='0.1.0',
      description='Release automation tool for Python projects',
      author='Antonio Terceiro',
      author_email='antonio.terceiro@linaro.org',
      url='https://gitlab.com/Linaro/tuxpkg',
      packages=packages,
      package_data=package_data,
      entry_points=entry_points,
     )
