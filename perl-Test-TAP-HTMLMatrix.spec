%define module   Test-TAP-HTMLMatrix
%define version    0.09
%define release    %mkrel 3

Name:       perl-%{module}
Version:    %{version}
Release:    %{release}
License:    GPL or Artistic
Group:      Development/Perl
Summary:    Creates colorful matrix of Test::Harness
Source:     http://www.cpan.org/modules/by-module/Test/%{module}-%{version}.tar.gz
Url:        http://search.cpan.org/dist/%{module}
BuildRequires: perl(Petal::Utils)
BuildRequires: perl(Petal)
BuildRequires: perl(Test::More)
BuildRequires: perl(Test::TAP::Model)
BuildRequires: perl(URI::file)
BuildRequires: perl(Module::Build::Compat)
BuildArch: noarch
BuildRoot:  %{_tmppath}/%{name}-%{version}

%description
This module is a wrapper for a template and some visualization classes,
that knows to take a the Test::TAP::Model manpage object, which
encapsulates test results, and produce a pretty html file.

%prep
%setup -q -n %{module}-%{version} 

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

