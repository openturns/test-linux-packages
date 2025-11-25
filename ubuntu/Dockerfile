FROM ubuntu:noble
ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get -y update && apt-get -y install curl gnupg apt-transport-https ca-certificates

RUN curl -fsSL https://openturns.github.io/apt/public.key | gpg --dearmor --yes --output /usr/share/keyrings/openturns-keyring.gpg
RUN echo "deb [signed-by=/usr/share/keyrings/openturns-keyring.gpg] https://openturns.github.io/apt/ubuntu noble main" | tee /etc/apt/sources.list.d/openturns.list
RUN apt-get -y update && apt-get -y install python3-openturns libopenturns-dev
