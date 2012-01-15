#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Test
%define	pnam	Refcount
Summary:	Test::Refcount - assert reference counts on objects
Summary(pl.UTF-8):	Test::Refcount - testowanie liczników odwołań dla obiektów
Name:		perl-Test-Refcount
Version:	0.07
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Test/PEVANS/Test-Refcount-%{version}.tar.gz
# Source0-md5:	0a78c2f25e91c27baf0f71118a970245
URL:		http://search.cpan.org/dist/Test-Refcount/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Devel-FindRef
BuildRequires:	perl-Devel-Refcount
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Perl garbage collector uses simple reference counting during the
normal execution of a program. This means that cycles or unweakened
references in other parts of code can keep an object around for longer
than intended. To help avoid this problem, the reference count of a
new object from its class constructor ought to be 1. This way, the
caller can know the object will be properly DESTROYed when it drops
all of its references to it.

This module provides two test functions to help ensure this property
holds for an object class, so as to be polite to its callers.

If the assertion fails; that is, if the actual reference count is
different to what was expected, a trace of references to the object is
printed, using Marc Lehmann's Devel::FindRef module.

%description -l pl.UTF-8
Perlowy odśmiecacz (garbage collector) używa prostego zliczania
referencji podczas wykonywania programu. Oznacza to, że cykle lub
nie osłabione referencje w innych częściach kodu mogą utrzymać obiekt
na czas dłuższy, niż było to zamierzone. Aby pomóc w uniknięciu tego
problemu, liczba referencji nowego obiektu z konstruktora jego klasy
powinna wynosić 1. W ten sposób wywołujący może wiedzieć, że obiekt
będzie poprawnie zniszczony, kiedy pozbędzie się wszystkich
referencji.

Ten moduł udostępnia dwie funkcje testujące pomagające w upewnieniu
się co do tej właściwości klasy obiektu.

Jeśli zapewnienie nie powiedzie się, tzn. licznik referencji jest
różny od oczekiwanej wartości, wypisywany jest ślad referencji do
obiektu przy użyciu modułu Devel::FindRef Marca Lehmanna.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Build.PL \
	destdir=$RPM_BUILD_ROOT \
	installdirs=vendor
./Build

%{?with_tests:./Build test}

%install
rm -rf $RPM_BUILD_ROOT

./Build install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Test/Refcount.pm
%{_mandir}/man3/Test::Refcount.3pm*
