# Generated from faker-1.8.7.gem by gem2rpm -*- rpm-spec -*-
%global gem_name faker

Name: rubygem-%{gem_name}
Version: 1.8.7
Release: 1%{?dist}
Summary: Easily generate fake data
License: MIT
URL: https://github.com/stympy/faker
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby >= 2.1
BuildArch: noarch

%description
Faker, a port of Data::Faker from Perl, is used to easily generate fake data:
names, addresses, phone numbers, etc.


%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
gem unpack %{SOURCE0}

%setup -q -D -T -n  %{gem_name}-%{version}

gem spec %{SOURCE0} -l --ruby > %{gem_name}.gemspec

%build
# Create the gem as gem install only works on a gem file
gem build %{gem_name}.gemspec

# %%gem_install compiles any C extensions and installs the gem into ./%%gem_dir
# by default, so that we can move it into the buildroot in %%install
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/



%check
pushd .%{gem_instdir}
# Run the test suite.
popd

%files
%dir %{gem_instdir}
%license %{gem_instdir}/License.txt
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/CHANGELOG.md
%doc %{gem_instdir}/History.md
%doc %{gem_instdir}/README.md

%changelog
* Wed Mar 14 2018 Michal Ambroz <rebus at, seznam.cz> - 1.8.7-1
- Initial package
