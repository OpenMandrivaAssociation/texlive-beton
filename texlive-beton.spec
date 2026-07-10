%global tl_name beton
%global tl_revision 79618

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Use Concrete fonts
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/beton
License:	lppl1.2
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/beton.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/beton.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/beton.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
Requires(pre):	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Typeset a LaTeX2e document with the Concrete fonts designed by Don Knuth
and used in his book "Concrete Mathematics".

%prep
%setup -q -c -a1 -a2
rm -rf tlpkg
if [ -d RELOC ]; then
	cp -a RELOC/. .
	rm -rf RELOC
fi

%build

%install
mkdir -p %{buildroot}%{_datadir}/texmf-dist
# Flat tlnet layout: tex/ doc/ source/ fonts/ ... -> texmf-dist/
if [ -d texmf-dist ]; then
	cp -a texmf-dist/. %{buildroot}%{_datadir}/texmf-dist/
elif [ -d texmf ]; then
	mkdir -p %{buildroot}%{_datadir}/texmf
	cp -a texmf/. %{buildroot}%{_datadir}/texmf/
else
	for d in * .[!.]* ..?*; do
		[ -e "$d" ] || continue
		case "$d" in tlpkg|RELOC) continue ;; esac
		cp -a "$d" %{buildroot}%{_datadir}/texmf-dist/
	done
fi
rm -rf %{buildroot}%{_datadir}/texmf-dist/tlpkg

%files
%dir %{_datadir}/texmf-dist
%dir %{_datadir}/texmf-dist/doc
%dir %{_datadir}/texmf-dist/source
%dir %{_datadir}/texmf-dist/tex
%dir %{_datadir}/texmf-dist/doc/latex
%dir %{_datadir}/texmf-dist/source/latex
%dir %{_datadir}/texmf-dist/tex/latex
%dir %{_datadir}/texmf-dist/doc/latex/beton
%dir %{_datadir}/texmf-dist/source/latex/beton
%dir %{_datadir}/texmf-dist/tex/latex/beton
%doc %{_datadir}/texmf-dist/doc/latex/beton/beton.pdf
%doc %{_datadir}/texmf-dist/doc/latex/beton/legal.txt
%doc %{_datadir}/texmf-dist/source/latex/beton/beton.dtx
%doc %{_datadir}/texmf-dist/source/latex/beton/beton.ins
%{_datadir}/texmf-dist/tex/latex/beton/beton.sty
