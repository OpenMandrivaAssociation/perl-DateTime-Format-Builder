%define upstream_name    DateTime-Format-Builder
%define upstream_version 0.81

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	7

Summary:	Create DateTime parser classes and objects
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/DateTime/DateTime-Format-Builder-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Class::Factory::Util)
BuildRequires:	perl(DateTime)
BuildRequires:	perl(DateTime::Format::Strptime)
BuildRequires:	perl(Module::Build)
BuildRequires:	perl(Params::Validate)
BuildRequires:	perl(Task::Weaken)
BuildRequires:	perl(Module::Build::Compat)
# This dependency is missing so we specify it explicitly.
Requires:	perl(Class::Factory::Util)
BuildArch:	noarch

%description
This module understands the formats used by MySQL for its DATE, DATETIME,
TIME, and TIMESTAMP data types. It can be used to parse these formats in
order to create DateTime objects, and it can take a DateTime object and
produce a string representing it in the MySQL format.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes README
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Sat Apr 23 2011 Funda Wang <fwang@mandriva.org> 0.800.0-3mdv2011.0
+ Revision: 656905
- rebuild for updated spec-helper

* Sat Dec 04 2010 Shlomi Fish <shlomif@mandriva.org> 0.800.0-2mdv2011.0
+ Revision: 609257
- Add Requires for Class::Factory::Util (it was missing for some reason)

* Mon Mar 15 2010 Jérôme Quelin <jquelin@mandriva.org> 0.800.0-1mdv2011.0
+ Revision: 519950
- update to 0.80

* Sun Nov 29 2009 Jérôme Quelin <jquelin@mandriva.org> 0.790.100-1mdv2010.1
+ Revision: 471226
- import perl-DateTime-Format-Builder


* Sun Nov 29 2009 cpan2dist 0.7901-1mdv
- initial mdv release, generated with cpan2dist

