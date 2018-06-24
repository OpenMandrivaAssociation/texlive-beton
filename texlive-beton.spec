# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/beton
# catalog-date 2009-09-24 15:05:48 +0200
# catalog-license lppl
# catalog-version undef
Name:		texlive-beton
Version:	20180303
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
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Tue Jan 03 2012 Paulo Andrade <pcpa@mandriva.com.br> 20090924-2
+ Revision: 749569
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 20090924-1
+ Revision: 717910
- texlive-beton
- texlive-beton
- texlive-beton
- texlive-beton
- texlive-beton

