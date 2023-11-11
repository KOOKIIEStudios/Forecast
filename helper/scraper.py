# Copyright 2023 KOOKIIE
#
# This file is part of Forecast.
# Forecast is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Forecast is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Forecast. If not, see <https://www.gnu.org/licenses/>.
#
# Contact via Discord: `sessionkookiie`
import sys
from pathlib import Path

import requests

from utils import constants, logger

log = logger.get_logger(__name__)


def fetch_contents(uri: str) -> requests.Response:
    log.info("Fetching expansion pack information from Bulbapedia")
    try:
        response = requests.get(uri, timeout=5)
        response.raise_for_status()

        # if successful:
        return response
    except requests.exceptions.HTTPError as error:
        log.error("HTTP Error when fetching from Bulbapedia!\n%s", error)
        sys.exit(1)
    except requests.exceptions.ConnectionError:
        log.error("Unable to connect to Bulbapedia!")
        sys.exit(1)
    except requests.exceptions.Timeout:
        log.error("Bulbapedia timed out!")
        sys.exit(1)
    except requests.exceptions.RequestException as error:
        log.error("Unknown error occurred while fetching Bulbapedia!\n%s", error)
        sys.exit(1)


def save_raw_html(html_response: requests.Response, file_path: Path) -> None:
    log.info("Saving expansion pack data to temporary file")
    with open(file_path, "wb") as fd:
        for chunk in html_response.iter_content(chunk_size=128):
            fd.write(chunk)


def preprocess_html(file_path: Path) -> str:
    log.info("Sanitising and pre-processing HTML contents")
    with open(file_path, "r") as fd:
        line = fd.readline()

    if not line:
        log.error("Saved HTML file is empty!")

    new_line = line
    for key, value in constants.SANITISATION_MAP.items():
        new_line = new_line.replace(key, value)
    return new_line


def write_to_file(file_contents: str, file_path: Path) -> None:
    log.info("Saving sanitised data to temporary file")
    if not file_contents:
        log.error("No content to write!")
    with open(file_path, "w") as fd:
        fd.write(file_contents)
