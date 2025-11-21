Name:           hmat-oss 
Version:        1.9.0
Release:        1%{?dist}
Summary:        A hierarchical matrix C/C++ library
Group:          System Environment/Libraries
License:        GPL2
URL:            https://github.com/jeromerobert/hmat-oss
Source0:        https://github.com/jeromerobert/hmat-oss/archive/%{version}.tar.gz
Patch0:         mageia.patch
BuildRequires:  gcc-c++, cmake
BuildRequires:  lapack-devel
%if 0%{?suse_version}
BuildRequires:  lapacke-devel
BuildRequires:  cblas-devel
%endif
%if 0%{?centos_version} || 0%{?fedora_version}
BuildRequires:  atlas-devel
%endif
%if 0%{?fedora_version}
BuildRequires:  blas-static lapack-static
%endif
%if 0%{?mageia}
BuildRequires:  lib64blas-static-devel lib64lapack-static-devel
%endif
Requires:       libhmat-oss3

%description
A hierarchical matrix C/C++ library including a LU solver.

%package -n libhmat-oss3
Summary:        A hierarchical matrix C/C++ library 
Group:          Development/Libraries/C and C++
%if 0%{?mageia}
Requires:       lib64lapack3
%else
Requires:       lapack
%endif
%if 0%{?suse_version}
Requires:       cblas
Requires:       lapacke
%endif
%if 0%{?centos_version} || 0%{?fedora_version}
Requires:       atlas
%endif

%description -n libhmat-oss3
A hierarchical matrix C/C++ library (binaries) 

%package devel
Summary:        A hierarchical matrix C/C++ library 
Group:          Development/Libraries/C and C++
Requires:       libhmat-oss3 = %{version}
%if 0%{?suse_version}
Requires:       lapacke-devel
%else
Requires:       lapack-devel
%endif

%description devel
A hierarchical matrix C/C++ library (development files)

%prep
%setup -q
%if 0%{?mageia}
%patch0 -p1
%endif

%build
%if 0%{?centos_version} || 0%{?mageia}
export CXXFLAGS="${CXXFLAGS} -I/usr/include/lapacke"
%endif
%if 0%{?suse_version}
%cmake -DCBLAS_LIBRARIES="cblas;blas" -DLAPACKE_LIBRARIES="lapacke;lapack" .
%else
%cmake -DCBLAS_cblas_INCLUDE=/usr/include/cblas -DLAPACKE_LIBRARIES="lapacke;lapack" .
%endif
%cmake_build

%install
%cmake_install

%post -n libhmat-oss3 -p /sbin/ldconfig
%postun -n libhmat-oss3 -p /sbin/ldconfig

%files -n libhmat-oss3
%defattr(-,root,root,-)
%{_libdir}/*.so.*

%files devel
%defattr(-,root,root,-)
%dir %{_includedir}/hmat/
%{_includedir}/hmat/*.h
%{_libdir}/*.so
%dir %{_libdir}/cmake/hmat/
%{_libdir}/cmake/hmat/*.cmake

%changelog
* Sat Nov 22 2014 Julien Schueller <schueller at phimeca dot com> 1.0-1
- Initial package creation
