%if 0%{?rhel} == 7
%define python3_vers python36
%else
%define python3_vers python3
%endif

Name:           python-eccodes
Version:        0.9.3
Release:        2%{?dist}
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

%{!?el7:Requires: python36-cffi}


%description -n %{python3_vers}-eccodes
Python3 bindings for eccodes.


%prep
%autosetup -n eccodes-python-%{version}

%build
%py3_build

%install
%py3_install

%check
# it seems that the tests are missing
#%{__python3} setup.py test

%files -n %{python3_vers}-eccodes
%doc README.rst
%{python3_sitelib}/*


%changelog
* Thu Nov  7 2019 Daniele Branchini <dbranchini@arpae.it> - 0.9.3-2
- Added missing dependency (fix #1)

* Thu Oct 10 2019 Daniele Branchini <dbranchini@arpae.it> - 0.9.3-1
- Upstream update

* Fri Jun 14 2019 Daniele Branchini <dbranchini@arpae.it> - 0.9.1-1
- Initial package
