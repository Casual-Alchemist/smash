Name: smash
Version: 
Release: 1
Summary: 8051 In-System Progamming (ISP) tool
Group:Applications/Engineering		
License: GPL
URL: http://github.com/zilogic-systems/smash
Source0: smash-.tar.gz
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires: python >= 2.4, pyserial >= 2.2, pygtk2 >= 2.8, dbus-python >= 0.71, pygtk2-libglade >= 2.12

%description
Smash is an 8051 micro-controller In-System Programming (ISP) tool,
for Philips and NXP micro-controllers. The currently supported
micro-controllers include P89V660, P89V662, P89V664, P89V51RB2,
P89V51RC2, P89V51RD2.

%prep
%setup -q

%build
make install DESTDIR=build/rpm

%install
rm -rf %{buildroot}
cp -a build/rpm %{buildroot}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{_bindir}/*
%{_datadir}/%{name}

%changelog
* Mon May 15 2011 Deepak <deepak@zilogic.com>
Initial version
