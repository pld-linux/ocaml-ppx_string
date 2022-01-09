#
# Conditional build:
%bcond_without	ocaml_opt	# native optimized binaries (bytecode is always built)

# not yet available on x32 (ocaml 4.02.1), update when upstream will support it
%ifnarch %{ix86} %{x8664} %{arm} aarch64 ppc sparc sparcv9
%undefine	with_ocaml_opt
%endif

Summary:	A ppx extension for string interpolation
Summary(pl.UTF-8):	Rozszerzenie ppx do interpolacji łańcuchów znaków
Name:		ocaml-ppx_string
Version:	0.14.1
Release:	1
License:	MIT
Group:		Libraries
#Source0Download: https://github.com/janestreet/ppx_string/tags
Source0:	https://github.com/janestreet/ppx_string/archive/v%{version}/ppx_string-%{version}.tar.gz
# Source0-md5:	5765a8ca47970b2290fbd7c5d589b449
URL:		https://github.com/janestreet/ppx_string
BuildRequires:	ocaml >= 1:4.04.2
BuildRequires:	ocaml-base-devel >= 0.14
BuildRequires:	ocaml-base-devel < 0.15
BuildRequires:	ocaml-dune >= 2.0.0
BuildRequires:	ocaml-ppx_base-devel >= 0.14
BuildRequires:	ocaml-ppx_base-devel < 0.15
BuildRequires:	ocaml-ppxlib-devel >= 0.11.0
BuildRequires:	ocaml-stdio-devel >= 0.14
BuildRequires:	ocaml-stdio-devel < 0.15
%requires_eq	ocaml-runtime
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		debug_package	%{nil}

%description
A ppx extension for string interpolation.

This package contains files needed to run bytecode executables using
ppx_string library.

%description -l pl.UTF-8
Rozszerzenie ppx do interpolacji łańcuchów znaków.

Pakiet ten zawiera binaria potrzebne do uruchamiania programów
używających biblioteki ppx_string.

%package devel
Summary:	A ppx extension for string interpolation - development part
Summary(pl.UTF-8):	Rozszerzenie ppx do interpolacji łańcuchów znaków - cześć programistyczna
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
%requires_eq	ocaml
Requires:	ocaml-base-devel >= 0.14
Requires:	ocaml-ppx_base-devel >= 0.14
Requires:	ocaml-ppxlib-devel >= 0.11.0
Requires:	ocaml-stdio-devel >= 0.14

%description devel
This package contains files needed to develop OCaml programs using
ppx_string library.

%description devel -l pl.UTF-8
Pakiet ten zawiera pliki niezbędne do tworzenia programów w OCamlu
używających biblioteki ppx_string.

%prep
%setup -q -n ppx_string-%{version}

%build
dune build --verbose

%install
rm -rf $RPM_BUILD_ROOT

dune install --destdir=$RPM_BUILD_ROOT

# sources
%{__rm} $RPM_BUILD_ROOT%{_libdir}/ocaml/ppx_string/*.ml
# packaged as %doc
%{__rm} -r $RPM_BUILD_ROOT%{_prefix}/doc/ppx_string

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE.md
%dir %{_libdir}/ocaml/ppx_string
%attr(755,root,root) %{_libdir}/ocaml/ppx_string/ppx.exe
%{_libdir}/ocaml/ppx_string/META
%{_libdir}/ocaml/ppx_string/*.cma
%if %{with ocaml_opt}
%attr(755,root,root) %{_libdir}/ocaml/ppx_string/*.cmxs
%endif

%files devel
%defattr(644,root,root,755)
%{_libdir}/ocaml/ppx_string/*.cmi
%{_libdir}/ocaml/ppx_string/*.cmt
%{_libdir}/ocaml/ppx_string/*.cmti
%{_libdir}/ocaml/ppx_string/*.mli
%if %{with ocaml_opt}
%{_libdir}/ocaml/ppx_string/ppx_string.a
%{_libdir}/ocaml/ppx_string/*.cmx
%{_libdir}/ocaml/ppx_string/*.cmxa
%endif
%{_libdir}/ocaml/ppx_string/dune-package
%{_libdir}/ocaml/ppx_string/opam
