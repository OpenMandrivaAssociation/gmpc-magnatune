Summary:	A magnatune browser plugin for gmpc
Name:		gmpc-magnatune
Version:	0.18.0
Release:	%mkrel 1
License:	GPLv2+
Group:		Sound
Url:		http://www.sarine.nl//gmpc-plugins-magnatune
Source0:	http://download.sarine.nl/Programs/gmpc/%{version}/%{name}-%{version}.tar.gz
BuildRequires:	libmpd-devel >= 0.15.98
BuildRequires:	libglade2.0-devel
BuildRequires:	gtk+2-devel >= 2.4
BuildRequires:	gmpc-devel >= 0.18.0
BuildRequires:	sqlite3-devel
Requires:	gmpc
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
The magnatune plugin provides an interface to the 
www.magnatune.com website. The plugin allows you 
to browse, and preview available albums.
(It uses the 128kbit mp3 version).The magnatune 
plugin provides a double function, it also uses 
the data from the magnatune website to fetch 
cover art.

%prep
%setup -q

%build
%configure2_5x
%make

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}
%makeinstall_std

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files
%defattr(-,root,root)
%dir %{_datadir}/gmpc/plugins/magnatune
%{_libdir}/gmpc/plugins/magnatuneplugin.la
%{_libdir}/gmpc/plugins/magnatuneplugin.so
%{_datadir}/gmpc/plugins/magnatune/magnatune.png
