import logging

FORMAT = "%(asctime)s: %(levelname)s: %(message)s"
logging.basicConfig(filename="logs.log", level=logging.INFO, format=FORMAT)
STDERRLOGGER = logging.StreamHandler()
STDERRLOGGER.setFormatter(logging.Formatter(FORMAT))
logging.getLogger().addHandler(STDERRLOGGER)