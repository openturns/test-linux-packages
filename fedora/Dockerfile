FROM fedora:42

RUN curl -sSL https://download.opensuse.org/repositories/science:/openturns/Fedora_42/science:openturns.repo -o /etc/yum.repos.d/science-openturns.repo
RUN rpm --import https://download.opensuse.org/repositories/science:/openturns/Fedora_42/repodata/repomd.xml.key
RUN yum install -y python3-openturns

