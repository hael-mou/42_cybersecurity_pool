#  Scorpion
![](https://img.shields.io/badge/code-python-purple)
![](https://img.shields.io/badge/School-42-black)

**Scorpion** is a lightweight tool for **viewing and modifying image EXIF metadata**. It provides both a command-line interface (CLI) and a web-based GUI for inspecting image metadata and removing EXIF data.

> ❗️❗️ **Warning: just for Education purposes only !!**

## Features

-  View image information and EXIF metadata
-  Remove all EXIF metadata from images
-  Process multiple images from the CLI
-  Web-based GUI for viewing image metadata
-  Simple command-line interface

## Requirements

- Python 3.12 or newer
- [uv](https://docs.astral.sh/uv/getting-started/installation/)

## Installation

Install `uv` by following the [official installation guide](https://docs.astral.sh/uv/getting-started/installation/).

Then, from this directory:

```bash
uv sync
```

## Usage
### - View metadata : 
```bash
uv run scorpion image.jpg
```

### - Delete EXIF metadata : 
```bash
uv run scorpion -d image.jpg
```

### - Start the Web GUI :
```bash
uv run scorpion-gui
```
Scorpion includes a web-based GUI for viewing image metadata through your browser.
The web server listens on port 5000 by default.

### - Show help or the installed version:

```bash
uv run spider --help
uv run spider --version
```

## Options
```bash
███████  ██████  ██████  ██████  ██████  ██  ██████  ███    ██ 
██      ██      ██    ██ ██   ██ ██   ██ ██ ██    ██ ████   ██ 
███████ ██      ██    ██ ██████  ██████  ██ ██    ██ ██ ██  ██ 
     ██ ██      ██    ██ ██   ██ ██      ██ ██    ██ ██  ██ ██ 
███████  ██████  ██████  ██   ██ ██      ██  ██████  ██   ████               
====================================================================

usage:
    scorpion [-h] [--gui] [-d] [-v] [images ...]

positional arguments:
    images              List of image files to process

options:
    -h, --help       show this help message and exit
    --gui            Launch the graphical user interface
    -d, --delete     Delete all EXIF metadata
    -v, --version    show program's version number and exit
```

## Contributing

Contributions, bug reports and feature requests are welcome. Open a GitHub issue or submit a pull request targeting the relevant tool directory.
