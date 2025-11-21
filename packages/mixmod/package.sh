#!/bin/sh

# this script creates source package

set -e

path=.
pkgname=mixmod
obs=~/projects/science:openturns/$pkgname
pkgver=2.1.11
debver=$pkgver
rel=1

usage()
{
  echo "generate source package"
  echo ""
  echo "\t-h --help"
  echo "\t--path=$path"
  echo "\t--pkgname=$pkgname"
  echo "\t--pkgver=$pkgver"
  echo "\t--debver=$debver"
  echo "\t--rel=$rel"
  echo ""
}

while [ "$1" != "" ]; do
  PARAM=`echo $1 | awk -F= '{print $1}'`
  VALUE=`echo $1 | awk -F= '{print $2}'`
  case $PARAM in
    -h | --help)
      usage
      exit
      ;;
    --path)
      path=$VALUE
      ;;
    --pkgname)
      pkgname=$VALUE
      obs=~/projects/science:openturns/$pkgname
      ;;
    --pkgver)
      pkgver=$VALUE
      debver=$pkgver
      ;;
    --debver)
      debver=$VALUE
      ;;
    --rel)
      rel=$VALUE
      ;;
    --obs)
      obs=$VALUE
      ;;
      *)
    echo "ERROR: unknown parameter \"$PARAM\""
    usage
    exit 1
    ;;
  esac
  shift
done

echo "-- Creating $pkgname-$pkgver tarball from $path"

rm -rf /tmp/mixmod-$pkgver
#git archive HEAD --prefix=$pkgname-$pkgver/ | bzip2 > /tmp/$pkgname-$pkgver.tar.bz2
cd /tmp
wget -c https://github.com/mixmod/mixmod/archive/v${pkgver}.tar.gz
tar xzf v${pkgver}.tar.gz


rm -f "$pkgname"_$debver*
cp v${pkgver}.tar.gz "$pkgname"_$debver.orig.tar.gz
cd /tmp/mixmod-$pkgver

cp -r ~/projects/openturns/mixmod-pkg/debian .  

# build source package
echo "-- Creating source package "$pkgname"_$debver-$rel"
debuild -us -uc -S || echo "failed"

# rpm files
echo "-- Copying files to $obs"
cp -v ~/projects/openturns/mixmod-pkg/$pkgname.spec /tmp/v$pkgver.tar.gz $obs
cp -v ~/projects/openturns/mixmod-pkg/$pkgname-rpmlintrc $obs
cp -v /tmp/"$pkgname"_$debver.orig.tar.gz /tmp/"$pkgname"_$debver-$rel.dsc /tmp/"$pkgname"_$debver-$rel.debian.tar.xz $obs


# build binary packages
MAKEFLAGS="-j20" DEB_BUILD_OPTIONS="parallel=20" debuild -us -uc


