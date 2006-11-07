%define		module	IPy
Summary:	Class and tools for handling of IPv4 and IPv6 addresses and networks
Summary(pl):	Klasy i narzêdzia do obs³ugi adresów i sieci IPv4 i IPv6
Name:		python-%{module}
Version:	0.52
Release:	1
License:	BSD
Group:		Libraries/Python
Source0:	http://cheeseshop.python.org/packages/source/I/IPy/%{module}-%{version}.tar.gz
# Source0-md5:	750a19436bc86f89b692c73e74aa2811
URL:		http://software.inl.fr/trac/trac.cgi/wiki/IPy
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

%description -l pl
Klasa IP pozwala w wygodny sposób analizowaæ i obs³ugiwaæ wiêkszo¶æ
u¿ywanych notacji zapisu adresów i sieci IPv4 i IPv6. Jest w du¿ej
czê¶ci zainspirowana interfejsem modu³u Perla RIPE Net::IP, ale nie
wspó³dzieli z nim implementacji. Nie dzieli masek sieciowych nie-CIDR,
wiêc zabawne rzeczy typu maska 0xffffff0f s± tutaj niewykonalne.

%prep
%setup -q -n %{module}-%{version}

%build
python setup.py build

%install
rm -rf $RPM_BUILD_ROOT

python setup.py install \
        --single-version-externally-managed \
	--optimize=2 \
	--root $RPM_BUILD_ROOT

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README AUTHORS COPYING
%attr(755,root,root) %{py_sitescriptdir}/*.py[co]
%{py_sitescriptdir}/*.egg-info
