#!/bin/sh

set -e

for image in ubuntu debian centos fedora opensuse
do
  docker build ${image} -t ${image}
  docker run ${image} sh -c "curl -fsSLO https://raw.githubusercontent.com/openturns/openturns/v1.13/python/test/t_features.py && python ./t_features.py"
done

