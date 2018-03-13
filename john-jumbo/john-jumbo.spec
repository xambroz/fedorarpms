%global           jumbo_version 1
Summary:          John the Ripper password cracker
Name:             john-jumbo
Version:          1.8.0
Release:          jumbo.%{jumbo_version}.2%{?dist}

URL:              http://www.openwall.com/john
License:          GPLv2
Group:            Applications/System
Source0:          http://www.openwall.com/john/j/john-%{version}-jumbo-%{jumbo_version}.tar.xz
Source1:          http://www.openwall.com/john/j/john-%{version}-jumbo-%{jumbo_version}.tar.xz.sign
Patch0:           john-jumbo-inlines.patch
#Patch3:           http://www.openwall.com/john/g/john-%{version}-jumbo-%{jumbo_version}.diff.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root
Requires:         john = %{version}

Buildrequires:    nss-devel
Buildrequires:    krb5-devel
Buildrequires:    gmp-devel

Buildrequires:    gcc
Buildrequires:    autoconf
#For optional AES-NI support
Buildrequires:    yasm

%if 0%{?fedora} <= 25
Buildrequires:    openssl-devel
%else
Buildrequires:    compat-openssl10-devel
%endif


%description
John the Ripper is a fast password cracker. Its primary purpose is to
detect weak Unix passwords, but a number of other hash types are
supported as well.
This package includes the john added with the jumbo %{jumbo_version} patch to
add many more types of the passwords.

%prep
%setup -q -n john-%{version}-jumbo-%{jumbo_version}
#rm doc/INSTALL

