FROM opensuse/leap:15.1


RUN zypper -n ar -cfp 90 http://download.opensuse.org/repositories/science:/openturns/openSUSE_Leap_15.1/science:openturns.repo
RUN zypper -n ar -cfp 90 http://download.opensuse.org/repositories/science/openSUSE_Leap_15.1/science.repo
RUN zypper --gpg-auto-import-keys ref

RUN zypper -n install curl python-openturns

RUN curl -fsSLO https://raw.githubusercontent.com/openturns/openturns/v1.13rc1/python/test/t_features.py && python ./t_features.py

