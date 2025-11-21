# norootforbuild

Name:           nlopt
Version:        2.10.0
Release:        1%{?dist}
Summary:        A library for nonlinear optimization
License:        LGPL-2.0
Group:          Development/Libraries/C and C++
Url:            http://ab-initio.mit.edu/wiki/index.php/NLopt
Source0:        https://github.com/stevengj/nlopt/archive/refs/tags/v%{version}.tar.gz
BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  pkgconfig
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
NLopt is a free/open-source library for nonlinear optimization,
providing a common interface for a number of different free
optimization routines available online as well as original
implementations of various other algorithms.

%package     -n lib%{name}0
Summary:        A library for nonlinear optimization
Group:          System/Libraries
Provides:       nlopt

%description -n lib%{name}0
NLopt is a free/open-source library for nonlinear optimization,
providing a common interface for a number of different free
optimization routines available online as well as original
implementations of various other algorithms.

%package        devel
Summary:        Development files for %{name}
Group:          Development/Libraries/C and C++
Requires:       lib%{name}0 = %{version}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%setup -q

%build
%cmake -DCMAKE_SKIP_INSTALL_RPATH=TRUE
%cmake_build

%install
%cmake_install

%post -n lib%{name}0 -p /sbin/ldconfig

%postun -n lib%{name}0 -p /sbin/ldconfig

%files -n lib%{name}0
%defattr(-,root,root,-)
%{_libdir}/*.so.*

%files devel
%defattr(-,root,root,-)
%doc AUTHORS COPYING NEWS.md README.md TODO
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/cmake/nlopt/
%{_libdir}/pkgconfig/%{name}.pc
%{_mandir}/man3/%{name}*

%changelog
* Thu Nov 20 2025 Julien Schueller <schueller at phimeca dot com> 12.10-1
- Initial package creation
