Name:           pagmo2
Version:        2.19.1
Release:        1%{?dist}
Summary:        A C++ platform to perform parallel computations of optimisation tasks
Group:          System Environment/Libraries
License:        GPL3
URL:            https://esa.github.io/pagmo2/
Source0:        https://github.com/esa/pagmo2/archive/v%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  eigen3-devel
BuildRequires:  tbb-devel
BuildRequires:  boost-devel
%if 0%{?mageia}
BuildRequires:  boost-devel
%else
BuildRequires:  libboost_serialization-devel
%endif

%description
pagmo is a C++ scientific library for massively parallel optimization. It is
built around the idea of providing a unified interface to optimization
algorithms and to optimization problems and to make their deployment in
massively parallel environments easy.

%package devel
Summary:        Development files for %{name}
Group:          Development/Libraries/C and C++
Requires:       %{name} = %{version}
Requires:       eigen3-devel
%if 0%{?mageia}
Requires:       boost-devel
%else
Requires:       libboost_serialization-devel
%endif

%description devel
The %{name}-devel package contains development files for %{name}.

%prep
%setup -q -n %{name}-%{version}

%build
%cmake -DPAGMO_WITH_EIGEN3=ON -DCMAKE_UNITY_BUILD=ON
%cmake_build

%install
%cmake_install

%files
%defattr(-,root,root,-)
%{_libdir}/libpagmo.so.9*

%files devel
%defattr(-,root,root,-)
%{_libdir}/libpagmo.so
%{_includedir}/pagmo/
%{_libdir}/cmake/pagmo/

%changelog
* Thu Nov 20 2025 Julien Schueller <schueller at phimeca dot com> 2.19.1-1
- Initial package creation
