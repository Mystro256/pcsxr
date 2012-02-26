%define svnversion 75200
Name:           pcsxr
Version:        1.9.92
Release:        1.20120219svn%{svnversion}%{?dist}
Summary:        A plugin based PlayStation (PSX) emulator with high compatibility

#All is GPLv2+ except:
# SOURCE/plugins/gxvideo/* includes some GPLv3+
# SOURCE/libpcsxcore/coff.h is BSD License (no advertising)
# SOURCE/libpcsxcore/sjisfont.h is Public Domain
# SOURCE/libpcsxcore/psemu_plugin_defs.h is Public Domain
License:        GPLv3+ and BSD and Public Domain
Url:            http://pcsxr.codeplex.com/
#The source can be downloaded here:
#http://pcsxr.codeplex.com/SourceControl/changeset/changes/75200
Source:         %{name}-%{svnversion}.zip

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
%doc doc/keys.txt doc/tweaks.txt AUTHORS COPYING README NEWS
%{_mandir}/man1/%{name}.1*
%{_datadir}/%{name}
%{_datadir}/pixmaps/%{name}-icon.png
%{_datadir}/psemu
%{_bindir}/%{name}
%{_libdir}/games/psemu
%{_datadir}/applications/%{name}.desktop

%post
/bin/touch --no-create %{_datadir}/icons/hicolor &>/dev/null || :

%postun
if [ $1 -eq 0 ] ; then
    /bin/touch --no-create %{_datadir}/icons/hicolor &>/dev/null
    /usr/bin/gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :
fi

%posttrans
/usr/bin/gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :

%changelog
* Sun Feb 19 2011 Jeremy Newton <alexjnewt@hotmail.com> - 1.9.92-1.20120219svn75200
- Updated to new SVN checkout version

* Sun Feb 19 2011 Jeremy Newton <alexjnewt@hotmail.com> - 1.9.92-1.20120219svn75156
- Updated to new SVN checkout version
- Added svn macro
- Removed incorrect disabling of opengl for 64bit

* Wed Feb 8 2011 Jeremy Newton <alexjnewt@hotmail.com> - 1.9.92-3.20120128svn73976
- Minor source change for convenience.

* Wed Feb 8 2011 Jeremy Newton <alexjnewt@hotmail.com> - 1.9.92-2.20120128svn73976
- Fixed and optimized source files for size and convenience.
- Added missing file in license breakdown

* Sat Jan 28 2011 Jeremy Newton <alexjnewt@hotmail.com> - 1.9.92-1.20120128svn73976
- Fixed version number to be more specific
- Fixed inproper license
- Trimmed down the source, removed non-linux code

* Sat Jan 28 2011 Jeremy Newton <alexjnewt@hotmail.com> - 1.9.92-1.20120128svn
- Initial package SPEC created
