%include	/usr/lib/rpm/macros.perl
%define	pdir	Inline
%define	pname	CPP
Summary:	Inline::CPP perl module
Summary(pl):	Modu³ perla Inline::CPP
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
Modu³ Inline::CPP - pozwalaj±cy na pisanie procedur i klas Perla w
C++.

%prep
%setup -q -n %{pdir}-%{pname}-%{version}

%build
perl Makefile.PL </dev/null
%{__make}

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
