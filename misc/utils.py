__author__ = "Animikh Aich"
__copyright__ = "Copyright 2020, Animikh Aich"
__credits__ = ["Animikh Aich"]
__license__ = "MIT"
__version__ = "1.0.0"
__maintainer__ = "Animikh Aich"
__email__ = "animikhaich@gmail.com"

from misc import logging
import requests, os, json


def download_file(source_url, filename=None, folder=None):
    # Validity Checks
    if filename is None:
        filename = os.path.basename(source_url)

    if len(filename) < 1:
        logging.error(f"URL does not contain filename. No filename given")
        return (
            False,
            f"URL does not contain filename. No filename given. Please provide a filename",
            None,
        )

    if folder is None:
        filepath = filename
    else:
        if not os.path.exists(folder):
            os.makedirs(folder)

        filepath = os.path.join(folder, filename)

    try:
        # Download the file
        req = requests.get(source_url, allow_redirects=True)
    except Exception as e:
        logging.error(f"Failed to get the file due to error: {e}")
        return False, f"Failed to get the file due to error: {e}", None

    # Write the file to disk
    with open(filepath, "wb") as f:
        f.write(req.content)

    return True, f"File Downloaded in location {filepath}", filepath


def load_config(config_path):
    config = {}
    try:
        with open("config.json") as f:
            config = json.load(f)
        logging.info(f"Config Loaded. JSON Contents: \n{json.dumps(config, indent=4)}")
    except Exception as e:
        logging.error(f"Failed to Load Config, using default config Params. Error: {e}")

    return config
