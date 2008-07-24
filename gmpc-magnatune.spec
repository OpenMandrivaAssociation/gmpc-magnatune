Summary:	A magnatune browser plugin for gmpc
Name:		gmpc-magnatune
Version:	0.15.5.0
Release:	%mkrel 3
License:	GPLv2+
Group:		Sound
Url:		http://www.sarine.nl//gmpc-plugins-magnatune
Source0:	http://download.sarine.nl/download/gmpc-0.15.5/%{name}-%{version}.tar.bz2
BuildRequires:	libmpd-devel
BuildRequires:	libxml2-devel
BuildRequires:	libglade2.0-devel
BuildRequires:	gmpc-devel
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
%{_datadir}/gmpc/plugins/magnatuneplugin.la
%{_datadir}/gmpc/plugins/magnatuneplugin.so
%{_datadir}/gmpc/plugins/magnatune/magnatune.png
%{_datadir}/gmpc/plugins/magnatune/xdg-open
