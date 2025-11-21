FROM ubuntu:focal
RUN apt-get -y update && echo "Europe/Dublin" > /etc/timezone && apt-get install tzdata && dpkg-reconfigure -f noninteractive tzdata && apt-get -y install curl gnupg devscripts g++ cmake liblapacke-dev libblas-dev git debhelper-compat
RUN apt-get -y install wget
RUN cd && pwd && mkdir projects && cd projects && mkdir openturns && cd openturns && git clone https://github.com/openturns/hmat-pkg.git && pwd
ADD package.sh /root/projects/openturns/hmat-pkg
WORKDIR /root/projects/openturns/hmat-pkg
RUN mkdir -p /root/projects/science:openturns/hmat-oss
RUN echo "override_dh_auto_install:" >> debian/rules
RUN echo "\tdh_auto_install" >> debian/rules
RUN echo "\tldd /tmp/hmat-oss-1.8.1/debian/tmp/usr/lib/x86_64-linux-gnu/libhmat.so" >> debian/rules
RUN cat debian/rules
RUN sh ./package.sh
RUN cd /tmp && dpkg -i libhmat-oss3_1.8.1-1_amd64.deb libhmat-oss-dev_1.8.1-1_amd64.deb
RUN ldd /usr/lib/x86_64-linux-gnu/libhmat.so

