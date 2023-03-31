Name:		texlive-rec-thy
Version:	63982
Release:	2
Summary:	Commands to typeset recursion theory papers
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/rec-thy
License:	PD
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/rec-thy.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/rec-thy.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides many macros to express standard notation
in recursion theory (otherwise known as computability theory).

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/rec-thy/rec-thy.sty
%doc %{_texmfdistdir}/doc/latex/rec-thy/README
%doc %{_texmfdistdir}/doc/latex/rec-thy/rec-thy.pdf
%doc %{_texmfdistdir}/doc/latex/rec-thy/rec-thy.tex

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
