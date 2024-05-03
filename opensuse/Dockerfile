FROM opensuse/leap:15.5

RUN curl https://download.opensuse.org/repositories/science:/openturns/15.5/science:openturns.repo -o /etc/zypp/repos.d/science-openturns.repo
RUN rpm --import https://download.opensuse.org/repositories/science:/openturns/15.5/repodata/repomd.xml.key
RUN zypper -n install curl python3-openturns


