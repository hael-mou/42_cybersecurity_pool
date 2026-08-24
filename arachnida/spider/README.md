# Spider
![](https://img.shields.io/badge/code-python-purple)
![](https://img.shields.io/badge/School-42-black)

Spider is a command-line web scraping tool designed to collect resources from the same domain and download the images found on those pages.

> ❗️❗️ Warning: just for Education purposes only !!

## Requirements

- Python 3.12 or newer
- [uv](https://docs.astral.sh/uv/getting-started/installation/)
- Chromium installed for Playwright

## Installation

Install `uv` by following the [official installation guide](https://docs.astral.sh/uv/getting-started/installation/).
Then, from this directory:

```bash
uv sync
uv run playwright install --with-deps
```

## Usage

Scrape images from one page:

```bash
uv run spider https://example.com
```

Scrape the same domain recursively to depth 2 and save images to `downloads`:

```bash
uv run spider --recursive --level 2 --path downloads https://example.com
```

Show help or the installed version:

```bash
uv run spider --help
uv run spider --version
```

## Options

```bash
███████ ██████  ██ ██████  ███████ ██████
██      ██   ██ ██ ██   ██ ██      ██   ██
███████ ██████  ██ ██   ██ █████   ██████
     ██ ██      ██ ██   ██ ██      ██   ██
███████ ██      ██ ██████  ███████ ██   ██
===================================================

usage:
    spider [-h] [-r] [-l LEVEL] [-p PATH] [-v] url

positional arguments:
    url                 URL of the website to crawl

options:
    -h, --help          show this help message and exit
    -r, --recursive     Enable recursive crawling of the website (same domain only).
    -l, --level LEVEL   Maximum depth level for recursive crawling (default: 5).Only works only with -r.
    -p, --path PATH     Path to save the results (default: ./data).
    -v  --version       show program's version number and exit
```

## Contributing

Contributions, bug reports and feature requests are welcome. Open a GitHub issue or submit a pull request targeting the relevant tool directory.
