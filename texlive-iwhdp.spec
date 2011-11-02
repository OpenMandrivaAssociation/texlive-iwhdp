Name:		texlive-iwhdp
Version:	0.24
Release:	1
Summary:	Halle Institute for Economic Research (IWH) Discussion Papers
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/iwhdp
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/iwhdp.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/iwhdp.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
The document class is for creating Discussion Papers of the
Halle Institute for Economic Research (IWH) in Halle, Germany.
The class offers options for both English and German texts.

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
%{_texmfdistdir}/tex/latex/iwhdp/iwhdp.cls
%doc %{_texmfdistdir}/doc/latex/iwhdp/Anleitung.bib
%doc %{_texmfdistdir}/doc/latex/iwhdp/Anleitung.tex
%doc %{_texmfdistdir}/doc/latex/iwhdp/README
%doc %{_texmfdistdir}/doc/latex/iwhdp/anleitung.pdf
%doc %{_texmfdistdir}/doc/latex/iwhdp/iwhdp_paper.bib
%doc %{_texmfdistdir}/doc/latex/iwhdp/iwhdp_paper.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
