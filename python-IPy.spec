%define		module	IPy
Summary:	Class and tools for handling of IPv4 and IPv6 addresses and networks
Name:		python-%{module}
Version:	0.51
Release:	1
License:	BSD
Group:		Libraries/Python
Source0:	http://cheeseshop.python.org/packages/source/I/IPy/%{module}-%{version}.tar.gz
# Source0-md5:	46328d18e7c4c6191a9ba7af7afc3e9e
URL:		http://software.inl.fr/trac/trac.cgi/wiki/IPy
BuildRequires:	python-devel >= 1:2.5
BuildRequires:	rpmbuild(macros) >= 1.174
%pyrequires_eq	python-modules
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The IP class allows a comfortable parsing and handling for most notations in
use for IPv4 and IPv6 Addresses and Networks. It was greatly inspired bei
RIPE's Perl module NET::IP's interface but doesn't share the Implementation. It
doesn't share non-CIDR netmasks, so funky stuff lixe a netmask 0xffffff0f can't
be done here.

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

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README AUTHORS COPYING
%attr(755,root,root) %{py_sitescriptdir}/*.py[co]
%{py_sitescriptdir}/*.egg-info
