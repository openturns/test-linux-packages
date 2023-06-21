FROM debian:bookworm
ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get -y update && apt-get -y install curl gnupg apt-transport-https ca-certificates

RUN curl -fsSL https://openturns.github.io/apt/public.key | apt-key add -
RUN echo deb https://openturns.github.io/apt/debian bookworm main | tee /etc/apt/sources.list.d/openturns.list
RUN apt-get -y update && apt-get -y install python3-openturns libopenturns-dev
