%global tl_name pgfmath-xfp
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.0a
Release:	%{tl_revision}.1
Summary:	Define pgfmath functions using xfp
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/pgfmath-xfp
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/pgfmath-xfp.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/pgfmath-xfp.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/pgfmath-xfp.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package allows to define pgfmath functions that use the xfp fpu for
their calculations. The input arguments are parsed with pgfmath (while
the pgf-fpu is locally active), and the results are forwarded to xfp's
fpu for the function evaluation. The result of that calculation is then
parsed by pgfmath again (with the surrounding settings of pgfmath). This
way the functions should be usable in every pgfmath context, though
there is some overhead to this approach. The package is only meant as a
temporary stopgap until a more dedicated solution is available to use
xfp in pgf.

