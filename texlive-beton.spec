Name:		texlive-beton
Version:	15878
Release:	2
Summary:	Use Concrete fonts
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/beton
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/beton.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/beton.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/beton.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Typeset a LaTeX2e document with the Concrete fonts designed by
Don Knuth and used in his book "Concrete Mathematics".

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/beton/beton.sty
%doc %{_texmfdistdir}/doc/latex/beton/beton.pdf
%doc %{_texmfdistdir}/doc/latex/beton/legal.txt
#- source
%doc %{_texmfdistdir}/source/latex/beton/beton.dtx
%doc %{_texmfdistdir}/source/latex/beton/beton.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
