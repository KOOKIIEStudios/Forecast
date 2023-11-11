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
from pathlib import Path

import pandas as pd

from utils import constants, logger

log = logger.get_logger(__name__)


def extract_relevant_tables(file_path: Path) -> list[pd.DataFrame]:
    log.info("Parsing HTML into a list of Pandas Dataframes")
    tables = pd.read_html(file_path)
    return [df for df in tables if constants.ColumnNames.SET in df.columns]


def extract_relevant_columns(list_of_tables: list[pd.DataFrame]) -> list[pd.DataFrame]:
    log.info("Dropping undesired columns from dataframes")
    return [df[[constants.ColumnNames.NAME, constants.ColumnNames.SET]] for df in list_of_tables]


def post_process_table(table: pd.DataFrame) -> pd.DataFrame:
    log.info("Dropping undesired rows from dataframes")
    return table[table[constants.ColumnNames.SET] != constants.FILTER]


def manipulate_as_tables(list_of_tables: list[pd.DataFrame]) -> pd.DataFrame:
    log.info("Merging dataframes into single dataframes")
    merged_table = pd.concat(extract_relevant_columns(list_of_tables), ignore_index=True)
    return post_process_table(merged_table)
