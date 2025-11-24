# norootforbuild
%global python_sitearch %{_libdir}/python%(python3 -c "import sysconfig; print(sysconfig.get_python_version())")/site-packages

Name:           agrum
Version:        2.3.0
Release:        0%{?dist}
Summary:        A GRaphical Universal Modeler
Group:          System Environment/Libraries
License:        LGPLv3+
URL:            http://agrum.gitlab.io/
Source0:        https://gitlab.com/agrumery/aGrUM/-/archive/%{version}/aGrUM-%{version}.tar.bz2
BuildRequires:  gcc-c++, cmake, swig
BuildRequires:  python3-devel
BuildRequires:  python3-scipy
BuildRequires:  python3-six
BuildRequires:  python3-pandas
BuildRequires:  python3-pydot
BuildRequires:  python3-matplotlib
BuildRequires:  python3-scikit-learn
Requires:       libagrum0

%description
aGrUM is a C++ library for graphical models.
It is designed for easily building applications using graphical models such as Bayesian networks,
influence diagrams, decision trees, GAI networks or Markov decision processes.

%package -n libagrum0
Summary:        aGrUM library files
Group:          Development/Libraries/C and C++

%description -n libagrum0
Dynamic libraries for aGrUM.

%package devel
Summary:        aGrUM development files
Group:          Development/Libraries/C and C++
Requires:       libagrum0 = %{version}

%description devel
Development files for aGrUM library.

%package examples
Summary:        aGrUM examples
Group:          Productivity/Scientific/Math

%description examples
Example files for aGrUM

%package -n python3-%{name}
Summary:        aGrUM Python module
Group:          Productivity/Scientific/Math
Requires:       python3-scipy
Requires:       python3-six
Requires:       python3-pandas
Requires:       python3-pydot
Requires:       python3-matplotlib
Requires:       python3-scikit-learn
%description -n python3-%{name}
Python textual interface to aGrUM library

%prep
%setup -q -n aGrUM-%{version}

%build
%cmake -DCMAKE_SKIP_INSTALL_RPATH:BOOL=ON -DBUILD_PYTHON=ON
%cmake_build

%install
%cmake_install

%check
LD_LIBRARY_PATH=%{buildroot}%{_libdir} PYTHONPATH=%{buildroot}%{python_sitearch} python3 ./wrappers/pyagrum/testunits/gumTest.py

%post -n libagrum0 -p /sbin/ldconfig 
%postun -n libagrum0 -p /sbin/ldconfig 

%files -n libagrum0
%defattr(-,root,root,-)
%{_libdir}/*.so.*

%files devel
%defattr(-,root,root,-)
%dir %{_includedir}/%{name}
%{_includedir}/%{name}/*
%{_libdir}/*.so
%{_libdir}/cmake/
%{_libdir}/pkgconfig/agrum.pc

%files -n python3-%{name}
%defattr(-,root,root,-)
%{python_sitearch}/pyagrum*


%changelog
* Thu Nov 20 2025 Julien Schueller <schueller at phimeca dot com> 2.3.0-1
- Initial package creation

