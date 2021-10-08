__author__ = "Julián Arenas-Guerrero"
__credits__ = ["Julián Arenas-Guerrero"]

__license__ = "Apache-2.0"
__maintainer__ = "Julián Arenas-Guerrero"
__email__ = "arenas.guerrero.julian@outlook.com"


import argparse
import os

from configparser import ExtendedInterpolation

from .utils import configure_logger
from .constants import __copyright__
from .config import Config
from ._version import __version__


def _existing_file_path(file_path):
    """
    Checks whether a file exists.
    """

    file_path = str(file_path).strip()
    if not os.path.isfile(file_path):
        raise argparse.ArgumentTypeError("%r is not a valid file path." % file_path)

    return file_path


def _parse_arguments():
    """
    Parses command line arguments.
    """

    parser = argparse.ArgumentParser(
        description='Generate Knowledge Graphs from Heterogeneous Data Sources.',
        epilog=__copyright__,
        allow_abbrev=False,
        prog='python3 -m morph_kgc',
        argument_default=argparse.SUPPRESS
    )

    parser.add_argument('config', type=_existing_file_path, help='path to the configuration file')
    parser.add_argument('-v', '--version', action='version', version='Morph-KGC ' + __version__ + ' | ' + __copyright__)

    return parser.parse_args()


def parse_config():
    """
    Parses command line arguments and the config file. Logger is configured.
    """

    args = _parse_arguments()

    config = Config(interpolation=ExtendedInterpolation())
    config.read(args.config)

    config.complete_configuration_with_defaults()

    config.validate_configuration_section()
    config.validate_data_source_sections()

    configure_logger(config.get_logging_level(), config.get_logging_file())
    config.log_config_info()

    return config
