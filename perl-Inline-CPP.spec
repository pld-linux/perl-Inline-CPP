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
Summary(es):	M�dulo de Perl Inline::CPP
Summary(fr):	Module Perl Inline::CPP
Summary(it):	Modulo di Perl Inline::CPP
Summary(ja):	Inline::CPP Perl �⥸�塼��
Summary(ko):	Inline::CPP �� ����
Summary(no):	Perlmodul Inline::CPP
Summary(pl):	Modu� Perla Inline::CPP
Summary(pt):	M�dulo de Perl Inline::CPP
Summary(pt_BR):	M�dulo Perl Inline::CPP
Summary(ru):	������ ��� Perl Inline::CPP
Summary(sv):	Inline::CPP Perlmodul
Summary(uk):	������ ��� Perl Inline::CPP
Summary(zh_CN):	Inline::CPP Perl ģ��
Name:		perl-Inline-CPP
Version:	0.24
Release:	1
License:	Artistic
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pname}-%{version}.tar.gz
BuildRequires:	perl >= 5.6
BuildRequires:	perl-Inline-C >= 0.42
BuildRequires:	rpm-perlprov >= 3.0.3-16
Requires:	libstdc++-devel
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Inline::CPP - Write Perl subroutines and classes in C++.

%description -l pl
Modu� Inline::CPP - pozwalaj�cy na pisanie procedur i klas Perla w
C++.

%prep
%setup -q -n %{pdir}-%{pname}-%{version}

%build
perl Makefile.PL </dev/null
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
%{perl_sitelib}/Inline/CPP.pm
%{perl_sitelib}/Inline/CPP
%{_mandir}/man3/*
