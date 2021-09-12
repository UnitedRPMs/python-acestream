Name: python-acestream
Version: 0.2.0
Release: 1%{?dist}
Summary: Python Acestream
License: GPLv3
URL: https://github.com/jonian/python-acestream
BuildArch: noarch
Source0: %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
BuildRequires: python%{python3_pkgversion}-devel
BuildRequires: python%{python3_pkgversion}-setuptools
BuildRequires: python3-rpm-macros

%description
Python interface to interact with the AceStream Engine and the HTTP API.

%package -n python%{python3_pkgversion}-acestream
Summary: %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-acestream}

%description -n python%{python3_pkgversion}-acestream
%{description}

%prep
%setup -q

%build
%py3_build

%install
%py3_install

%files -n python%{python3_pkgversion}-acestream
%doc README.md
%license LICENSE.txt
%{python3_sitelib}/*

%changelog
* Sat Sep 11 2021 Sérgio Basto <sergio@serjux.com> - 0.2.0-1
- Update python-acestream to 0.2.0

* Wed Jun 10 2020 Unitedrpms Project <unitedrpms AT protonmail DOT com> 0.1.7-2 
- Rebuilt for python3.9

* Mon Dec 16 2019 Sérgio Basto <sergio@serjux.com> - 0.1.7-1
- Update to 0.1.7
