import os

from pkg_resources import get_build_platform
from setuptools import setup


def read_relative(file_name):
    here = os.path.dirname(__file__)
    with open(os.path.join(here, file_name)) as handle:
        return handle.read()


def get_version():
    contents = {}
    exec(read_relative("micropsi_integration_sdk/version.py"), contents)
    return contents["VERSION"]


setup(
    name="micropsi-integration-sdk",
    version=get_version(),
    author="Micropsi Industries",
    author_email="contact@micropsi-industries.com",
    url="https://github.com/micropsi-industries/micropsi-integration-sdk",
    description="Integration SDK for Micropsi Industries",
    long_description=read_relative('README.md'),
    long_description_content_type='text/markdown',
    packages=["micropsi_integration_sdk"],
    install_requires=["numpy", "pyquaternion"],
    entry_points={
        "console_scripts": ["mirai-sandbox=micropsi_integration_sdk.sandbox:main"],
    },
    platforms=[get_build_platform()],
    python_requires=">=3.6, <4",
    license="MIT",
)
