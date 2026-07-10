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
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Typeset a LaTeX2e document with the Concrete fonts designed by Don Knuth
and used in his book "Concrete Mathematics".

