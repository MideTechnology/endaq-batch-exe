# `endaq.batch`-exe

This repo provides a command-line interfaced Windows-executable-file version of the `endaq.batch` module (provided by [the `endaq` package](https://github.com/MideTechnology/endaq-python)).

# Building the .exe 

First, ensure you have Python 3.7-3.9 installed on your system. (The .exe *may* work on newer Python versions like 3.10, but will *NOT* work on older versions like 3.6 or earlier.) The instructions below assume your version of Python is accessible via `python` in the cmd terminal.

On a Windows machine, in the cmd terminal:
- fetch the repo via `git clone ...`, or simply download the repo folder:
	```
	$ git clone https://github.com/MideTechnology/endaq-batch-exe.git
	```
- navigate to the repo folder:
	```
	$ cd endaq-batch-exe
	```
- make a `venv` to store the requisite Python dependencies, and activate the `venv`:
	```
	$ python -m venv venv
	$ venv\Scripts\activate
	```
- install the requisite Python dependencies (while in the `venv`):
	```
	$ python -m pip install -U pip setuptools
	$ python -m pip install -r requirements.txt
	```
- build the .exe with PyInstaller:
	```
	$ python -m PyInstaller main.spec --noconfirm
	```
