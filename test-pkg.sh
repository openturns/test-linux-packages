#!/bin/sh

set -e

for image in ubuntu debian fedora opensuse mageia
do
  docker build ${image}
done

