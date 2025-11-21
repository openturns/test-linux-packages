Name:           nanoflann
Version:        1.8.0
Release:        1%{?dist}
Summary:        a C++ header-only library for Nearest Neighbor (NN) search wih KD-trees
Group:          System Environment/Libraries
License:        BSD
URL:            https://github.com/jlblancoc/nanoflann
Source0:        https://github.com/jlblancoc/nanoflann/archive/v%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  eigen3-devel

%description
nanoflann is a C++11 header-only library for building KD-Trees of datasets with different topologies:
R2, R3 (point clouds), SO(2) and SO(3) (2D and 3D rotation groups).

%package devel
Summary:        Development files for %{name}
Group:          Development/Libraries/C and C++
Requires:       %{name} = %{version}
Requires:       eigen3-devel

%description devel
The %{name}-devel package contains development files for %{name}.

%prep
%setup -q -n %{name}-%{version}

%build
%cmake -DNANOFLANN_BUILD_EXAMPLES=OFF -DNANOFLANN_BUILD_TESTS=OFF
%cmake_build

%install
%cmake_install

%files
%defattr(-,root,root,-)

%files devel
%defattr(-,root,root,-)
%{_includedir}/nanoflann.hpp
%{_datadir}/cmake/nanoflann/
%{_libdir}/pkgconfig/nanoflann.pc

%changelog
* Thu Nov 20 2025 Julien Schueller <schueller at phimeca dot com> 1.8.0-1
- Initial package creation
