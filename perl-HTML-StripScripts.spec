#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-HTML-StripScripts
Version  : 1.06
Release  : 23
URL      : https://cpan.metacpan.org/authors/id/D/DR/DRTECH/HTML-StripScripts-1.06.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/D/DR/DRTECH/HTML-StripScripts-1.06.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libh/libhtml-stripscripts-perl/libhtml-stripscripts-perl_1.06-1.debian.tar.xz
Summary  : 'Strip scripting constructs out of HTML'
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-HTML-StripScripts-license = %{version}-%{release}
Requires: perl-HTML-StripScripts-perl = %{version}-%{release}
BuildRequires : buildreq-cpan

%description
NAME
HTML::StripScripts - Strip scripting constructs out of HTML
SYNOPSIS
use HTML::StripScripts;

%package dev
Summary: dev components for the perl-HTML-StripScripts package.
Group: Development
Provides: perl-HTML-StripScripts-devel = %{version}-%{release}
Requires: perl-HTML-StripScripts = %{version}-%{release}

%description dev
dev components for the perl-HTML-StripScripts package.


%package license
Summary: license components for the perl-HTML-StripScripts package.
Group: Default

%description license
license components for the perl-HTML-StripScripts package.


%package perl
Summary: perl components for the perl-HTML-StripScripts package.
Group: Default
Requires: perl-HTML-StripScripts = %{version}-%{release}

%description perl
perl components for the perl-HTML-StripScripts package.


%prep
%setup -q -n HTML-StripScripts-1.06
cd %{_builddir}
tar xf %{_sourcedir}/libhtml-stripscripts-perl_1.06-1.debian.tar.xz
cd %{_builddir}/HTML-StripScripts-1.06
mkdir -p deblicense/
cp -r %{_builddir}/debian/* %{_builddir}/HTML-StripScripts-1.06/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-HTML-StripScripts
cp %{_builddir}/debian/copyright %{buildroot}/usr/share/package-licenses/perl-HTML-StripScripts/f6ee5333ac341a2dfe65f486a1da278a1e5d3597
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/HTML::StripScripts.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-HTML-StripScripts/f6ee5333ac341a2dfe65f486a1da278a1e5d3597

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.34.0/HTML/StripScripts.pm
