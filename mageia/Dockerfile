FROM mageia:7
WORKDIR /tmp

RUN urpmi.addmedia --distrib --wget 'ftp://ftp.snt.utwente.nl/pub/os/linux/mageia/distrib/$RELEASE/$ARCH'
RUN urpmi --auto-update
RUN urpmi curl

RUN curl http://download.opensuse.org/repositories/science:/openturns/Mageia_7/science:openturns.repo -o /etc/yum.repos.d/obs-openturns.repo
RUN rpm --import http://download.opensuse.org/repositories/science:/openturns/Mageia_7/repodata/repomd.xml.key
RUN dnf makecache
RUN dnf install -y python3-openturns

