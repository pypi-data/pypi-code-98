# -*-coding: utf-8 -*-
"""
    @File   : setup.py.py
    @Author : panjq
    @E-mail : pan_jinquan@163.com
    @Date   : 2019-06-12 20:13:04
"""
import os
import dldtrainer
from setuptools import setup, find_packages

root = os.path.dirname(__file__)
setup(name='dldtrainer',
      version=dldtrainer.__version__,
      description='dldtrainer',
      url='https://github.com/PanJinquan',
      author='PanJinquan',
      author_email='pan_jinquan@163.com',
      license='MIT',
      packages=find_packages(where=".",
                             exclude=["build", "configs", "data", "dist", "dldtrainer.egg-info", "test",
                                      '.idea', ".gitignore",
                                      ]),  # 为空为全部
      package_data={
          # 如果包中含有.txt文件，则包含它
          'pjq': ['*.jpg'],
          # 包含demo包data文件夹中的 *.dat文件
          'demo': ['data/*.dat']
      },
      install_requires=[
          # 'pandas>=0.20.0',  # 所需要包的版本号
          # 'numpy>=1.14.0'  # 所需要包的版本号
      ],
      zip_safe=False)
