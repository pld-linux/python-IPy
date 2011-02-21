%define		module	IPy
Summary:	Class and tools for handling of IPv4 and IPv6 addresses and networks
Summary(pl.UTF-8):	Klasy i narzędzia do obsługi adresów i sieci IPv4 i IPv6
Name:		python-%{module}
Version:	0.74
Release:	1
License:	BSD
Group:		Libraries/Python
Source0:	http://cheeseshop.python.org/packages/source/I/IPy/%{module}-%{version}.tar.gz
# Source0-md5:	f4f7ddc7c5e55a47222a5cc6c0a87b6d
URL:		https://github.com/haypo/python-ipy/wiki
BuildRequires:	python-devel >= 1:2.5
BuildRequires:	python-setuptools
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.174
%pyrequires_eq	python-modules
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

%prep
%setup -q -n %{module}-%{version}

%build
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT

%{__python} setup.py install \
	--optimize=2 \
	--root $RPM_BUILD_ROOT

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog PKG-INFO README AUTHORS COPYING
%attr(755,root,root) %{py_sitescriptdir}/*.py[co]
%{py_sitescriptdir}/*.egg-info
