#!/bin/bash
set -e

echo "Starting SSH..."
/usr/sbin/sshd

echo "Starting Tor..."
su -s /bin/bash debian-tor -c "tor -f /etc/tor/torrc" &

echo "Starting Nginx..."
exec nginx -g "daemon off;"