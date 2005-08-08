
%define 	module	IPy

Summary:	A Python module for handling IPv4 and IPv6 Addresses and Networks
Summary(pl):	Modu³ jêzyka Python do obs³ugi adresów i sieci IPv4 oraz IPv6
Name:		python-%{module}
Version:	0.42
Release:	1
License:	GPL
Group:		Libraries/Python
Source0:	http://c0re.23.nu/c0de/IPy/%{module}-%{version}.tar.gz
# Source0-md5:	76bb49482b8c99a49505331558d0eb71
URL:		http://c0re.23.nu/c0de/IPy/
BuildRequires:	python
%pyrequires_eq 	python-modules
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A Python module for handling IPv4 and IPv6 Addresses and Networks.

%description -l pl
Modu³ jêzyka Python do obs³ugi adresów i sieci IPv4 oraz IPv6.

%prep
%setup -q -n %{module}-%{version}
python setup.py build

%install
rm -rf $RPM_BUILD_ROOT

python setup.py install \
        --root=$RPM_BUILD_ROOT \
        --optimize=2

%py_comp $RPM_BUILD_ROOT%{py_sitescriptdir}
%py_ocomp $RPM_BUILD_ROOT%{py_sitescriptdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc example/*.py CHANGES README THANKS
%{py_sitescriptdir}/*.py[co]
