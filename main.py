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

from helper import Forecast
from utils import logger

log = logger.get_logger(__name__)


if __name__ == "__main__":
    log.info("----- ForeCAST Set Abbreviation Generator for CastFORM -----")
    forecast = Forecast()
    forecast.generate_dart_file()
    log.info("Completed! Now shutting down...")
    logger.shutdown_logger()
    sys.exit(0)
