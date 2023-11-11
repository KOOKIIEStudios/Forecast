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
from enum import StrEnum
from pathlib import Path

REQUEST_URL = "https://bulbapedia.bulbagarden.net/w/api.php?action=parse&format=json&page=List_of_Pok%C3%A9mon_Trading_Card_Game_expansions"
RAW_HTML = "download.txt"
PREPROCESSED_HTML = "sanitised.txt"

OUTPUT_FOLDER = Path.cwd() / "out"
OUTPUT_FILE = OUTPUT_FOLDER / "set_abbreviations.dart"


class ColumnNames(StrEnum):
    NAME = "full_name"
    SET = "set_abb"


SANITISATION_MAP = {
    'colspan=\\"2\\"': "colspan=2",
    "\\n": "",
    "Name of Expansion": ColumnNames.NAME,
    "Set abb.": ColumnNames.SET,
}
FILTER = "\\u2014"
