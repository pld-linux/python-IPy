# Conditional build:
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

# NOTES:
# - 'module' should match the Python import path (first component?)
# - 'egg_name' should equal to Python egg name
# - 'pypi_name' must match the Python Package Index name
%define		module		IPy
%define		egg_name	IPy
%define		pypi_name	IPy
Summary:	Class and tools for handling of IPv4 and IPv6 addresses and networks
Summary(pl.UTF-8):	Klasy i narzędzia do obsługi adresów i sieci IPv4 i IPv6
Name:		python-%{pypi_name}
Version:	0.83
Release:	1
License:	BSD
Group:		Libraries/Python
Source0:	https://pypi.debian.net/IPy/%{module}-%{version}.tar.gz
# Source0-md5:	7b8c6eb4111b15aea31b67108e769712
URL:		https://github.com/haypo/python-ipy/wiki
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
%if %{with python2}
BuildRequires:	python-modules
BuildRequires:	python-setuptools
%endif
%if %{with python3}
BuildRequires:	python3-modules
BuildRequires:	python3-setuptools
%endif
Requires:	python-modules
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The IP class allows a comfortable parsing and handling for most
notations in use for IPv4 and IPv6 Addresses and Networks. It was
greatly inspired bei RIPE's Perl module Net::IP's interface but
doesn't share the Implementation. It doesn't share non-CIDR netmasks,
so funky stuff lixe a netmask 0xffffff0f can't be done here.

%description -l pl.UTF-8
Klasa IP pozwala w wygodny sposób analizować i obsługiwać większość
używanych notacji zapisu adresów i sieci IPv4 i IPv6. Jest w dużej
części zainspirowana interfejsem modułu Perla RIPE Net::IP, ale nie
współdzieli z nim implementacji. Nie dzieli masek sieciowych nie-CIDR,
więc zabawne rzeczy typu maska 0xffffff0f są tutaj niewykonalne.

%package -n python3-%{pypi_name}
Summary:	-
Summary(pl.UTF-8):	-
Group:		Libraries/Python
Requires:	python3-modules

%description -n python3-%{pypi_name}
The IP class allows a comfortable parsing and handling for most
notations in use for IPv4 and IPv6 Addresses and Networks. It was
greatly inspired bei RIPE's Perl module Net::IP's interface but
doesn't share the Implementation. It doesn't share non-CIDR netmasks,
so funky stuff lixe a netmask 0xffffff0f can't be done here.

%description -n python3-%{pypi_name} -l pl.UTF-8
Klasa IP pozwala w wygodny sposób analizować i obsługiwać większość
używanych notacji zapisu adresów i sieci IPv4 i IPv6. Jest w dużej
części zainspirowana interfejsem modułu Perla RIPE Net::IP, ale nie
współdzieli z nim implementacji. Nie dzieli masek sieciowych nie-CIDR,
więc zabawne rzeczy typu maska 0xffffff0f są tutaj niewykonalne.

%prep
%setup -q -n %{pypi_name}-%{version}

%build
%if %{with python2}
%py_build
%endif

%if %{with python3}
%py3_build
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

# when files are installed in other way that standard 'setup.py
# they need to be (re-)compiled
# change %{py_sitedir} to %{py_sitescriptdir} for 'noarch' packages!
%py_ocomp $RPM_BUILD_ROOT%{py_sitedir}
%py_comp $RPM_BUILD_ROOT%{py_sitedir}

%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc ChangeLog README AUTHORS COPYING
%{py_sitescriptdir}/%{module}.py*
%{py_sitescriptdir}/%{egg_name}-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-%{pypi_name}
%defattr(644,root,root,755)
%doc ChangeLog README AUTHORS COPYING
%{py3_sitescriptdir}/%{module}.py*
%{py3_sitescriptdir}/__pycache__/%{module}.*.pyc
%{py3_sitescriptdir}/%{egg_name}-%{version}-py*.egg-info
%endif
