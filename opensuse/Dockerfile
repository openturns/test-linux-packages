FROM opensuse/leap:15.2


RUN zypper -n ar -cfp 90 http://download.opensuse.org/repositories/science:/openturns/openSUSE_Leap_15.2/science:openturns.repo
RUN zypper -n ar -cfp 90 http://download.opensuse.org/repositories/science/openSUSE_Leap_15.2/science.repo
RUN zypper --gpg-auto-import-keys ref

RUN zypper -n install curl python3-openturns


