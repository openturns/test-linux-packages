#!/bin/sh

set -e

for image in mageia centos fedora opensuse ubuntu debian
do
  docker build ${image} -t ${image}
  docker run ${image} sh -c "curl -fsSLO https://raw.githubusercontent.com/openturns/openturns/v1.24rc1/python/test/t_PlatformInfo_std.py && python3 ./t_PlatformInfo_std.py"
done
