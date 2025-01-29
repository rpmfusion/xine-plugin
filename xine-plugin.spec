Name:           xine-plugin
Version:        1.0.2
Release:        29%{?dist}
Summary:        Mozilla/Netscape compatible media plugin

License:        GPLv2+
URL:            http://xinehq.de/
Source0:        http://prdownloads.sourceforge.net/xine/xine-plugin-%{version}.tar.bz2

# https://bugs.xine-project.org/show_bug.cgi?id=581
Patch0:         xine-plugin-1.0.2-Sync_prcpucfg_h_with_nspr.patch

BuildRequires:  gcc
BuildRequires:  libX11-devel
BuildRequires:  pkgconfig
BuildRequires:  xine-lib-devel
BuildRequires:  xorg-x11-proto-devel

Requires:       mozilla-filesystem

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
%patch -P0 -p0


%build
%configure --with-plugindir=%{_libdir}/mozilla/plugins
%make_build


%install
%make_install
rm -rf $RPM_BUILD_ROOT/%{_libdir}/mozilla/plugins/*.la


%files
%license COPYING
%doc AUTHORS README
%{_libdir}/mozilla/plugins/*


%changelog
* Wed Jan 29 2025 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 1.0.2-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Aug 02 2024 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 1.0.2-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sun Feb 04 2024 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 1.0.2-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Aug 02 2023 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 1.0.2-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon Aug 08 2022 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 1.0.2-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild and ffmpeg
  5.1

* Wed Feb 09 2022 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 1.0.2-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Aug 03 2021 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1.0.2-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Feb 04 2021 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1.0.2-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Aug 19 2020 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1.0.2-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Feb 05 2020 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1.0.2-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Aug 09 2019 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1.0.2-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Mar 05 2019 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1.0.2-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Aug 19 2018 Leigh Scott <leigh123linux@googlemail.com> - 1.0.2-17
- Rebuilt for Fedora 29 Mass Rebuild binutils issue

* Fri Jul 27 2018 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1.0.2-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Jul 21 2018 Xavier Bachelot <xavier@bachelot.org> - 1.0.2-15
- Add BR: gcc.
- Remove Group:.

* Thu Mar 01 2018 RPM Fusion Release Engineering <leigh123linux@googlemail.com> - 1.0.2-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 31 2017 RPM Fusion Release Engineering <kwizart@rpmfusion.org> - 1.0.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Mar 25 2017 Xavier Bachelot <xavier@bachelot.org> - 1.0.2-12
- Sync prcpucfg.h with nspr to fix build on aarch64.
- Cleanup specfile.

* Tue Mar 21 2017 RPM Fusion Release Engineering <kwizart@rpmfusion.org> - 1.0.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Aug 31 2014 Sérgio Basto <sergio@serjux.com> - 1.0.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Wed Oct 23 2013 Xavier Bachelot <xavier@bachelot.org> - 1.0.2-9
- Rebuild for xine-lib 1.2.

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
