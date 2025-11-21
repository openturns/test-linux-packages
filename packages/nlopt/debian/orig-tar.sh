#!/bin/sh -e

# called by uscan with '--upstream-version' <version> <file>
PKG=nlopt
DIR=$PKG-$2
TAR=../${PKG}_$2+dfsg.orig.tar.gz

# clean up the upstream tarball
tar xvf $3
tar -c -z -f $TAR -X debian/orig-tar.exclude $DIR
rm -rf $DIR $3

# move to directory 'tarballs'
if [ -r .svn/deb-layout ]
then
  . .svn/deb-layout
  mv $TAR $origDir
  echo "moved $TAR to $origDir"
fi

exit 0
