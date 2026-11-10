import os
from importlib.metadata import version

from toolviper.utils.logger import setup_logger

from . import graph
from .graph import Graph

__version__ = version("dougu")

# Setup default logger instance for module
if not os.getenv("VIPER_LOGGER_NAME"):
    os.environ["VIPER_LOGGER_NAME"] = "dougu"
    setup_logger(
        logger_name="dougu",
        log_to_term=True,
        log_to_file=False,
        log_file="dougu-logfile",
        log_level="INFO",
    )