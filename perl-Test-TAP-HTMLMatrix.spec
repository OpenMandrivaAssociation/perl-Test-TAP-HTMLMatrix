%define upstream_name    Test-TAP-HTMLMatrix
%define upstream_version 0.09

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	4

Summary:	Creates colorful matrix of Test::Harness
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Test/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Petal::Utils)
BuildRequires:	perl(Petal)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(Test::TAP::Model)
BuildRequires:	perl(URI::file)
BuildRequires:	perl(Module::Build::Compat)
BuildArch:	noarch

%description
This module is a wrapper for a template and some visualization classes,
that knows to take a the Test::TAP::Model manpage object, which
encapsulates test results, and produce a pretty html file.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std
rm -f %{buildroot}%{perl_vendorlib}/Test/TAP/example.pl

%files
%doc Changes README example.pl
%{_mandir}/man3/*
%{perl_vendorlib}/Test


%changelog
* Sat Aug 01 2009 Jérôme Quelin <jquelin@mandriva.org> 0.90.0-1mdv2010.0
+ Revision: 405597
- rebuild using %%perl_convert_version

* Tue Sep 09 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.09-3mdv2009.0
+ Revision: 283297
- examples belongs to documentation (fix conflict with perl-Test-TAP-Model)

* Fri Aug 08 2008 Thierry Vignaud <tvignaud@mandriva.com> 0.09-2mdv2009.0
+ Revision: 268744
- rebuild early 2009.0 package (before pixel changes)

* Sat May 31 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.09-1mdv2009.0
+ Revision: 213846
- import perl-Test-TAP-HTMLMatrix


* Sat May 31 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.09-1mdv2009.0
- first mdv release
