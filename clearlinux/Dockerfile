FROM clearlinux:latest

RUN swupd bundle-add c-basic os-core-dev python3-basic devpkg-openblas devpkg-libxml2 devpkg-boost --skip-diskspace-check
RUN cd /tmp && git clone --depth 1 https://github.com/openturns/openturns.git && cd openturns && cmake -DCMAKE_INSTALL_PREFIX=~/.local -DUSE_COTIRE=ON -DCOTIRE_MAXIMUM_NUMBER_OF_UNITY_INCLUDES="-j16" -DSWIG_COMPILE_FLAGS="-O1" . && make install -j8 && ctest -R pyinstall -j8 --timeout 200
