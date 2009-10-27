#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Test
%define	pnam	Refcount
Summary:	Test::Refcount - assert reference counts on objects
#Summary(pl.UTF-8):
Name:		perl-Test-Refcount
Version:	0.05
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://search.cpan.org/CPAN/authors/id/P/PE/PEVANS/Test-Refcount-%{version}.tar.gz
# Source0-md5:	657b089713b1283218590119faf12432
URL:		http://search.cpan.org/dist/Test-Refcount/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl(Devel::FindRef)
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
printed, using Marc Lehmann's Devel::FindRef module. See the examples
below for more information.

# %description -l pl.UTF-8
# TODO

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
%{perl_vendorlib}/Test/*.pm
%{_mandir}/man3/*
