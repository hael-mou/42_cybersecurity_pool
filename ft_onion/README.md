# FT_ONION

![](https://img.shields.io/badge/tor_network-purple)
![](https://img.shields.io/badge/School-42-black)

ft_onion is a Docker-based web server project using Nginx, Tor Hidden Service, and OpenSSH. It provides a web page accessible locally and through a `.onion` address, with SSH access secured using public key authentication.

## Requirements

* Docker
* Docker Compose
* Tor Browser
* OpenSSH client

## Project Structure

```text
ft_onion/
├── config/
│   ├── nginx.conf
│   ├── sshd_config
│   └── torrc
├── scripts/
│   └── start.sh
├── web/
│   └── index.html
├── Dockerfile
├── docker-compose.yml
└── README.md
```

SSH keys are generated locally and must not be uploaded to the repository.

## Installation

Generate your SSH key pair:

```bash
mkdir -p ssh
ssh-keygen -t ed25519 -f ./ssh/id_ed25519
```

This creates:

```text
ssh/id_ed25519
ssh/id_ed25519.pub
```

The private key must remain local.

## Usage

### 1 - Build and start the project

```bash
docker compose up -d --build
```

Check the running containers:

```bash
docker compose ps
```

### 2 - Access the website

Locally:

```bash
curl http://localhost
```

Or open:

```text
http://localhost
```

### 3 - Access through Tor

Get the generated `.onion` address:

```bash
docker compose exec ft_onion cat /var/lib/tor/hidden_service/hostname
```

Open the displayed `.onion` address using Tor Browser.

### 4 - Connect through SSH

```bash
ssh -i ./ssh/id_ed25519 hael-mou@localhost -p 4242
```

### 5 - Remove the old SSH host key

If the container is recreated and SSH shows a host key warning:

```bash
ssh-keygen -f ~/.ssh/known_hosts -R '[localhost]:4242'
```

Then connect again:

```bash
ssh -i ./ssh/id_ed25519 hael-mou@localhost -p 4242
```

### 6 - Stop the project

```bash
docker compose down
```

## Ports

| Service | Port | Description |
| ------- | ---: | ----------- |
| Nginx   |   80 | Web server  |
| SSH     | 4242 | SSH access  |

## Contributing

Contributions, bug reports and feature requests are welcome. Open a GitHub issue or submit a pull request.
