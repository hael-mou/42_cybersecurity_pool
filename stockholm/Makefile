SHELL := /bin/sh

KEY_DIR := secret
PRIVATE_KEY := $(KEY_DIR)/stockholm.key
PUBLIC_KEY := $(KEY_DIR)/stockholm.pub
PROJECT_PUBLIC_KEY := src/stockholm/utils/stockholm.pub
INFECTION_DIR := $(HOME)/infection

.PHONY: prepare sync keys infection help


prepare: sync keys infection
	@echo "Stockholm preparation complete."

sync:
	@uv sync

keys:
	@mkdir -p "$(KEY_DIR)"
	@if [ ! -f "$(PRIVATE_KEY)" ]; then \
		echo "Generating private key..."; \
		openssl genrsa -out "$(PRIVATE_KEY)" 2048; \
	fi
	@if [ ! -f "$(PUBLIC_KEY)" ] || [ "$(PRIVATE_KEY)" -nt "$(PUBLIC_KEY)" ]; then \
		echo "Generating public key..."; \
		openssl rsa -in "$(PRIVATE_KEY)" -pubout -out "$(PUBLIC_KEY)"; \
	fi
	@chmod 600 "$(PRIVATE_KEY)"
	@cp "$(PUBLIC_KEY)" "$(PROJECT_PUBLIC_KEY)"

infection:
	@mkdir -p "$(INFECTION_DIR)"

help:
	@uv run stockholm --help