%patch0 -p1 -b .inlines
#%patch3 -p1 -b .jumbo
chmod 0644 doc/*
sed -i 's#\$JOHN/john.conf#%{_sysconfdir}/%{name}/john.conf#' src/params.h
chmod -R u+r src

%build
cd src
export CFLAGS="-DJOHN_SYSTEMWIDE=1"
#%%configure
#./configure --build=x86_64-redhat-linux-gnu --host=x86_64-redhat-linux-gnu --program-prefix= --disable-dependency-tracking --prefix=/usr --exec-prefix=/usr --bindir=/usr/bin --sbindir=/usr/sbin --sysconfdir=/etc --datadir=/usr/share --includedir=/usr/include --libdir=/usr/lib64 --libexecdir=/usr/libexec --localstatedir=/var --sharedstatedir=/var/lib --mandir=/usr/share/man --infodir=/usr/share/info
./configure
make



%install
rm -rf %{buildroot}
install -d -m 755 %{buildroot}%{_bindir}
install -m 755 run/john %{buildroot}%{_bindir}/%{name}
install -d -m 755 %{buildroot}%{_libexecdir}/john
install -m 755 run/*.pl %{buildroot}%{_bindir}/
install -m 755 run/*.py %{buildroot}%{_bindir}/
install -m 755 run/*.rb %{buildroot}%{_bindir}/
install -m 755 run/stats %{buildroot}%{_libexecdir}/john/
install -m 755 run/*.conf %{buildroot}%{_libexecdir}/john/

for LINK in `find run/ -type l` ; do
	LINKNAME=`basename $LINK`
	pushd %{buildroot}%{_bindir}
	ln -s %{name} "$LINKNAME"
	popd
done

#Remove files conflicting with john package
rm -f %{buildroot}%{_bindir}/unafs
rm -f %{buildroot}%{_bindir}/unique
rm -f %{buildroot}%{_bindir}/unshadow


#perl-SHA is not in Fedora at the moment
#rm %{buildroot}%{_libexecdir}/john/sha-test.pl



%files
%doc doc/*
%license
%{_bindir}/*
%{_libexecdir}/john/stats
%{_libexecdir}/john/dumb16.conf
%{_libexecdir}/john/dumb32.conf
%{_libexecdir}/john/dynamic.conf
%{_libexecdir}/john/dynamic_flat_sse_formats.conf
%{_libexecdir}/john/john.conf
%{_libexecdir}/john/john.local.conf
%{_libexecdir}/john/korelogic.conf
%{_libexecdir}/john/regex_alphabets.conf
%{_libexecdir}/john/repeats16.conf
%{_libexecdir}/john/repeats32.conf


%changelog
* Tue Feb 21 2017 Michal Ambroz <rebus AT seznam.cz> - 1.8.0-jumbo.1.2
- build with compat openssl for FC26

* Tue Feb 21 2017 Michal Ambroz <rebus AT seznam.cz> - 1.8.0-jumbo.1.1
- 1.8.0 + jumbo 1 patch

* Wed Nov 09 2011 Michal Ambroz <rebus AT seznam.cz> - 1.7.9-jumbo.7.1
- 1.7.9 + jumbo 7 patch

* Wed Nov 09 2011 Michal Ambroz <rebus AT seznam.cz> - 1.7.8-jumbo.8.1
- 1.7.8 + jumbo 8 patch

* Wed Sep 14 2011 Michal Ambroz <rebus AT seznam.cz> - 1.7.8-jumbo.5.1
- 1.7.8 + jumbo 5 patch

* Mon Jul 25 2011 Michal Ambroz <rebus AT seznam.cz> - 1.7.8-jumbo.4.1
- 1.7.8 + jumbo 4 patch

* Mon Jun 06 2011 Michal Ambroz <rebus AT seznam.cz> - 1.7.7-jumbo.6.1
- 1.7.7 + jumbo 6 patch

* Wed Feb 09 2011 Michal Ambroz <rebus AT seznam.cz> - 1.7.6-jumbo.11.3
- Jumbo11 patch

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Aug 23 2010 Till Maas <opensource@till.name> - 1.7.6-1
- Update to latest release (RH #626537)
- use less regexes in %%files

* Mon Jan 18 2010 Till Maas <opensource@till.name> - 1.7.3.4-1
- Update to new release
- fix Source0
- add missing -m parameters to install
- set LDFLAGS to RPM_OPT_FLAGS for non mmx build
- add signature as Source1

* Fri Jan 08 2010 Till Maas <opensource@till.name> - 1.7.0.2-9
- Use %%global instead of %%global

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.0.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.0.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Feb 20 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1.7.0.2-6
- Autorebuild for GCC 4.3

* Thu Aug 23 2007 Till Maas <opensource till name> - 1.7.0.2-5
- update License Tag
- bump release for rebuild

* Sat May 05 2007 Till Maas <opensouce till name> - 1.7.0.2-4
- use correct target for ppc64

* Tue Feb 27 2007 Till Maas <opensource till name> - 1.7.0.2-3
- fixing wrong characters in specfile
- https://bugzilla.redhat.com/bugzilla/attachment.cgi?id=148873&action=view

* Wed Jan 10 2007 Till Maas <opensource till name> - 1.7.0.2-2
- no mmx version for x86_64 since it is 32bit and does not build

* Tue Jan 09 2007 Till Maas <opensource till name> - 1.7.0.2-1
- prevent stripping in Makefile to get non-empty debuginfo
- version bump
- build mmx and fallback version

* Mon Oct 09 2006 Jeremy Katz <katzj@redhat.com> - 1.6-5
- FC6 Rebuild

* Sun May 22 2005 Jeremy Katz <katzj@redhat.com> - 1.6-4
- rebuild on all arches

* Thu Apr  7 2005 Michael Schwendt <mschwendt[AT]users.sf.net>
- rebuilt

* Fri Apr 25 2003 Marius Johndal <mariuslj at ifi.uio.no> 0:1.6-0.fdr.2
- Added epoch.
- Modified makefile patch to honour %%optflags.
- setup -q.
- Added full URL of source.

* Thu Mar  6 2003 Marius Johndal <mariuslj at ifi.uio.no> 1.6-0.fdr.1
- Initial Fedora RPM release.

* Sat Dec  7 2002 Marius Johndal <mariuslj at ifi.uio.no>
- Misc. RH 8.0 changes.

* Mon Dec  2 2002 Guillaume Rousse <g.rousse@linux-mandrake.com> 1.6-2mdk
- config file in /etc
- fix configuration problem

* Mon Sep 16 2002 Guillaume Rousse <g.rousse@linux-mandrake.com> 1.6-1mdk
- first mdk version