# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/beton
# catalog-date 2009-09-24 15:05:48 +0200
# catalog-license lppl
# catalog-version undef
Name:		texlive-beton
Version:	20090924
Release:	1
Summary:	Use Concrete fonts
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/beton
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/beton.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/beton.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/beton.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
Typeset a LaTeX2e document with the Concrete fonts designed by
Don Knuth and used in his book "Concrete Mathematics".

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
%{_texmfdistdir}/tex/latex/beton/beton.sty
%doc %{_texmfdistdir}/doc/latex/beton/beton.pdf
%doc %{_texmfdistdir}/doc/latex/beton/legal.txt
#- source
%doc %{_texmfdistdir}/source/latex/beton/beton.dtx
%doc %{_texmfdistdir}/source/latex/beton/beton.ins
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
