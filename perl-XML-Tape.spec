#
# Conditional build:
%bcond_without	autodeps	# don't BR packages needed only for resolving deps
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	XML
%define		pnam	Tape
Summary:	XML::Tape - module for the manipulation of XMLtape archives
Summary(pl):	XML::Tape - modu³ do obróbki archiwów XMLtape
Name:		perl-XML-Tape
Version:	0.22
Release:	1
License:	unknown
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	50be9e231bd225b850fe6ca7f0c55210
URL:		http://search.cpan.org/dist/XML-Tape/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with autodeps} || %{with tests}
BuildRequires:	perl-DB_File
BuildRequires:	perl-Digest-MD5
BuildRequires:	perl-XML-LibXML
BuildRequires:	perl-XML-Parser
BuildRequires:	perl-XML-SAX-Writer
BuildRequires:	perl(HTTP::OAI)
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The XMLtape provides a write-once/read-many XML wrapper for a
collection of XML documents. The wrapper provides an easy storage
format for big collections of XML files which can be processed with
off the shelf tools and validated against a schema. The XMLtape is
typically used in digital preservation projects.

%description -l pl
Modu³ XML::Tape to opakowanie XML jednokrotnego zapisu i wielokrotnego
odczytu dla zbioru dokumentów XML. Udostêpnia ³atwy format
przechowywania du¿ych zbiorów plików XML, które mog± byæ przetwarzane
przy u¿yciu odpowiednich narzêdzi i sprawdzane pod k±tem zgodno¶ci ze
schematem. XMLtape zwykle jest u¿ywany przy projektach cyfrowych
zabezpieczeñ.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%attr(755,root,root) %{_bindir}/xmltape
%attr(755,root,root) %{_bindir}/xmlindex
%{perl_vendorlib}/XML/Tape.pm
%dir %{perl_vendorlib}/XML/Tape
%{perl_vendorlib}/XML/Tape/Index.pm
%{_mandir}/man3/*
