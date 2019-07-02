
FROM ubuntu:bionic

RUN apt-get -y update
RUN echo "Europe/Dublin" > /etc/timezone
RUN apt-get install tzdata
RUN dpkg-reconfigure -f noninteractive tzdata
RUN apt-get -y install curl gnupg

RUN curl -fsSL http://debian.openturns.org/openturns.org-repo.key | apt-key add -
RUN echo deb http://ubuntu.openturns.org bionic main | tee /etc/apt/sources.list.d/openturns.list
RUN apt-get -y  update
RUN apt-get -y install python3-openturns python-openturns libopenturns-dev

