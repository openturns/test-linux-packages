#!/bin/sh

set -e

for image in ubuntu/bionic fedora opensuse mageia
do
  docker build ${image}
done

