#!/usr/bin/env python3
import os
import sys
from pathlib import Path

COMMANDS = [
    'python -m pip install -U pip setuptools wheel pip-tools',
    'pip install -e .',
]

os.chdir(Path(__file__).parent)

if not os.getenv('VIRTUAL_ENV'):
    if input('Should I create a virtual environment `.venv`? [Y/n]') == 'n':
        print(
            'Please create and activate a virtual environment of your choice.',
        )
        sys.exit()
    os.system('python -m venv .venv --prompt playwright_example')

venv_path = Path(os.getenv('VIRTUAL_ENV', '.venv'))
venv_bin_folder = 'Scripts' if os.name == 'nt' else 'bin'
for cmd in COMMANDS:
    os.system(venv_path.joinpath(venv_bin_folder, cmd))
activate = (
    f'{venv_path / F"{venv_bin_folder}/activate.bat"}'
    if os.name == 'nt'
    else f'source {venv_path / f"{venv_bin_folder}/activate"}'
)

print('Your development environment is set up.')  # noqa: T201
if not os.getenv('VIRTUAL_ENV'):
    print(
        '\n\n\n\n********* Activate your new virtual environment by running:',
        activate,
        '**********',
    )
