FROM opensuse/leap:15.6

RUN curl https://download.opensuse.org/repositories/science:/openturns/15.6/science:openturns.repo -o /etc/zypp/repos.d/science-openturns.repo
RUN rpm --import https://download.opensuse.org/repositories/science:/openturns/15.6/repodata/repomd.xml.key
RUN zypper -n install curl python3-openturns


