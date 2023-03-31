Name:		texlive-substitutefont
Version:	32066
Release:	2
Summary:	Easy font substitution
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/substitutefont
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/substitutefont.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/substitutefont.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Many free fonts are extensions of a basic font family with new
glyphs or shapes. Such fonts may be given a new name due to
licence reasons or to the creator's preference. The package
facilitates the task of setting up a font family as substitute
for another one, using its \substitutefont command.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/substitutefont/substitutefont.sty
%doc %{_texmfdistdir}/doc/latex/substitutefont/README
%doc %{_texmfdistdir}/doc/latex/substitutefont/cyrillic-lm-lgc.pdf
%doc %{_texmfdistdir}/doc/latex/substitutefont/cyrillic-lm-lgc.tex
%doc %{_texmfdistdir}/doc/latex/substitutefont/cyrillic-paratype.pdf
%doc %{_texmfdistdir}/doc/latex/substitutefont/cyrillic-paratype.tex
%doc %{_texmfdistdir}/doc/latex/substitutefont/greek-palatino-didot.pdf
%doc %{_texmfdistdir}/doc/latex/substitutefont/greek-palatino-didot.tex
%doc %{_texmfdistdir}/doc/latex/substitutefont/greek-times-artemisia.pdf
%doc %{_texmfdistdir}/doc/latex/substitutefont/greek-times-artemisia.tex
%doc %{_texmfdistdir}/doc/latex/substitutefont/substitutefont-doc.html
%doc %{_texmfdistdir}/doc/latex/substitutefont/substitutefont-test.pdf
%doc %{_texmfdistdir}/doc/latex/substitutefont/substitutefont-test.tex
%doc %{_texmfdistdir}/doc/latex/substitutefont/substitutefont.sty.html

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
