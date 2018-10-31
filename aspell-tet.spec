%define _enable_debug_packages %{nil}
%define debug_package          %{nil}

%define src_ver 0.1.1
%define fname aspell5-%{languagecode}
%define aspell_ver 0.60
%define languageenglazy Tetum
%define languagecode tet
%define lc_ctype tet_TP

Summary:	%{languageenglazy} files for aspell
Name:		aspell-%{languagecode}
Version:	0.50.0
Release:	21
Group:		System/Internationalization
License:	GPLv2
Url:		http://aspell.net/
Source0:	http://ftp.gnu.org/gnu/aspell/dict/%{languagecode}/%fname-%{src_ver}.tar.bz2
ExcludeArch:	ia64

BuildRequires:	aspell >= %{aspell_ver}
Requires:	aspell >= %{aspell_ver}
# Mandriva Stuff
# there is not tet locale yet
#Requires:	locales-%{languagecode}
# aspell = 1, myspell = 2, lang-specific = 3
Provides:	enchant-dictionary = 1
Provides:	aspell-dictionary
Provides:	aspell-%{lc_ctype}
Provides:	spell-%{languagecode}
Autoreqprov:	no

%description
A %{languageenglazy} dictionary for use with aspell, a spelling checker.

%prep
%setup -qn %{fname}-%{src_ver}

%build
# don't use configure macro
./configure

%make

%install
%makeinstall_std

chmod 644 Copyright README doc/*

%files
%doc README Copyright doc/*
%doc doc/*
%{_libdir}/aspell-%{aspell_ver}/*

