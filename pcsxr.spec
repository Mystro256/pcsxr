%global svnversion 82044
Name:           pcsxr
Version:        1.9.92
Release:        1.20130104svn%{svnversion}%{?dist}
Summary:        A plugin based PlayStation (PSX) emulator with high compatibility

#All is GPLv2+ except:
# SOURCE/libpcsxcore/coff.h is BSD License (no advertising)
# SOURCE/libpcsxcore/sjisfont.h is Public Domain
# SOURCE/libpcsxcore/psemu_plugin_defs.h is Public Domain
License:        GPLv2+ and BSD and Public Domain
Url:            http://pcsxr.codeplex.com/
#The source can be downloaded here:
#http://pcsxr.codeplex.com/SourceControl/changeset/82044
Source:         %{name}-%{svnversion}.zip
#http://pcsxr.codeplex.com/workitem/8567
Patch0:         %{name}-remove-assertion-64bit.patch

BuildRequires:  SDL-devel
BuildRequires:  gtk2-devel
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
rm -f -r win32 macosx debian-upstream
%patch0 -p1

%build
sh autogen.sh
%configure --prefix=/usr --enable-libcdio --enable-opengl
make %{?_smp_mflags}

%install
make %{?_smp_mflags} install DESTDIR=%{buildroot}
desktop-file-install \
  --remove-key=Encoding \
  --dir %{buildroot}%{_datadir}/applications \
  data/%{name}.desktop
%find_lang %{name}

%files -f %{name}.lang
%doc doc/keys.txt doc/tweaks.txt AUTHORS COPYING README
%{_mandir}/man1/%{name}.1*
%{_datadir}/%{name}
%{_datadir}/pixmaps/%{name}-icon.png
%{_datadir}/psemu
%{_bindir}/%{name}
%{_libdir}/games/psemu
%{_datadir}/applications/%{name}.desktop

%changelog
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
