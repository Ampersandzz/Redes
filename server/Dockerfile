FROM ubuntu:latest
ENV PATH="/root/server/bin:${PATH}"
ENV TZ=America/Santiago

COPY init.sh /var/tmp/init.sh

RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

RUN apt update && \
    apt install -y binutils && \
    apt install -y build-essential && \
    apt install libssl-dev && \
    apt install -y libncurses5-dev && \
    apt install -y pkg-config && \
    apt install -y bison && \
    apt install -y cmake 

EXPOSE 3306

ADD https://github.com/mysql/mysql-server/tarball/8.0 /root/
WORKDIR /root/
RUN tar xvf 8.0 && mkdir server
RUN cd server/ && cmake ../mysql-mysql-server-f8cdce8/ -DDOWNLOAD_BOOST=1 -DWITH_BOOST=/usr/local/bin && \
    make && \
    mysqld --initialize-insecure && \
    mysqld --daemonize -u root

RUN chmod 755 /var/tmp/init.sh && \
    cd /var/tmp/ && \
    ./init.sh

RUN mysql -h localhost -u root < /var/tmp/mysql-user.sql && \
    pids=$(pgrep mysqld) && \
    kill $pids && \
    mysqld --daemonize --ssl=0 -u root
