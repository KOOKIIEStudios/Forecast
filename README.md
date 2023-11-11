# Forecast
Forecast is a Python script that generates set abbreviations for [CastFORM](https://github.com/BAA-Studios/CastFORM).  
It uses [Bulbapedia's](https://bulbapedia.bulbagarden.net/wiki/Main_Page) [Wikimedia web service API](https://bulbapedia.bulbagarden.net/wiki/Special:ApiSandbox) to fetch all known expansion pack information, which is then parsed and converted into a Dart file as a drop-in replacement in CastFORM.

## A rose by any other name would smell as sweet
Forecast is designed as a part of the toolchain for [CastFORM](https://github.com/BAA-Studios/CastFORM), a Pokémon registration sheet filler.  
Being a form-automation application based around Pokémon TCG, CastFORM is a play on words using the name of one of the playable Pokémon.  
This project inherits its name from Castform's unique ability in the game.

## Tech Stack
Weather Ball is developed using Python 3.12. The entry point is `main.py`.  
If you're using Chocolatey, install Python using the following command: `choco install python`, which should automatically add Python to Path.

Forecast is intended to work with [CastFORM](https://github.com/BAA-Studios/CastFORM) v2.0.0 or newer. This is because it requires changes to the [deck_string_parser](https://github.com/BAA-Studios/CastFORM/blob/main/packages/deck_string_parser/README.md) internal library that is not available as of v1.2.4 (the last version for v1).

## Usage
1. Clone, and `cd` to this repository
2. Set up your virtual environment
    - Linux: run `setup.sh`
    - Windows: run `start.sh`
3. Run `start.bat`/`start.sh` to run the program
    - If unsure, select the virtual environment when prompted
4. Check `./out` for the output file

## Sandbox
The `/sandbox` folder contains a Jupyter notebook for testing purposes. Features and fixes are tested here before being implemented in the code base.

## Disclaimer
**Forecast** is an open-source Python application that fetches formats Pokémon expansion pack information.  
**Forecast** is part of the developer toolchain created for [CastFORM](https://github.com/BAA-Studios/CastFORM).  
**Forecast** is non-monetised, and provided as is. Every reasonable effort has been taken to ensure correctness and reliability of **Forecast**. 
We will not be liable for any special, direct, indirect, or consequential damages or any damages whatsoever resulting from 
loss of use, data or profits, whether in an action if contract, negligence or other tortious action, arising out of or in connection with the use of **Forecast** (in part or in whole).