FROM clearlinux:latest

RUN swupd bundle-add c-basic os-core-dev python3-basic devpkg-openblas devpkg-libxml2 devpkg-boost machine-learning-basic --skip-diskspace-check
RUN cd /tmp && git clone --depth 1 https://github.com/openturns/openturns.git && cd openturns && cmake -DCMAKE_INSTALL_PREFIX=~/.local -DCMAKE_UNITY_BUILD=ON -DCMAKE_UNITY_BUILD_BATCH_SIZE=32 -DSWIG_COMPILE_FLAGS="-O1" . && make install -j8 && ctest -R pyinstall -j8 --timeout 200
