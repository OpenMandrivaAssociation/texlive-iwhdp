Name:		texlive-iwhdp
Version:	37552
Release:	2
Summary:	Halle Institute for Economic Research (IWH) Discussion Papers
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/iwhdp
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/iwhdp.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/iwhdp.doc.r%{version}.tar.xz
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
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
