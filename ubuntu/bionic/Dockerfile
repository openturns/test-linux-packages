
FROM ubuntu:bionic
MAINTAINER jschueller

ENV MAKEFLAGS "-j8"
ENV TERM dumb
WORKDIR /tmp

# mimic circleci image
RUN apt-get -y update
RUN echo "Europe/Dublin" > /etc/timezone
RUN apt-get install tzdata
RUN dpkg-reconfigure -f noninteractive tzdata
RUN apt-get -y install curl gnupg

RUN curl -fsSL http://debian.openturns.org/openturns.org-repo.key | apt-key add -
RUN echo deb http://ubuntu.openturns.org bionic main | tee /etc/apt/sources.list.d/openturns.list
RUN apt-get -y  update
RUN apt-get -y install python3-openturns python-openturns libopenturns-dev

RUN useradd -m -d /home/ubuntu -u 1000 -U -G users,tty -s /bin/bash ubuntu
RUN echo 'ubuntu ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers
USER ubuntu

RUN curl -fsSLO https://raw.githubusercontent.com/openturns/openturns/v1.12/python/test/t_features.py && /usr/bin/python3 ./t_features.py && /usr/bin/python2 ./t_features.py
