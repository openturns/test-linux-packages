# norootforbuild

Name:           fmilib
Version:        3.0.4
Release:        1%{?dist}
Summary:        open-source implementation of the FMI open standard
Group:          System Environment/Libraries
License:        BSD
URL:            https://github.com/modelon-community/fmi-library
Source0:        https://github.com/modelon-community/fmi-library/archive/%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires:  gcc, cmake
%if 0%{?suse_version}
BuildRequires:  libexpat-devel
%else
BuildRequires:  expat-devel
%endif
BuildRequires:  minizip-devel

%description
FMI Library (FMIL) is a software package written in C that enables integration
of Functional Mock-up Units (FMUs) import in applications. FMI Library is an
independent open-source implementation of the FMI open standard
(www.fmi-standard.org). The library provides a C API for interacting with all
parts of FMUs, including unzipping, loading of shared object files (DLLs)
contained in FMUs, as well as parsing of XML model metadata files. The user is
thereby relieved from managing the details of FMU interaction, which
significantly reduce the time required to implement FMU import capabilities.

%package devel
Summary:        Development files for %{name}
Group:          Development/Libraries/C and C++
Requires:       %{name} = %{version}

%description devel
Header files and library links for fmilib 

%prep
%setup -q -n fmi-library-%{version}

%build
%cmake -DFMILIB_BUILD_STATIC_LIB=OFF -DFMILIB_BUILD_TESTS=OFF -DFMILIB_EXTERNAL_LIBS=ON
%cmake_build

%install
%cmake_install
rm -r %{buildroot}%{_datadir}/doc/

%files
%defattr(-,root,root,-)
%{_libdir}/libfmilib_shared.so

%files devel
%defattr(-,root,root,-)
%{_includedir}/FMI*/
%{_includedir}/JM/
%{_includedir}/fmilib*

%changelog
* Thu Nov 20 2025 Julien Schueller <schueller at phimeca dot com> 3.0.4-1
- Initial package creation
