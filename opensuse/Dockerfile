FROM opensuse/leap:15.4

RUN curl https://download.opensuse.org/repositories/science:/openturns/15.4/science:openturns.repo -o /etc/zypp/repos.d/science-openturns.repo
RUN rpm --import https://download.opensuse.org/repositories/science:/openturns/15.4/repodata/repomd.xml.key
RUN zypper -n install curl python3-openturns


