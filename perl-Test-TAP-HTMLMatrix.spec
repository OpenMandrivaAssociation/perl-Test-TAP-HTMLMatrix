%define upstream_name    Test-TAP-HTMLMatrix
%define upstream_version 0.09

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    Creates colorful matrix of Test::Harness
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Test/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Petal::Utils)
BuildRequires: perl(Petal)
BuildRequires: perl(Test::More)
BuildRequires: perl(Test::TAP::Model)
BuildRequires: perl(URI::file)
BuildRequires: perl(Module::Build::Compat)
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

%description
This module is a wrapper for a template and some visualization classes,
that knows to take a the Test::TAP::Model manpage object, which
encapsulates test results, and produce a pretty html file.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf %{buildroot}
%makeinstall_std
rm -f %{buildroot}%{perl_vendorlib}/Test/TAP/example.pl

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes README example.pl
%{_mandir}/man3/*
%{perl_vendorlib}/Test
