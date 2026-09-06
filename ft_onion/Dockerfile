
FROM    debian:bookworm-slim

# ==== Dependency : =============================
RUN     apt-get update &&\
        apt-get install -y nginx tor openssh-server &&\ 
        rm -rf /var/lib/apt/lists/*

RUN     useradd -m -s /bin/bash hael-mou &&\
        passwd -d hael-mou &&\
        passwd -u hael-mou

# ==== Configs : ================================
COPY    ./config/nginx.conf /etc/nginx/nginx.conf
COPY    ./config/torrc /etc/tor/torrc
COPY    ./ssh/id_ed25519.pub /home/hael-mou/.ssh/authorized_keys
COPY    ./config/sshd_config /etc/ssh/sshd_config
COPY    ./web/index.html /var/www/html

# ==== Setup : ==================================
RUN     mkdir -p /run/sshd && \
        chown -R hael-mou:hael-mou /home/hael-mou/.ssh && \
        chmod 700 /home/hael-mou/.ssh /run/sshd && \
        chmod 600 /home/hael-mou/.ssh/authorized_keys /run/sshd

RUN     mkdir -p /var/lib/tor/hidden_service && \
        chown -R debian-tor:debian-tor /var/lib/tor && \
        chmod 700 /var/lib/tor/hidden_service

# ==== Expose : =================================
EXPOSE  4242
EXPOSE  80

# ==== start : ==================================
COPY    ./scripts/start.sh /start.sh
RUN     chmod +x /start.sh
CMD     [ "/start.sh" ]
