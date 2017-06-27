%global         gituser         decalage2
%global         gitname         olefile
# v0.44
#%global         commit          3397e5ea9172c26fca35fb45175fde170c277e3d
# v0.45dev1
%global         commit          53c619f4c68ee226b57c07a3956efcc814a548f0
%global         shortcommit     %(c=%{commit}; echo ${c:0:7})

%global         sum             Tools to analyze Microsoft OLE2 files



Name:           python-%{gitname}
Version:        0.45
Release:        0.1.git%{shortcommit}%{?dist}
Summary:        %{sum}

License:        BSD
URL:            https://www.decalage.info/olefile
# URL:          https://github.com/decalage2/olefile
#Source0:       https://github.com/%{gituser}/%{gitname}/archive/v%{version}/%{gitname}-%{version}.tar.gz
Source0:        https://github.com/%{gituser}/%{gitname}/archive/%{commit}/%{name}-%{version}-%{shortcommit}.tar.gz
#Patch0:        %{name}-thirdparty.patch


BuildArch:      noarch
BuildRequires:  python2-devel python3-devel
# needed to generate documentation man-page
BuildRequires:  python-sphinx


%description
The olefile is a Python package from Philippe Lagadec (decalage2)
to parse, read and write Microsoft OLE2 files (also called Structured
Storage, Compound File Binary Format or Compound Document File
Format), such as Microsoft Office 97-2003 documents, vbaProject.bin
in MS Office 2007+ files, Image Composer and FlashPix files, Outlook
messages, StickyNotes, several Microscopy file formats,
McAfee antivirus quarantine files, etc.
See http://www.decalage.info/olefile for more info.



%package -n python2-%{gitname}
Summary:        %{sum}
%{?python_provide:%python_provide python2-%{gitname}}

%description -n python2-%{gitname}
The olefile is a Python package from Philippe Lagadec (decalage2)
to parse, read and write Microsoft OLE2 files (also called Structured
Storage, Compound File Binary Format or Compound Document File
Format), such as Microsoft Office 97-2003 documents, vbaProject.bin
in MS Office 2007+ files, Image Composer and FlashPix files, Outlook
messages, StickyNotes, several Microscopy file formats,
McAfee antivirus quarantine files, etc.
See http://www.decalage.info/olefile for more info.



%package -n python3-%{gitname}
Summary:        %{sum}
%{?python_provide:%python_provide python3-%{gitname}}

%description -n python3-%{gitname}
The olefile is a Python package from Philippe Lagadec (decalage2)
to parse, read and write Microsoft OLE2 files (also called Structured
Storage, Compound File Binary Format or Compound Document File
Format), such as Microsoft Office 97-2003 documents, vbaProject.bin
in MS Office 2007+ files, Image Composer and FlashPix files, Outlook
messages, StickyNotes, several Microscopy file formats,
McAfee antivirus quarantine files, etc.
See http://www.decalage.info/olefile for more info.



%package -n python-%{gitname}-doc
%{?python_provide:%python_provide python2-%{gitname}-doc}
%{?python_provide:%python_provide python3-%{gitname}-doc}
Summary:        %{sum}
%description -n python-%{gitname}-doc


%prep
#autosetup -n %{gitname}-%{version}
%autosetup -n %{gitname}-%{commit}

%build
%py2_build
pushd doc
make man
popd
%py3_build

%install
# Must do the python2 install first because the scripts in /usr/bin are
# overwritten with every setup.py install, and in general we want the
# python3 version to be the default.
%py2_install
%py3_install

install -D -m644 doc/_build/man/olefile.1 %{buildroot}%{_mandir}/man1/%{name}.1

%check
%{__python2} setup.py test
%{__python3} setup.py test

# Note that there is no %%files section for the unversioned python module if we are building for several python runtimes
%files -n python2-%{gitname}
%license olefile/LICENSE.txt
%{python2_sitelib}/*


%files -n python3-%{gitname}
%license olefile/LICENSE.txt
%doc olefile/README.html olefile/README.rst
%{python3_sitelib}/*
%{_mandir}/man1/%{name}.1*



%changelog
* Thu Jun 15 2017 Michal Ambroz <rebus at, seznam.cz> 0.45-0.1.dev1.53c619f4
- initial version