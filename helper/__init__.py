# Copyright 2023 KOOKIIE
#
# This file is part of Forecast.
# Weather Ball is free software: you can redistribute it and/or modify
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
# along with Weather Ball. If not, see <https://www.gnu.org/licenses/>.
#
# Contact via Discord: `sessionkookiie`
"""Holds the Forecast class"""
import tempfile
from datetime import datetime, timezone
from pathlib import Path

import pandas as pd

from . import parser
from . import scraper
from utils import constants, logger


class Forecast:
    """Performs scraping, parsing, and file IO

    Typical usage example:

        forecast = Forecast()
        forecast.generate_dart_file()
    """
    def __init__(self) -> None:
        self.log = logger.get_logger(__name__)
        self.response = scraper.fetch_contents(constants.REQUEST_URL)

    @staticmethod
    def generate_timestamp() -> str:
        return datetime.now(timezone.utc).strftime("%A, %d. %B %Y %I:%M%p")

    def perform_initial_processing(self) -> list[pd.DataFrame]:
        # consolidate IO actions for temp folder
        self.log.info("Creating temporary directory in output folder for pre-processing")
        with tempfile.TemporaryDirectory(prefix="temp_", dir=constants.OUTPUT_FOLDER) as temp_folder_name:
            temp_folder = constants.OUTPUT_FOLDER / temp_folder_name
            raw_html_file = temp_folder / constants.RAW_HTML
            sanitised_html_file = temp_folder / constants.PREPROCESSED_HTML

            # download and pre-process
            scraper.save_raw_html(self.response, raw_html_file)
            buffer = scraper.preprocess_html(raw_html_file)
            scraper.write_to_file(buffer, sanitised_html_file)

            # read as table
            return parser.extract_relevant_tables(sanitised_html_file)

    def format_as_lines(self, table: pd.DataFrame) -> list[str]:
        self.log.info("Generating Dart file contents")
        if table is None:
            print("INVALID TABLE")

        string_buffer = [
            f"// Generated using Forecast on {self.generate_timestamp()} UTC\n",
            "//     See: https://github.com/KOOKIIEStudios/Forecast\n",
            "const Set<String> setAbbreviations = {\n",
        ]

        for row in table.itertuples(index=False):
            string_buffer.append(f'  "{getattr(row, constants.ColumnNames.SET)}",')
            string_buffer.append(f'  // {getattr(row, constants.ColumnNames.NAME)}\n')

        string_buffer.append("};\n")
        return string_buffer

    def write_lines(self, lines: list[str], file_path: Path) -> None:
        self.log.info("Writing out to file: %s", file_path.name)
        if not lines:
            self.log.error("No content to write!")
        with open(file_path, "w") as fd:
            fd.writelines(lines)
        self.log.info("File saved in: %s", file_path.parent)

    def generate_dart_file(self) -> None:
        name_and_set_mapping = parser.manipulate_as_tables(self.perform_initial_processing())
        lines = self.format_as_lines(name_and_set_mapping)
        self.write_lines(lines, constants.OUTPUT_FILE)
