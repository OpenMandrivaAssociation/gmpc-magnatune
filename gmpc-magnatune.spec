Summary:	A magnatune browser plugin for gmpc
Name:		gmpc-magnatune
Version:	0.20.0
Release:	3
License:	GPLv2+
Group:		Sound
Url:		http://www.sarine.nl//gmpc-plugins-magnatune
Source0:	http://download.sarine.nl/Programs/gmpc/%{version}/%{name}-%{version}.tar.gz
BuildRequires:	libmpd-devel >= 0.15.98
BuildRequires:	libglade2.0-devel
BuildRequires:	gtk+2-devel >= 2.4
BuildRequires:	gmpc-devel >= 0.18.0
BuildRequires:	sqlite3-devel
BuildRequires:	intltool
Requires:	gmpc

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
%makeinstall_std

%files
%defattr(-,root,root)
%dir %{_datadir}/gmpc/plugins/magnatune
%{_libdir}/gmpc/plugins/magnatuneplugin.so
%{_datadir}/gmpc/plugins/magnatune/magnatune.png


%changelog
* Sun Dec 05 2010 Oden Eriksson <oeriksson@mandriva.com> 0.20.0-2mdv2011.0
+ Revision: 610907
- rebuild

* Mon Apr 05 2010 Funda Wang <fwang@mandriva.org> 0.20.0-1mdv2010.1
+ Revision: 531683
- update to new version 0.20.0

* Mon Dec 28 2009 Funda Wang <fwang@mandriva.org> 0.19.0-1mdv2010.1
+ Revision: 482926
- new version 0.19.0

* Mon May 25 2009 Funda Wang <fwang@mandriva.org> 0.18.0-1mdv2010.0
+ Revision: 379402
- New version 0.18.0

* Sun Jan 04 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 0.17.0-2mdv2009.1
+ Revision: 324626
- fix installation on x86_64
- update to new version 0.17.0

* Wed Dec 03 2008 Funda Wang <fwang@mandriva.org> 0.16.0-1mdv2009.1
+ Revision: 309577
- move plugins

  + Tomasz Pawel Gajc <tpg@mandriva.org>
    - fix file list
    - update to new version 0.16.0

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 0.15.5.0-3mdv2009.0
+ Revision: 246284
- rebuild

* Wed Jan 30 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 0.15.5.0-1mdv2008.1
+ Revision: 160389
- add spec file
- add source
- Created package structure for gmpc-magnatune.

