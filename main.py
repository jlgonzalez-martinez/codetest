""" Application main module """
import logging

from argparse import ArgumentParser

from dynaconf.loaders import settings_loader

from config import settings
from presentation.app import start


def _arg_parser() -> dict:
    """
    Create an argument parser with the config option and parses the arguments

    Returns: parsed args

    """
    parser = ArgumentParser(description="Fever codetest")
    parser.add_argument("-c", "--config", type=str, required=True,
                        help='Fever codetest config file path')
    return vars(parser.parse_args())


def main(config_file_path: str):
    """
    Start the application, init logging, configuration and data model
    Args:
        config_file_path: Config file

    """
    settings_loader(settings, filename=config_file_path, silent=False)
    logging.basicConfig(level=logging.DEBUG)
    start()


if __name__ == '__main__':
    arg_vars = _arg_parser()
    main(arg_vars['config'])
