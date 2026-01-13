#
# Conditional build:
%bcond_without	tests	# do not perform "make test"

%define		pdir	Inline
%define		pnam	CPP
Summary:	Inline::CPP Perl module
Summary(cs.UTF-8):	Modul Inline::CPP pro Perl
Summary(da.UTF-8):	Perlmodul Inline::CPP
Summary(de.UTF-8):	Inline::CPP Perl Modul
Summary(es.UTF-8):	Módulo de Perl Inline::CPP
Summary(fr.UTF-8):	Module Perl Inline::CPP
Summary(it.UTF-8):	Modulo di Perl Inline::CPP
Summary(ja.UTF-8):	Inline::CPP Perl モジュール
Summary(ko.UTF-8):	Inline::CPP 펄 모줄
Summary(nb.UTF-8):	Perlmodul Inline::CPP
Summary(pl.UTF-8):	Moduł Perla Inline::CPP
Summary(pt.UTF-8):	Módulo de Perl Inline::CPP
Summary(pt_BR.UTF-8):	Módulo Perl Inline::CPP
Summary(ru.UTF-8):	Модуль для Perl Inline::CPP
Summary(sv.UTF-8):	Inline::CPP Perlmodul
Summary(uk.UTF-8):	Модуль для Perl Inline::CPP
Summary(zh_CN.UTF-8):	Inline::CPP Perl 模块
Name:		perl-Inline-CPP
Version:	0.34
Release:	2
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	365609155c8cbde9aee7307f408929a9
URL:		http://search.cpan.org/dist/Inline-CPP/
BuildRequires:	perl-Inline-C >= 0.43
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
Requires:	libstdc++-devel
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Inline::CPP - Write Perl subroutines and classes in C++.

%description -l pl.UTF-8
Moduł Inline::CPP - pozwalający na pisanie procedur i klas Perla w
C++.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL </dev/null \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

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
