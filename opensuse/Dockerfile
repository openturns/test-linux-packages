FROM opensuse/leap:16.0

RUN curl https://download.opensuse.org/repositories/science:/openturns/16.0/science:openturns.repo -o /etc/zypp/repos.d/science-openturns.repo
RUN rpm --import https://download.opensuse.org/repositories/science:/openturns/16.0/repodata/repomd.xml.key
RUN zypper -n install curl python3-openturns


