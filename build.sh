#!/usr/bin/env bash

# For use with WINE

/home/rwardrup/DEV/venv_wine/bin/activate  # Activate the WINE virtual environment
wine c:/Python34/python.exe /home/rwardrup/DEV/pyinstaller/pyinstaller.py /home/rwardrup/DEV/GIS-Helper/assets/gh-debug.spec