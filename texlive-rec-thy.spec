# revision 20909
# category Package
# catalog-ctan /macros/latex/contrib/rec-thy
# catalog-date 2011-01-02 11:52:10 +0100
# catalog-license lppl
# catalog-version 1.2
Name:		texlive-rec-thy
Version:	1.2
Release:	1
Summary:	Commands to typeset recursion theory papers
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/rec-thy
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/rec-thy.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/rec-thy.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
The package provides many macros to express standard notation
in recursion theory (otherwise known as computability theory).

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/rec-thy/rec-thy.sty
%doc %{_texmfdistdir}/doc/latex/rec-thy/README
%doc %{_texmfdistdir}/doc/latex/rec-thy/rec-thy.pdf
%doc %{_texmfdistdir}/doc/latex/rec-thy/rec-thy.tex
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
