Name:           libewf
Version:        20140608
Release:        1%{?dist}
Summary:        Library for the Expert Witness Compression Format (EWF)

Group:          System Environment/Libraries
License:        LGPLv3+
URL:            http://sourceforge.net/projects/libewf/
#Source0:        http://libewf.googlecode.com/files/libewf-%{version}.tar.gz
Source0:        https://53efc0a7187d0baa489ee347026b8278fe4020f6.googledrive.com/host/0B3fBvzttpiiSMTdoaVExWWNsRjg/libewf-%{version}.tar.gz


BuildRequires:  fuse-devel
BuildRequires:  libuuid-devel
BuildRequires:  openssl-devel
BuildRequires:  zlib-devel
#Needed for mount.ewf(.py) support
BuildRequires:  python-devel


%description
Libewf is a library for support of the Expert Witness Compression Format (EWF),
it support both the SMART format (EWF-S01) and the EnCase format (EWF-E01). 
Libewf allows you to read and write media information within the EWF files.


%package -n     ewftools
Summary:        Utilities for the Expert Witness Compression Format (EWF)
Group:          Applications/System
Requires:       %{name} = %{version}-%{release}
Provides:       %{name}-tools = %{version}-%{release}
Obsoletes:      %{name}-tools <= %{version}-%{release}
Requires:       fuse-python >= 0.2
#Requires:       disktype

%description -n ewftools
Several tools for reading and writing EWF files.
It contains tools to acquire, verify and export EWF files.

%package        devel
Summary:        Development files for %{name}
Group:          Development/Libraries
Requires:       %{name} = %{version}-%{release}
Requires:       zlib-devel
Requires:       pkgconfig

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%setup -q


%build
%configure --disable-static \
  --enable-wide-character-type \
  --enable-python


# Remove rpath from libtool
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool

# clean unused-direct-shlib-dependencies
sed -i -e 's! -shared ! -Wl,--as-needed\0!g' libtool

make %{?_smp_mflags}


%install
make install DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p"
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'



%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig


%files
%doc AUTHORS COPYING NEWS
%{_libdir}/*.so.*

%files -n ewftools
%{_bindir}/ewf*
%{_mandir}/man1/*.gz
%{python_sitearch}/pyewf.so

%files devel
%{_includedir}/libewf.h
%{_includedir}/libewf/
%{_libdir}/*.so
%{_libdir}/pkgconfig/libewf.pc
%{_mandir}/man3/*.gz

%changelog
* Sat Aug 16 2014 Michal Ambroz <rebus AT seznam.cz> - 20140608-1
- Update to 20140608

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20130416-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20130416-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat May 18 2013 Nicolas Chauvet <kwizart@gmail.com> - 20130416-1
- Update to 20130416

* Thu Feb 28 2013 Nicolas Chauvet <kwizart@gmail.com> - 20130128-1
- Update to 20130128
- Switch to LGPLv3+
- Add BR fuse-devel
- Spec clean-up

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20100226-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20100226-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20100226-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20100226-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Jul 21 2010 David Malcolm <dmalcolm@redhat.com> - 20100226-2
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Mon Mar  8 2010 Nicolas Chauvet <kwizart@fedoraproject.org> - 20100226-1
- Update to 20100226
- Avoid version on python module.

* Fri Aug 21 2009 Tomas Mraz <tmraz@redhat.com> - 20080501-9
- rebuilt with new openssl

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20080501-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Jun 29 2009 kwizart < kwizart at gmail.com > - 20080501-7
- Switch to libuuid-devel usage over e2fsprogs-devel

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20080501-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Jan 15 2009 kwizart < kwizart at gmail.com > - 20080501-5
- Update mount_ewf to 20090113

* Sat Dec 27 2008 kwizart < kwizart at gmail.com > - 20080501-4
- Fix for python2.6

* Mon Sep 15 2008 kwizart < kwizart at gmail.com > - 20080501-3
- Update mount_ewf to 20080910
- Switch URL to sourceforge site

* Sat Jun  7 2008 kwizart < kwizart at gmail.com > - 20080501-2
- Update mount_ewf to 20080513

* Thu May  1 2008 kwizart < kwizart at gmail.com > - 20080501-1
- Update to 20080501 (bugfix)
- Patch for pkg-config was merged with this release
- Improve ewftools description.

* Tue Apr 29 2008 kwizart < kwizart at gmail.com > - 20080322-3
- Add disktype Requires for ewftools (required for mount.ewf support).
- Patch libewf.pc to export only the needed libs

* Tue Apr 22 2008 kwizart < kwizart at gmail.com > - 20080322-2
- Add support for mount.ewf with fuse-python

* Wed Mar 26 2008 kwizart < kwizart at gmail.com > - 20080322-1
- Update to 20080322 (Stable)
- License update: the BSD advertisement clause was removed.

* Mon Mar 17 2008 kwizart < kwizart at gmail.com > - 20080315-1
- Update to 20080315 (beta)
- Change versionning scheme (use date for version).

* Mon Nov  5 2007 kwizart < kwizart at gmail.com > - 0-2.20070512
- Update License to BSD with advertising

* Fri Nov  2 2007 kwizart < kwizart at gmail.com > - 0-1.20070512
- Initial package for Fedora

