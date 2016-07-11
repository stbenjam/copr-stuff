Name:       xrectsel
Version:    0.3.1
Release:	3%{?dist}
Summary:    Print the geometry of a rectangular screen region

Group:      Applications/System
License:    GPLv3
URL:        https://github.com/lolilolicon/xrectsel
Source0:    https://github.com/lolilolicon/xrectsel/archive/0.3.1.zip

Requires: libX11
BuildRequires: libX11
BuildRequires: libX11-devel
BuildRequires: gcc
BuildRequires: autoconf
BuildRequires: automake

%description
Print the geometry of a rectangular screen region

%prep
%setup -q

%build
./bootstrap
%configure
make

%install
%make_install

%files
%defattr(-,root,root)
%{_bindir}/%{name}


%changelog
* Mon Jul 11 2016 Stephen Benjamin <stephen@redhat.com> 0.3.1-3
- Package created
