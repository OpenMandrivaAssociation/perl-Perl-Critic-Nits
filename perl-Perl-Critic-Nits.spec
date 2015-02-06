%define upstream_name    Perl-Critic-Nits
%define upstream_version v1.0.0

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	5

Summary:	Policies of nits I like to pick
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Perl/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Perl::Critic)
BuildRequires:	perl(Test::More)
BuildArch:	noarch

%description
The included policy is:

* the
  Perl::Critic::Policy::ValuesAndExpressions::ProhibitAccessOfPrivateData
  manpage

  Prohibits direct access to a hash-based object's hash. [Severity: 5]

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
%doc Changes META.yml README
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Mon Apr 18 2011 Funda Wang <fwang@mandriva.org> 1.0.0-2mdv2011.0
+ Revision: 655612
- rebuild for updated spec-helper

* Fri Aug 27 2010 Jérôme Quelin <jquelin@mandriva.org> 1.0.0-1mdv2011.0
+ Revision: 573476
- import perl-Perl-Critic-Nits

