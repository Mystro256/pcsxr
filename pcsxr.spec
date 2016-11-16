%global svnversion 87788
%undefine _hardened_build
Name:           pcsxr
Version:        1.9.94
Release:        4%{?dist}
Summary:        A plugin based PlayStation (PSX) emulator with high compatibility

#All is GPLv2+ except:
# SOURCE/libpcsxcore/coff.h is BSD License (no advertising)
# SOURCE/libpcsxcore/sjisfont.h is Public Domain
# SOURCE/libpcsxcore/psemu_plugin_defs.h is Public Domain
License:        GPLv2+ and BSD and Public Domain
URL:            http://pcsxr.codeplex.com/
#The source can be downloaded here (1.9.94 is a snapshot of svn 87788):
#https://pcsxr.codeplex.com/downloads/get/756488
Source:         %{name}-%{svnversion}.zip
#http://pcsxr.codeplex.com/workitem/8567
Patch0:         %{name}-remove-assertion-64bit.patch

BuildRequires:  SDL2-devel
BuildRequires:  gtk3-devel
BuildRequires:  nasm
BuildRequires:  mesa-libGL-devel
BuildRequires:  gettext
BuildRequires:  libglade2-devel
BuildRequires:  libXv-devel
BuildRequires:  libXtst-devel
BuildRequires:  libcdio-devel
BuildRequires:  intltool
BuildRequires:  glib2-devel
BuildRequires:  libtool
BuildRequires:  autoconf
BuildRequires:  desktop-file-utils

%description
#modified from debian files
PCSX-Reloaded is an advanced PlayStation (PSX) emulator, which uses a plugin
architecture to provide full support for all components of the PSX. It has full
emulation support for game pads, videos, sound, memory cards, and other
important PSX components, and is able to play many games without problems.

%prep
%setup -q -n %{name}
#remove any unnecessary files:
rm -f -r win32 macosx
#suppresses 64 bit assert issues (patch):
%patch0 -p1

%build
autoreconf -ivf
%configure --prefix=%{_prefix} --enable-libcdio --enable-opengl
%{make_build} V=1

%install
%{make_install}

desktop-file-install \
  --remove-key=Encoding \
  --dir %{buildroot}%{_datadir}/applications \
  %{buildroot}%{_datadir}/applications/%{name}.desktop

%find_lang %{name}

%files -f %{name}.lang
%doc doc/keys.txt doc/tweaks.txt AUTHORS README
%license COPYING
%{_mandir}/man1/%{name}.1*
%{_datadir}/%{name}/
%{_datadir}/pixmaps/%{name}-icon.png
%{_datadir}/psemu/
%{_bindir}/%{name}
%{_libdir}/games/psemu/
%{_datadir}/applications/%{name}.desktop

%changelog
* Wed Nov 16 2016 Adrian Reber <adrian@lisas.de> - 1.9.94-4
- Rebuild for libcdio-0.94

* Wed Nov 02 2016 Leigh Scott <leigh123linux@googlemail.com> - 1.9.94-3
- Disable hardening (rfbz#4316)

* Tue Oct 28 2014 Nicolas Chauvet <kwizart@gmail.com> - 1.9.94-2
- Restore dist tag

* Mon Oct 27 2014 Jeremy Newton <alexjnewt@hotmail.com> - 1.9.94-1
- Updated to 1.9.94 release (marked as alpha on website)
- Use SDL2

* Sat Apr 5 2014 Jeremy Newton <alexjnewt@hotmail.com> - 1.9.93-2.svn89782
- Update to svn for Fedora 21 (beta 1.9.93 version doesn't build)

* Sat Apr 5 2014 Jeremy Newton <alexjnewt@hotmail.com> - 1.9.93-1
- Updated to new beta release

* Thu May 30 2013 Jeremy Newton <alexjnewt@hotmail.com> - 1.9.92-4.20130530svn85000
- Updated to new SVN version

* Sat Feb 16 2013 Jeremy Newton <alexjnewt@hotmail.com> - 1.9.92-3.20130216svn82923
- Updated to new SVN version
- Changing version numbering to match Guidelines

* Fri Jan 4 2013 Jeremy Newton <alexjnewt@hotmail.com> - 1.9.92-2.20130104svn82044
- Fixed missing gtk3 dependency

* Fri Jan 4 2013 Jeremy Newton <alexjnewt@hotmail.com> - 1.9.92-1.20130104svn82044
- Updated to new SVN checkout version
- Removed unnecessary zero length Doc file (NEWS)

* Mon Jul 23 2012 Jeremy Newton <alexjnewt@hotmail.com> - 1.9.92-1.20120723svn78971
- Added a patch to temporarily fix a 64bit-only problem

* Thu Jul 19 2012 Jeremy Newton <alexjnewt@hotmail.com> - 1.9.92-1.20120719svn78971
- Updated to new SVN checkout version
- Removed unnessary hicolor icon updating

* Thu Jul 5 2012 Jeremy Newton <alexjnewt@hotmail.com> - 1.9.92-1.20120705svn78288
- Updated to new SVN checkout version

* Fri Mar 9 2012 Jeremy Newton <alexjnewt@hotmail.com> - 1.9.92-1.20120421svn77577
- Updated to new SVN checkout version

* Fri Mar 9 2012 Jeremy Newton <alexjnewt@hotmail.com> - 1.9.92-1.20120309svn75683
- Updated to new SVN checkout version
- Changed define to global

* Sun Feb 19 2012 Jeremy Newton <alexjnewt@hotmail.com> - 1.9.92-1.20120219svn75200
- Updated to new SVN checkout version

* Sun Feb 19 2012 Jeremy Newton <alexjnewt@hotmail.com> - 1.9.92-1.20120219svn75156
- Updated to new SVN checkout version
- Added svn macro
- Removed incorrect disabling of opengl for 64bit

* Wed Feb 8 2012 Jeremy Newton <alexjnewt@hotmail.com> - 1.9.92-3.20120128svn73976
- Minor source change for convenience.

* Wed Feb 8 2012 Jeremy Newton <alexjnewt@hotmail.com> - 1.9.92-2.20120128svn73976
- Fixed and optimized source files for size and convenience.
- Added missing file in license breakdown

* Sat Jan 28 2012 Jeremy Newton <alexjnewt@hotmail.com> - 1.9.92-1.20120128svn73976
- Fixed version number to be more specific
- Fixed inproper license
- Trimmed down the source, removed non-linux code

* Sat Jan 28 2012 Jeremy Newton <alexjnewt@hotmail.com> - 1.9.92-1.20120128svn
- Initial package SPEC created
