# d2r-legacymon

A script that looks for the -legacy command line argument when launching [Legacy Guard](https://github.com/txtatech/d2r-legacy-guard) from inside a mod.

It utilizes the `psutil` library to gather information about the parent process and the `subprocess` and `multiprocessing` modules to launch [Legacy Guard](https://github.com/txtatech/d2r-legacy-guard) in a separate process if it finds the -legacy command line argument present in the D2R.exe process that initially launched it.

## Prerequisites

Before running this script, make sure you have the following dependencies installed:

- Python (version 3.6 or later)
- `psutil` library

You can install the `psutil` library using `pip`:

pip install psutil


## Installation

1. Clone this repository or download the script file (`legacymon.py`) to your local machine.

2. Install the required dependencies as mentioned in the Prerequisites section.

3. Place the legacymon.py in the same place that the Legacy Guard start_legacyguard.exe is located. 
Note: When launching Legacy Guard from inside a mod this script will only work if it is located in the same folder as D2R.exe

4. The launcher inside the mod must point to 'legacymon.py' instead of 'start_legacyguard.exe' for this script to work.

## Usage

1. Start the game with the added command line argument -legacy 

2. Launch the script from within the mod/game.

Copyrights
Diablo II and Diablo II: Resurrected are copyrighted by Blizzard Entertainment, Inc. All rights reserved. Diablo II, Diablo II: Resurrected and Blizzard Entertainment are trademarks or registered trademarks of Blizzard Entertainment, Inc. in the U.S. and/or other countries.
All trademarks referenced here are the properties of their respective owners.

This project and its maintainers are not associated with or endorsed by Blizzard Entertainment, Inc.

