__author__ = "Animikh Aich"
__copyright__ = "Copyright 2020, Animikh Aich"
__credits__ = ["Animikh Aich"]
__license__ = "MIT"
__version__ = "1.0.0"
__maintainer__ = "Animikh Aich"
__email__ = "animikhaich@gmail.com"

import logging

FORMAT = "%(asctime)s: %(levelname)s: %(message)s"
logging.basicConfig(filename="logs.log", level=logging.INFO, format=FORMAT)
STDERRLOGGER = logging.StreamHandler()
STDERRLOGGER.setFormatter(logging.Formatter(FORMAT))
logging.getLogger().addHandler(STDERRLOGGER)