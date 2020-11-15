FROM ubuntu:18.10
MAINTAINER nicolas.boettcher@mail.udp.cl

WORKDIR /var

ENV PYTHONIOENCODING=utf8
RUN sed -i 's/archive\.ubuntu\.com/old-releases\.ubuntu\.com/' /etc/apt/sources.list
RUN sed -i '/security\.ubuntu\.com/d' /etc/apt/sources.list

RUN apt-get -yqq update \
    && apt-get clean \
    && apt-get install -yqq build-essential python-dev libnetfilter-queue-dev tcpdump python3-pip

RUN apt install -yqq python3-pip vim git byobu net-tools iptables
RUN cd /tmp;git clone https://github.com/kti/python-netfilterqueue.git \
    && cd /tmp/python-netfilterqueue;python setup.py install

RUN DEBIAN_FRONTEND=noninteractive apt-get install -y tshark wireshark

RUN pip3 install --process-dependency-links polymorph==2.0.2

VOLUME ["/var/develop"]

ENTRYPOINT ["byobu"]
