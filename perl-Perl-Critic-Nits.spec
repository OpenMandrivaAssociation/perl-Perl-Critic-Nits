%define upstream_name    Perl-Critic-Nits
%define upstream_version v1.0.0

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 2

Summary:    Policies of nits I like to pick
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Perl/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Perl::Critic)
BuildRequires: perl(Test::More)
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

%description
The included policy is:

* the
  Perl::Critic::Policy::ValuesAndExpressions::ProhibitAccessOfPrivateData
  manpage

  Prohibits direct access to a hash-based object's hash. [Severity: 5]

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor

%make

%check
%make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes META.yml README
%{_mandir}/man3/*
%perl_vendorlib/*


