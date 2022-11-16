Name:		texlive-pgfmath-xfp
Version:	59268
Release:	1
Summary:	Define pgfmath functions using xfp
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/pgfmath-xfp
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pgfmath-xfp.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pgfmath-xfp.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pgfmath-xfp.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package allows to define pgfmath functions that use the
xfp fpu for their calculations. The input arguments are parsed
with pgfmath (while the pgf-fpu is locally active), and the
results are forwarded to xfp's fpu for the function evaluation.
The result of that calculation is then parsed by pgfmath again
(with the surrounding settings of pgfmath). This way the
functions should be usable in every pgfmath context, though
there is some overhead to this approach. The package is only
meant as a temporary stopgap until a more dedicated solution is
available to use xfp in pgf.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/pgfmath-xfp
%{_texmfdistdir}/tex/latex/pgfmath-xfp
%doc %{_texmfdistdir}/doc/latex/pgfmath-xfp

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
