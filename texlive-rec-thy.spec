# revision 27225
# category Package
# catalog-ctan /macros/latex/contrib/rec-thy
# catalog-date 2012-06-21 10:44:34 +0200
# catalog-license pd
# catalog-version 1.3
Name:		texlive-rec-thy
Version:	2.4.1
Release:	1
Summary:	Commands to typeset recursion theory papers
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/rec-thy
License:	PD
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/rec-thy.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/rec-thy.doc.tar.xz
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
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Wed Aug 08 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.3-1
+ Revision: 812817
- Update to latest release.

* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.2-2
+ Revision: 755648
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.2-1
+ Revision: 719439
- texlive-rec-thy
- texlive-rec-thy
- texlive-rec-thy
- texlive-rec-thy

