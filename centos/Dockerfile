FROM centos:7

RUN curl -sSL http://download.opensuse.org/repositories/science:/openturns/CentOS_7/science:openturns.repo -o /etc/yum.repos.d/obs-openturns.repo
RUN rpm --import http://download.opensuse.org/repositories/science:/openturns/CentOS_7/repodata/repomd.xml.key
RUN yum install -y python-openturns

