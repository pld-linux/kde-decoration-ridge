%define		_decoration 	ridge
Summary:	Kwin decoration - %{_decoration}
Summary(pl.UTF-8):	Dekoracja kwin - %{_decoration}
Name:		kde-decoration-%{_decoration}
Version:	0.3.1
Release:	2
License:	GPL
Group:		Themes
Source0:	http://kde-look.org/content/files/10429-%{_decoration}-%{version}.tar.bz2
# Source0-md5:	b5aa08aec4a278d34ad04d36f6f14d43
URL:		http://kde-look.org/content/show.php?content=10429
BuildRequires:	autoconf
BuildRequires:	unsermake
BuildRequires:	automake
BuildRequires:	kdelibs-devel >= 9:3.2.0
BuildRequires:	kdebase-desktop-libs >= 9:3.2.0
BuildRequires:	rpmbuild(macros) >= 1.129
Requires:	kdebase-desktop-libs >= 9:3.2.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A kwin window decoration with flat, square buttons.

%description -l pl.UTF-8
Dekoracja kwin z płaskimi, kwadratowymi przyciskami.

%package -n kde-colorscheme-%{_decoration}
Summary:	Color scheme for KDE style - %{_decoration}
Summary(pl.UTF-8):	Schemat kolorów do stylu KDE - %{_decoration}
Group:		Themes
Requires:	kdebase-core

%description -n kde-colorscheme-%{_decoration}
A gray colorscheme with blue window title and light yellow selection
background.

%description -n kde-colorscheme-%{_decoration} -l pl.UTF-8
Szary schemat kolorów z niebieskim tytułem okna oraz żółtym tłem
zaznaczenia.

%prep
%setup -q -n %{_decoration}-%{version}

%build
cp -f /usr/share/automake/config.sub admin
export UNSERMAKE=/usr/share/unsermake/unsermake
%{__make} -f Makefile.dist

%configure \
	--with-qt-libraries=%{_libdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir="%{_kdedocdir}"

%clean
rm -rf $RPM_BUILD_ROOT

%files -n kde-colorscheme-%{_decoration}
%defattr(644,root,root,755)
%{_datadir}/apps/kdisplay/color-schemes/*.kcsrc

%files
%defattr(644,root,root,755)
%{_libdir}/kde3/kwin*.la
%attr(755,root,root) %{_libdir}/kde3/kwin*.so
%{_datadir}/apps/kwin/*.desktop
