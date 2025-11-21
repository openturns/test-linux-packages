Name:           spectra
Version:        1.0.1
Release:        1%{?dist}
Summary:        C++ Library For Large Scale Eigenvalue Problems
Group:          System Environment/Libraries
License:        MPL2
URL:            https://spectralib.org/
Source0:        https://github.com/yixuan/spectra/archive/spectra-%{version}.tar.bz2
BuildArch:      noarch
BuildRequires:  gcc-c++, cmake, eigen3-devel
Requires:       spectra-devel

%description
C++ Library For Large Scale Eigenvalue Problems.

%package devel
Summary:        C++ Library For Large Scale Eigenvalue Problems
Group:          Development/Libraries/C and C++
Requires:       eigen3-devel

%description devel
C++ Library For Large Scale Eigenvalue Problems (development files)

%prep
%setup -q

%build
%cmake
%cmake_build

%install
%cmake_install

%files devel
%defattr(-,root,root,-)
%{_includedir}/Spectra/
%{_prefix}/share/spectra/

%changelog
* Fri Oct 15 2021 Julien Schueller <schueller at phimeca dot com> 1.0.0-1
- Initial package creation
