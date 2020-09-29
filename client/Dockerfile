FROM ubuntu:latest
ENV PATH="/root/usr/bin:${PATH}"

RUN apt update && \
    apt install -y binutils && \
    apt install xz-utils && \
    apt install -y libedit-dev && \
    apt install -y libssl-dev


ADD http://mirrors.kernel.org/ubuntu/pool/main/m/mysql-8.0/mysql-client-core-8.0_8.0.21-0ubuntu0.20.04.4_amd64.deb /root/

RUN cd /root/ && ar vx mysql-client-core-8.0_8.0.21-0ubuntu0.20.04.4_amd64.deb && \
    tar xvf data.tar.xz

CMD mysql -h ${MYSQL_HOST} -u redes -psome_pass
