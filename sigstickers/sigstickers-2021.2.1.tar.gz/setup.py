# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['sigstickers']

package_data = \
{'': ['*']}

install_requires = \
['Pillow>=8.1.0,<10',
 'anyio>=2.0.2,<4',
 'emoji>=0.6.0,<2',
 'signalstickers-client>=3.0.0,<5']

entry_points = \
{'console_scripts': ['sigstickers = sigstickers:cli']}

setup_kwargs = {
    'name': 'sigstickers',
    'version': '2021.2.1',
    'description': 'Download sticker packs from Signal',
    'long_description': '[![GitHub top language](https://img.shields.io/github/languages/top/FHPythonUtils/SigStickers.svg?style=for-the-badge)](../../)\n[![Repository size](https://img.shields.io/github/repo-size/FHPythonUtils/SigStickers.svg?style=for-the-badge)](../../)\n[![Issues](https://img.shields.io/github/issues/FHPythonUtils/SigStickers.svg?style=for-the-badge)](../../issues)\n[![License](https://img.shields.io/github/license/FHPythonUtils/SigStickers.svg?style=for-the-badge)](/LICENSE.md)\n[![Commit activity](https://img.shields.io/github/commit-activity/m/FHPythonUtils/SigStickers.svg?style=for-the-badge)](../../commits/master)\n[![Last commit](https://img.shields.io/github/last-commit/FHPythonUtils/SigStickers.svg?style=for-the-badge)](../../commits/master)\n[![PyPI Downloads](https://img.shields.io/pypi/dm/sigstickers.svg?style=for-the-badge)](https://pypistats.org/packages/sigstickers)\n[![PyPI Total Downloads](https://img.shields.io/badge/dynamic/json?style=for-the-badge&label=total%20downloads&query=%24.total_downloads&url=https%3A%2F%2Fapi.pepy.tech%2Fapi%2Fprojects%2Fsigstickers)](https://pepy.tech/project/sigstickers)\n[![PyPI Version](https://img.shields.io/pypi/v/sigstickers.svg?style=for-the-badge)](https://pypi.org/project/sigstickers)\n\n<!-- omit in TOC -->\n# SigStickers - Signal Sticker Downloader\n\n<img src="readme-assets/icons/name.png" alt="Project Icon" width="750">\n\nDownload sticker packs from Signal\n\n- [Using](#using)\n\t- [Help](#help)\n- [Formats](#formats)\n- [Documentation](#documentation)\n- [Install With PIP](#install-with-pip)\n- [Language information](#language-information)\n\t- [Built for](#built-for)\n- [Install Python on Windows](#install-python-on-windows)\n\t- [Chocolatey](#chocolatey)\n\t- [Download](#download)\n- [Install Python on Linux](#install-python-on-linux)\n\t- [Apt](#apt)\n- [How to run](#how-to-run)\n\t- [With VSCode](#with-vscode)\n\t- [From the Terminal](#from-the-terminal)\n- [Download Project](#download-project)\n\t- [Clone](#clone)\n\t\t- [Using The Command Line](#using-the-command-line)\n\t\t- [Using GitHub Desktop](#using-github-desktop)\n\t- [Download Zip File](#download-zip-file)\n- [Community Files](#community-files)\n\t- [Licence](#licence)\n\t- [Changelog](#changelog)\n\t- [Code of Conduct](#code-of-conduct)\n\t- [Contributing](#contributing)\n\t- [Security](#security)\n\t- [Support](#support)\n\t- [Rationale](#rationale)\n\n## Using\n\n- Get the URL of the Signal sticker pack\n- Run the program `python -m sigstickers`\n- Enter the URL of the sticker pack\n- Get the output in the `downloads` folder.\n\n### Help\n\n```sh\nusage: Welcome to SigSticker, providing all of your sticker needs [-h] [-p PACK [PACK ...]]\n\noptional arguments:\n  -h, --help            show this help message and exit\n  -p PACK [PACK ...], --pack PACK [PACK ...]\n                        Pass in a pack url inline\n```\n\n## Formats\n\n|Format|Static|Animated|\n|------|------|--------|\n|.gif  |✔$    |✔$      |\n|.png  |✔     |+       |\n|.webp |✔     |✔       |\n\n```txt\n+ The first frame of an animated image is saved as gif\n$ Some images saved as gif do not render as expected\n```\n\n## Documentation\nSee the [Docs](/DOCS/) for more information.\n\n## Install With PIP\n\n```python\npip install sigstickers\n```\n\nHead to https://pypi.org/project/sigstickers/ for more info\n\n## Language information\n### Built for\nThis program has been written for Python 3 and has been tested with\nPython version 3.9.0 <https://www.python.org/downloads/release/python-380/>.\n\n## Install Python on Windows\n### Chocolatey\n\n```powershell\nchoco install python\n```\n\n### Download\nTo install Python, go to <https://www.python.org/> and download the latest\nversion.\n\n## Install Python on Linux\n### Apt\n\n```bash\nsudo apt install python3.9\n```\n\n## How to run\n### With VSCode\n\n1. Open the .py file in vscode\n2. Ensure a python 3.9 interpreter is selected (Ctrl+Shift+P > Python:Select\nInterpreter > Python 3.9)\n3. Run by pressing Ctrl+F5 (if you are prompted to install any modules, accept)\n\n### From the Terminal\n\n```bash\n./[file].py\n```\n\n## Download Project\n### Clone\n#### Using The Command Line\n\n1. Press the Clone or download button in the top right\n2. Copy the URL (link)\n3. Open the command line and change directory to where you wish to\nclone to\n4. Type \'git clone\' followed by URL in step 2\n\n\t```bash\n\tgit clone https://github.com/FHPythonUtils/SigStickers\n\t```\n\nMore information can be found at\n<https://help.github.com/en/articles/cloning-a-repository>\n\n#### Using GitHub Desktop\n\n1. Press the Clone or download button in the top right\n2. Click open in desktop\n3. Choose the path for where you want and click Clone\n\nMore information can be found at\n<https://help.github.com/en/desktop/contributing-to-projects/cloning-a-repository-from-github-to-github-desktop>\n\n### Download Zip File\n\n1. Download this GitHub repository\n2. Extract the zip archive\n3. Copy/ move to the desired location\n\n## Community Files\n### Licence\nMIT License\nCopyright (c) FredHappyface\n(See the [LICENSE](/LICENSE.md) for more information.)\n\n### Changelog\nSee the [Changelog](/CHANGELOG.md) for more information.\n\n### Code of Conduct\nOnline communities include people from many backgrounds. The *Project*\ncontributors are committed to providing a friendly, safe and welcoming\nenvironment for all. Please see the\n[Code of Conduct](https://github.com/FHPythonUtils/.github/blob/master/CODE_OF_CONDUCT.md)\n for more information.\n\n### Contributing\nContributions are welcome, please see the\n[Contributing Guidelines](https://github.com/FHPythonUtils/.github/blob/master/CONTRIBUTING.md)\nfor more information.\n\n### Security\nThank you for improving the security of the project, please see the\n[Security Policy](https://github.com/FHPythonUtils/.github/blob/master/SECURITY.md)\nfor more information.\n\n### Support\nThank you for using this project, I hope it is of use to you. Please be aware that\nthose involved with the project often do so for fun along with other commitments\n(such as work, family, etc). Please see the\n[Support Policy](https://github.com/FHPythonUtils/.github/blob/master/SUPPORT.md)\nfor more information.\n\n### Rationale\nThe rationale acts as a guide to various processes regarding projects such as\nthe versioning scheme and the programming styles used. Please see the\n[Rationale](https://github.com/FHPythonUtils/.github/blob/master/RATIONALE.md)\nfor more information.\n',
    'author': 'FredHappyface',
    'author_email': None,
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/FHPythonUtils/SigStickers',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
