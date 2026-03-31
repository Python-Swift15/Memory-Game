# Memory-Game 🧠

A terminal-based Memory / Simon-style sequence game implemented in Python. The program shows a growing sequence of digits (1–4) and you must repeat the sequence by pressing the matching keys. Difficulty levels control the display speed and the game speeds up as you progress.

## Features

- Classic sequence memory gameplay (show then repeat)
- Five difficulty levels: Easy → God (adjusts sequence display speed)
- Colored on-screen digits using ANSI escape codes
- Simple audio feedback using the system bell
- Terminal-first interface with single-key input support (Unix and Windows)
- Lightweight single-file implementation: `PY3memorygame.py`

## How it works (matching the code)

- The game displays a loading bar and an intro screen.
- Choose a difficulty (1 to 5). Each difficulty maps to a name and a base speed.
- Each round appends a random digit from 1–4 to the sequence.
- The sequence is shown one item at a time (big colored number + short beep).
- The player repeats the sequence by pressing keys 1–4 (single-key input; no Enter required).
- If the player repeats correctly, the level increments and the sequence grows; if not, the game ends and shows the correct sequence.

## Requirements

- Python 3.x
- Works in a terminal / console
- No external libraries required

Notes:
- On Unix-like systems the script uses `termios`/`tty` for raw single-key input; on Windows it falls back to `msvcrt`.
- The script uses `os.system("clear")` to clear the terminal (on Windows you may want to change this to `cls`).

## Installation 

Clone the repository and run the script:

```bash
git clone https://github.com/Python-Swift15/Memory-Game.git
cd Memory-Game
