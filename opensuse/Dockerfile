FROM opensuse/leap:15.1


RUN ls /etc/

RUN zypper -n ar -cfp 90 http://download.opensuse.org/repositories/science:/openturns/openSUSE_Leap_15.1/science:openturns.repo
RUN zypper -n ar -cfp 90 http://download.opensuse.org/repositories/science/openSUSE_Leap_15.1/science.repo

# RUN curl http://download.opensuse.org/repositories/science:/openturns/openSUSE_Leap_15.0/science:openturns.repo -o /etc/yum.repos.d/obs-openturns.repo
# RUN rpm --import http://download.opensuse.org/repositories/science:/openturns/openSUSE_Leap_15.0/repodata/repomd.xml.key
# RUN dnf makecache
# RUN zypper -n refresh --gpg-auto-import-keys
 RUN zypper --gpg-auto-import-keys ref
RUN zypper -n install python-openturns

RUN curl -fsSLO https://raw.githubusercontent.com/openturns/openturns/v1.12/python/test/t_features.py && python ./t_features.py

