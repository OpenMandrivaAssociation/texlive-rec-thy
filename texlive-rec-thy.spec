%global tl_name rec-thy
%global tl_revision 76924

Name:		texlive-%{tl_name}
Epoch:		1
Version:	4.5
Release:	%{tl_revision}.1
Summary:	Commands to typeset recursion theory papers
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/rec-thy
License:	pd
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/rec-thy.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/rec-thy.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package is designed to help mathematicians publishing papers in the
area of recursion theory (aka Computability Theory) easily use standard
notation. This includes easy commands to denote Turing reductions,
Turing functionals, c.e. sets, stagewise computations, forcing and
syntactic classes.

