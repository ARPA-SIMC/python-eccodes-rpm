%if 0%{?rhel} == 7
%define python3_vers python36
%else
%define python3_vers python3
%endif

%global releaseno 1

Name:           python-eccodes
Version:        0.9.1
Release:        1%{?dist}
Summary:        Python bindings for eccodes

License:        Apache License, Version 2.0
URL:            https://pypi.org/project/eccodes-python/
Source0:        https://files.pythonhosted.org/packages/source/e/eccodes-python/eccodes-python-%{version}.tar.gz#/eccodes-python-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  %{python3_vers}-devel
BuildRequires:  %{python3_vers}-numpy
BuildRequires:  %{python3_vers}-pytest
BuildRequires:  %{python3_vers}-setuptools
BuildRequires:  eccodes-devel

Requires:       eccodes

%description
Python bindings for eccodes.


%package     -n %{python3_vers}-eccodes
Summary:        Python3 bindings for Magics

%description -n %{python3_vers}-eccodes
Python3 bindings for eccodes.


%prep
%autosetup -n eccodes-%{version}

%build
%py3_build

%install
%py3_install

%check
# TODO: it seems that the tests are missing
%{__python3} setup.py test

%files -n %{python3_vers}-eccodes
%doc README.rst
%{python3_sitelib}/*


%changelog
* Fri Jun 14 2019 Daniele Branchini <dbranchini@arpae.it>
- Initial package
