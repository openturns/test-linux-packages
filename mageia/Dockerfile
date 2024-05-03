FROM mageia:9
WORKDIR /tmp

RUN urpmi.addmedia --distrib --wget 'ftp://ftp.snt.utwente.nl/pub/os/linux/mageia/distrib/$RELEASE/$ARCH'
RUN urpmi --auto-update
RUN urpmi curl

RUN curl  https://download.opensuse.org/repositories/science:/openturns/Mageia_9/science:openturns.repo -o /etc/yum.repos.d/science-openturns.repo
RUN rpm --import https://download.opensuse.org/repositories/science:/openturns/Mageia_9/repodata/repomd.xml.key
RUN dnf makecache
RUN dnf install -y python3-openturns

