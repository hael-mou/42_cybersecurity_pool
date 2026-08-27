# FT_OTP
![](https://img.shields.io/badge/code-python-purple)
![](https://img.shields.io/badge/School-42-black)

ft_otp is a command-line one-time password (OTP) generator. It can generate an encrypted key from a hexadecimal key file, create a QR code for OTP applications, and generate a 6-digit time-based OTP.

## Requirements

- Python 3.12 or newer
- [uv](https://docs.astral.sh/uv/getting-started/installation/)
- An hexadecimal key file containing the secret key

## Installation

Install `uv` by following the [official installation guide](https://docs.astral.sh/uv/getting-started/installation/).
Then, from this directory:

```bash
uv sync
```

## Usage
### 1 - Generate an encrypted key
Generate an encrypted key from a hexadecimal key file:(-g / --generate)

```bash
uv run ft_otp -g ./hex_key.txt
```
You can specify a different output file:
```bash
uv run ft_otp --g ./hex_key.txt --key-output ./my_key.key
```
By default, the encrypted key is saved to `./ft_otp.key.`

### 2 - Generate a QR code
Generate a QR code from an encrypted key:
```bash
uv run ft_otp --qrcode
```


You can specify the key file and customize the OTP account information:
```bash
uv run ft_otp --qrcode ./ft_otp.key \
    --issuer "MyService" \
    --account "user@example.com"
```

To specify a different QR code output:
```bash
uv run ft_otp --qrcode ./ft_otp.key --qr-output ./otp.png

```
By default, the command reads `./ft_otp.key` and `./ft_otp.png`

### 3 - Generate an OTP
Generate a 6-digit OTP from the encrypted key:
By default, the key is read from:

The generated OTP uses:
- 6 digits
- 30-second time steps

For a custom key file:
```bash
uv run ft_otp --key ./my_key.key

```

### 4 - Show help and version
```bash
uv run ft_otp --help
uv run ft_otp --version
```

## Options
```bash
usage:
    ft_otp [-h] [-g [HEX_KEY]] [--key-output KEY_FILE]
           [-q [KEY_FILE]] [--issuer NAME] [--account ACCOUNT]
           [--qr-output IMAGE] [-k [KEY_FILE]] [-v]

A one-time password (OTP) generator

options:
    -h, --help
        show this help message

    -g, --generate [HEX_KEY]
        Generate an encrypted key from a hex key file.
        Default: ./hex_key.txt

    --key-output KEY_FILE
        Output encrypted key file.
        Default: ./ft_otp.key

    -q, --qrcode [KEY_FILE]
        Generate a QR code from a key file.
        Default: ./ft_otp.key

    --issuer NAME
        Service or application name.
        Default: ft_otp

    --account ACCOUNT
        Account name.
        Default: user

    --qr-output IMAGE
        Output QR code image.
        Default: ./ft_otp.png

    -k, --key [KEY_FILE]
        Generate a 6-digit OTP from a key file.
        Default: ./ft_otp.key

    -v, --version
        show program version number
```

## Contributing
Contributions, bug reports and feature requests are welcome. Open a GitHub issue or submit a pull request targeting the relevant tool directory.
