Summary: Command-line utility for grabbing/encoding data from audio CD
Name: abcde
Version: 2.2.0
Release: 2
Copyright: GPL
Group: Applications/Sound
Source: http://www.hispalinux.es/~data/files/%{name}_%{version}.orig.tar.gz
URL: http://www.hispalinux.es/~data/abcde.php
Buildroot: /tmp/%{name}-root
BuildArch: noarch
Packager: Jan "Yenya" Kasprzak <kas@fi.muni.cz>
Requires: cd-discid
Patch0: abcde-2.2.0-quote.diff
Patch1: abcde-2.2.0-editor.diff

%description
abcde is a frontend command-line utility (actually, a shell script) that
grabs tracks off a CD, encodes them to Ogg/Vorbis, MP3, FLAC, Ogg/Speex and/or
MPP/MP+(Musepack) format, and tags them, all in one go.

%prep 
%setup
%patch0 -p0
%patch1 -p0

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT

make DESTDIR=$RPM_BUILD_ROOT install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README examples/abcded examples/abcde.init
%config /etc/abcde.conf
/usr/bin/abcde
/usr/bin/cddb-tool
%{_mandir}/man1/abcde.1.gz
%{_mandir}/man1/cddb-tool.1.gz

%changelog
* Thu Feb 17 2005 Jan "Yenya" Kasprzak <kas@fi.muni.cz> 2.2.0-2
- Quoting patch ("expr: not a numeric expression" error when
	generating the playlist).
- Editor patch (vi is /bin/vi not /usr/bin/vi in Fedora; patched to use
	$PATH instead of hard-coded prefix).

* Thu Feb 17 2005 Jan "Yenya" Kasprzak <kas@fi.muni.cz> 2.2.0-1
- initial release
