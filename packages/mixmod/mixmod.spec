Name:           mixmod
Version:        2.1.11
Release:        1%{?dist}
Summary:        Classification with Mixture Modelling
Group:          System Environment/Libraries
License:        GPL2
URL:            https://github.com/mixmod/mixmod
Source0:        https://github.com/mixmod/mixmod/archive/v%{version}.tar.gz
BuildRequires:  gcc-c++, cmake
BuildRequires:  eigen3-devel
Requires:       libmixmod

%description
A hierarchical matrix C/C++ library including a LU solver.

%package -n libmixmod
Summary:        A hierarchical matrix C/C++ library 
Group:          Development/Libraries/C and C++

%description -n libmixmod
A hierarchical matrix C/C++ library (binaries) 

%package devel
Summary:        A hierarchical matrix C/C++ library 
Group:          Development/Libraries/C and C++
Requires:       libmixmod = %{version}

%description devel
A hierarchical matrix C/C++ library (development files)

%prep
%setup -q

%build
%cmake -DCMAKE_UNITY_BUILD=ON .
%cmake_build

%install
%cmake_install

%post -n libmixmod -p /sbin/ldconfig
%postun -n libmixmod -p /sbin/ldconfig

%files -n libmixmod
%defattr(-,root,root,-)
%{_libdir}/*.so.*
%dir %{_datadir}/mixmod/
%{_datadir}/mixmod/*

%files devel
%defattr(-,root,root,-)
%dir %{_includedir}/mixmod/
%{_includedir}/mixmod/*
%{_includedir}/mixmod.h
%{_libdir}/*.so

%changelog
* Tue Jan 09 2024 Julien Schueller <schueller at phimeca dot com> 2.1.10-1
- Initial package creation
