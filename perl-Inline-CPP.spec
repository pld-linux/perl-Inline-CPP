#
# Conditional build:
# _without_tests - do not perform "make test"
%include	/usr/lib/rpm/macros.perl
%define		pdir	Inline
%define		pname	CPP
Summary:	Inline::CPP Perl module
Summary(cs):	Modul Inline::CPP pro Perl
Summary(da):	Perlmodul Inline::CPP
Summary(de):	Inline::CPP Perl Modul
Summary(es):	Módulo de Perl Inline::CPP
Summary(fr):	Module Perl Inline::CPP
Summary(it):	Modulo di Perl Inline::CPP
Summary(ja):	Inline::CPP Perl ¥â¥¸¥å¡¼¥ë
Summary(ko):	Inline::CPP ÆÞ ¸ðÁÙ
Summary(no):	Perlmodul Inline::CPP
Summary(pl):	Modu³ Perla Inline::CPP
Summary(pt):	Módulo de Perl Inline::CPP
Summary(pt_BR):	Módulo Perl Inline::CPP
Summary(ru):	íÏÄÕÌØ ÄÌÑ Perl Inline::CPP
Summary(sv):	Inline::CPP Perlmodul
Summary(uk):	íÏÄÕÌØ ÄÌÑ Perl Inline::CPP
Summary(zh_CN):	Inline::CPP Perl Ä£¿é
Name:		perl-Inline-CPP
Version:	0.24
Release:	3
License:	Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pname}-%{version}.tar.gz
# Source0-md5:	7d7b51fef2ecb2082257dcc585621a96
BuildRequires:	perl-devel >= 5.6
BuildRequires:	perl-Inline-C >= 0.43
BuildRequires:	rpm-perlprov >= 4.1-13
Requires:	libstdc++-devel
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Inline::CPP - Write Perl subroutines and classes in C++.

%description -l pl
Modu³ Inline::CPP - pozwalaj±cy na pisanie procedur i klas Perla w
C++.

%prep
%setup -q -n %{pdir}-%{pname}-%{version}

%build
%{__perl} Makefile.PL </dev/null \
	INSTALLDIRS=vendor
%{__make}
%{!?_without_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README TESTED
%{perl_vendorlib}/Inline/CPP.pm
%{perl_vendorlib}/Inline/CPP
%{_mandir}/man3/*
