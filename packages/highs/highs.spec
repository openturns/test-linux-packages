# norootforbuild

Name:           highs
Version:        1.12.0
Release:        1%{?dist}
Summary:        Linear optimization software
Group:          System Environment/Libraries
License:        MIT
URL:            https://highs.dev/
Source0:        https://github.com/ERGO-Code/HiGHS/archive/v%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  chrpath

%description
HiGHS is a high performance serial and parallel solver for large scale
sparse linear optimization problems of the form
	
    Minimize (1/2) x^TQx + c^Tx subject to L <= Ax <= U; l <= x <= u
	
where Q must be positive semi-definite and, if Q is zero, there may be a
requirement that some of the variables take integer values.  Thus HiGHS
can solve linear programming (LP) problems, convex quadratic programming
(QP) problems, and mixed integer programming (MIP) problems.  It is
mainly written in C++, but also has some C.
	
HiGHS has primal and dual revised simplex solvers, originally written by
Qi Huangfu and further developed by Julian Hall.  It also has an
interior point solver for LP written by Lukas Schork, an active set
solver for QP written by Michael Feldmeier, and a MIP solver written by
Leona Gottwald.  Other features have been added by Julian Hall and Ivet
Galabova, who manages the software engineering of HiGHS and interfaces
to C, C#, FORTRAN, Julia and Python.
 
Although HiGHS is freely available under the MIT license, we would be
pleased to learn about users' experience and give advice via email sent
to highsopt@gmail.com.

%package devel
Summary:        Development files for %{name}
Group:          Development/Libraries/C and C++
Requires:       %{name} = %{version}

%description devel
Header files and library links for HiGHS

%prep
%setup -q -n HiGHS-%{version}

%build
%cmake -DBUILD_EXAMPLES=OFF -DBUILD_TESTING=OFF -DCMAKE_UNITY_BUILD=ON
%cmake_build

%install
%cmake_install
chrpath -d %{buildroot}%{_bindir}/highs

%files
%defattr(-,root,root,-)
%{_bindir}/highs
%{_libdir}/libhighs.so.1*

%files devel
%defattr(-,root,root,-)
%{_includedir}/highs_export.h
%{_includedir}/highs/
%{_libdir}/cmake/highs/
%{_libdir}/libhighs.so
%{_libdir}/pkgconfig/highs.pc

%changelog
* Thu Nov 20 2025 Julien Schueller <schueller at phimeca dot com> 1.12.0-1
- Initial package creation
