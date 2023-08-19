# About MouseWarp

This program moves the mouse cursor to the selected window when AltTab is pressed.

for windows, for myself.

**I have no knowledge of Python !!!!!!!!**

## Setup Dev Environment (Note)

Clone this Repository
`git clone https://github.com/quartz1216/mousewarp.git`

Add python venv
`python -m venv mousewarp`

Activate venv
`.\mousewarp\Scripts\Activate.ps1`

install pyinstaller
`pip install pyinstaller`

install pywin32 
`pip install pywin32`

Build execute file
`pyinstaller .\mousewarp.py -F -w --add-data "icon.ico;." --add-data "icon.ico;." --clean --icon=icon.ico`
