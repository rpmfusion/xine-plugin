Name:           xine-plugin
Version:        1.0.2
Release:        8%{?dist}
Summary:        Mozilla/Netscape compatible media plugin

Group:          Applications/Multimedia
License:        GPLv2+
URL:            http://xinehq.de/
Source0:        http://prdownloads.sourceforge.net/xine/xine-plugin-%{version}.tar.bz2
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  xine-lib-devel
BuildRequires:  pkgconfig
BuildRequires:  xorg-x11-proto-devel
BuildRequires:  libX11-devel

Requires: mozilla-filesystem

%description
This is a very simple netscape/mozilla browser plugin using the xine
engine to display multimedia streams.

Features:

- embedded display on browser window
- streaming playback directly from xine engine
- playback control using keyboard
- relative paths supported
- on screen display of buffering and stream information
- playlists and references support
- loop and repeat mode
- multiple instances within the same page
- javascript support


%prep
%setup -q

%build
%configure --with-plugindir=%{_libdir}/mozilla/plugins
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
rm -rf $RPM_BUILD_ROOT/%{_libdir}/mozilla/plugins/*.la


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc AUTHORS COPYING README
%{_libdir}/mozilla/plugins/*


%changelog
* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Jul 27 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Dec 11 2008 Martin Sourada <mso@fedoraproject.org> - 1.0.2-1
- new upstreame release 
- should fix rhbz #473830

* Sun Jun 22 2008 Martin Stransky <stransky@redhat.com> - 1.0.1-4
- rebuild against new xulrunner

* Sun Jun 01 2008 Martin Sourada <martin.sourada@gmail.com> - 1.0.1-3
- require mozilla-filesystem instead of xulrunner on >= F9

* Wed Apr 23 2008 Martin Sourada <martin.sourada@gmail.com> - 1.0.1-2
- remove the dropped patch from spec file completely

* Tue Apr 22 2008 Martin Sourada <martin.sourada@gmail.com> - 1.0.1-1
- new upstream release
- drop the xine-lib version patch - fixed in upstream

* Sat Feb 09 2008 Martin Sourada <martin.sourada@gmail.com> - 1.0-6
- rebuild for gcc 4.3
- add patch for x.y.z.w format xine-lib version string

* Tue Aug 21 2007 Martin Sourada <martin.sourada@seznam.cz> - 1.0-5
- rebuild 

* Thu Aug 09 2007 Martin Sourada <martin.sourada@seznam.cz> - 1.0-4
- update License: field to GPLv2+

* Wed Mar 14 2007 Martin Sourada <martin.sourada@seznam.cz> - 1.0-3
- fix rpmlint warning

* Tue Mar 13 2007 Martin Sourada <martin.sourada@seznam.cz> - 1.0-2
- add BR: xorg-x11-proto-devel, libX11-devel

* Sun Feb 04 2007 Martin Sourada <martin.sourada@seznam.cz> - 1.0-1
- Initial package
