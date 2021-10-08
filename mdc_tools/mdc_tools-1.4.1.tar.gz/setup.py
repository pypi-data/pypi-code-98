from setuptools import setup, find_packages
import glob

setup(
    name="mdc_tools",
    version="1.4.1",
    author="Dechao Meng",
    author_email="dechao.meng@vipl.ict.ac.cn",
    url="https://github.com/silverbulletmdc/mdc_tools",
    # keywords=("pytorch", "vehicle", "ReID"),
    description="Personal tools",
    scripts=glob.glob('scripts/*'),
    install_requires=["jstyleson"],
    # long_description="",
    packages=find_packages(exclude=('examples', 'examples.*')),
)
