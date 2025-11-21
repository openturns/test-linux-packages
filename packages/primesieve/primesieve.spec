Name:           primesieve
Version:        12.10
Release:        1%{?dist}
Summary:        Fast prime number generator
Group:          System Environment/Libraries
License:        BSD
URL:            https://github.com/kimwalisch/primesieve
Source0:        https://github.com/kimwalisch/primesieve/archive/v%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires:  gcc-c++
BuildRequires:  cmake

%description
primesieve is a command-line program and C/C++ library for quickly generating prime numbers.
It is very cache efficient, it detects your CPU's L1 & L2 cache sizes and allocates its main data structures accordingly.
It is also multi-threaded by default, it uses all available CPU cores whenever possible i.e. if sequential ordering is not required.
primesieve can generate primes and prime k-tuplets up to 264.

%package devel
Summary:        Development files for %{name}
Group:          Development/Libraries/C and C++
Requires:       %{name} = %{version}

%description devel
The %{name}-devel package contains development files for %{name}.

%prep
%setup -q -n %{name}-%{version}

%build
%cmake -DWITH_MULTIARCH=OFF
%cmake_build

%install
%cmake_install

%files
%defattr(-,root,root,-)
%{_bindir}/primesieve
%{_libdir}/libprimesieve.so.12*
%{_mandir}/man1/primesieve.*

%files devel
%defattr(-,root,root,-)
%{_libdir}/libprimesieve.so
%{_includedir}/primesieve*
%{_libdir}/cmake/primesieve/
%{_libdir}/pkgconfig/primesieve.pc

%changelog
* Thu Nov 20 2025 Julien Schueller <schueller at phimeca dot com> 12.10-1
- Initial package creation
