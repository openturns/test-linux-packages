FROM mageia:6
WORKDIR /tmp

RUN urpmi.addmedia --distrib --wget 'ftp://ftp.snt.utwente.nl/pub/os/linux/mageia/distrib/$RELEASE/$ARCH'
RUN urpmi --auto-update
RUN urpmi curl

RUN curl http://download.opensuse.org/repositories/science:/openturns/Mageia_6/science:openturns.repo -o /etc/yum.repos.d/obs-openturns.repo
RUN rpm --import http://download.opensuse.org/repositories/science:/openturns/Mageia_6/repodata/repomd.xml.key
RUN dnf makecache
RUN dnf install -y python-openturns

RUN curl -fsSLO https://raw.githubusercontent.com/openturns/openturns/v1.12/python/test/t_features.py && python ./t_features.py
