Summary:	Print dialog and printer manager for Xfce
Summary(pl.UTF-8):	Okno dialogowe wydruku i zarządca drukarek dla Xfce
Name:		xfprint
Version:	4.6.0
Release:	1
License:	GPL v2
Group:		X11/Applications
Source0:	http://www.xfce.org/archive/xfce-%{version}/src/%{name}-%{version}.tar.bz2
# Source0-md5:	cf2e0de43367da6a0ef7eeef04876281
Patch0:		%{name}-bsdlpr.patch
URL:		http://www.xfce.org/projects/xfprint/
BuildRequires:	a2ps-devel
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	cups-devel
BuildRequires:	gettext-devel
BuildRequires:	gtk+2-devel >= 2:2.10.6
BuildRequires:	gtk-doc >= 1.7
BuildRequires:	intltool
BuildRequires:	libtool
BuildRequires:	libxfce4util-devel >= %{version}
BuildRequires:	libxfcegui4-devel >= %{version}
BuildRequires:	openssl-devel >= 0.9.7d
BuildRequires:	pkgconfig >= 1:0.9.0
BuildRequires:	rpmbuild(macros) >= 1.311
BuildRequires:	xfce4-dev-tools >= 4.6.0
BuildRequires:	xfconf-devel >= %{version}
Requires(post,postun):	gtk+2
Requires(post,postun):	hicolor-icon-theme
Requires:	%{name}-print-backend = %{version}-%{release}
Requires:	a2ps
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Xfprint contains a print dialog and a printer manager for the Xfce
Desktop Environment.

%description -l pl.UTF-8
Xfprint zawiera okno dialogowe wydruku i zarządcę drukarek dla
środowiska Xfce.

%package apidocs
Summary:	xfprint API documentation
Summary(pl.UTF-8):	Dokumentacja API xfprint
Group:		Documentation
Requires:	gtk-doc-common

%description apidocs
xfprint API documentation.

%description apidocs -l pl.UTF-8
Dokumentacja API xfprint.

%package cups
Summary:	CUPS plugin for xfprint
Summary(pl.UTF-8):	Wtyczka CUPS dla xfprint
Group:		X11/Applications
Requires:	%{name} = %{version}-%{release}
Provides:	%{name}-print-backend = %{version}-%{release}

%description cups
This package contains plugin for xfprint allowing to use CUPS printing
system directly.

%description cups -l pl.UTF-8
Paczka ta zawiera wtyczkę dla xfprint, która umożliwia bezpośrednie
korzystanie z systemu wydruku CUPS.

%package bsdlpr
Summary:	bsdlpr plugin for xfprint
Summary(pl.UTF-8):	Wtyczka bsdlpr dla xfprint
Group:		X11/Applications
Requires:	%{name} = %{version}-%{release}
Requires:	/usr/bin/lpr
Provides:	%{name}-print-backend = %{version}-%{release}

%description bsdlpr
This package contains plugin for xfprint allowing to use old bsd style
printing system through lpr program.

%description bsdlpr -l pl.UTF-8
Paczka ta zawiera wtyczkę dla xfprint, która umożliwia drukowanie w
stylu bsd poprzez program lpr.

%package devel
Summary:	Headers files for the xfprint library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki xfprint
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	gtk+2-devel >= 2:2.10.6
Requires:	libxfce4util-devel >= %{version}
Requires:	libxfcegui4-devel >= %{version}

%description devel
Header files for the xfprint library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki xfprint.

%prep
%setup -q
%patch0 -p1

%build
%{__glib_gettextize}
%{__intltoolize}
%{__libtoolize}
%{__aclocal}
%{__automake}
%{__autoheader}
%{__autoconf}
%configure \
	--disable-static \
	--enable-cups \
	--enable-bsdlpr=yes \
	--enable-gtk-doc \
	--with-html-dir=%{_gtkdocdir}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

mv $RPM_BUILD_ROOT%{_datadir}/locale/pt{_PT,}

# unusable (no devel resources)
rm -f $RPM_BUILD_ROOT%{_libdir}/xfce4/xfprint-plugins/*.la

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/ldconfig
%update_icon_cache hicolor

%postun
/sbin/ldconfig
%update_icon_cache hicolor

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_bindir}/xfprint-settings
%attr(755,root,root) %{_bindir}/xfprint4
%attr(755,root,root) %{_bindir}/xfprint4-manager
%attr(755,root,root) %{_libdir}/libxfprint.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libxfprint.so.0
%dir %{_libdir}/xfce4/xfprint-plugins
%{_desktopdir}/xfprint-manager.desktop
%{_desktopdir}/xfprint-settings.desktop
%{_desktopdir}/xfprint.desktop
%{_datadir}/xfce4/doc/C/*
%lang(fr) %{_datadir}/xfce4/doc/fr/*
%{_iconsdir}/hicolor/*/devices/*

%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/libxfprint

%files cups
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/xfce4/xfprint-plugins/cups_plugin.so

%files bsdlpr
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/xfce4/xfprint-plugins/bsdlpr_plugin.so

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libxfprint.so
%{_includedir}/xfce4/libxfprint
%{_libdir}/libxfprint.la
%{_pkgconfigdir}/xfprint-1.0.pc
