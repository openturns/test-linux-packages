#!/bin/sh

set -e

for image in ubuntu debian centos fedora opensuse
do
  docker build ${image}
done
