# Stockholm

![](https://img.shields.io/badge/code-python-purple)
![](https://img.shields.io/badge/School-42-black)

**Stockholm** is an educational Python project that demonstrates file encryption and decryption using a command-line interface. It uses Fernet to encrypt files and RSA to protect the generated file-encryption key.

> ❗️❗️ **Warning: for educational purposes only. Run this project exclusively in an isolated test directory with disposable files.**

## Features

- Recursively find supported files in the `$HOME/infection` directory
- Encrypt  files
- Store encrypted files with the `.ft` extension
- Protect the generated encryption key with an RSA public key
- Restore encrypted files using the matching RSA private key
- Silent execution mode
- Colored command-line logging

## Requirements

- Linux
- Python 3.12 or newer
- [uv](https://docs.astral.sh/uv/getting-started/installation/)
- Filesystem support for extended attributes
- openssl

## Installation

Install `uv` by following the [official installation guide](https://docs.astral.sh/uv/getting-started/installation/).
Then, from this directory:

## Preparing 

The `prepare` target installs the Python dependencies with `uv`, creates `$HOME/infection`, generates the RSA keys in `secret/`, and copies the public key to `src/stockholm/utils/stockholm.pub`.

```bash
make prepare
```

The private key must be kept safe because it is required for decryption. Generated keys are local files and must not be committed.


## Usage

### Encrypt supported test files

```bash
uv run stockholm
```

This processes  files below `$HOME/infection` and creates encrypted files with the `.ft` extension.

### Decrypt previously encrypted files

```bash
uv run stockholm --reverse secret/stockholm.key
```

Use the RSA private key that matches the configured public key.

### Run silently

```bash
uv run stockholm --silent
```

The `--silent` option suppresses terminal output while keeping the operation active.

### Show help or the installed version

```bash
uv run stockholm --help
uv run stockholm --version
```

## Options

```text
usage:
	stockholm [-h] [-r KEY] [-s] [-v]

options:
	-h, --help          show this help message and exit
	-r KEY, --reverse KEY
						Reverse the operation using the specified key
	-s, --silent        Do not produce any output
	-v, --version       show program's version number and exit
```

## Safety

Do not run this program against system files, personal data, shared folders, or files belonging to other users. Always work in a disposable directory and keep backups of any test data.

## Contributing

Contributions, bug reports, and feature requests are welcome. Open an issue or submit a pull request with a clear description of the proposed change.
