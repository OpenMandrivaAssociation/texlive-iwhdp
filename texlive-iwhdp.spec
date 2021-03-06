Name:		texlive-iwhdp
Version:	0.50
Release:	2
Summary:	Halle Institute for Economic Research (IWH) Discussion Papers
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/iwhdp
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/iwhdp.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/iwhdp.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The document class is for creating Discussion Papers of the
Halle Institute for Economic Research (IWH) in Halle, Germany.
The class offers options for both English and German texts.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/iwhdp
%doc %{_texmfdistdir}/doc/latex/iwhdp

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
