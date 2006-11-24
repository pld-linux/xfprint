Summary:	Print dialog and printer manager for Xfce
Summary(pl):	Okno dialogowe wydruku i zarz±dca drukarek dla Xfce
Name:		xfprint
Version:	4.3.99.2
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://www.xfce.org/archive/xfce-%{version}/src/%{name}-%{version}.tar.bz2
# Source0-md5:	c2eb9dee0002e875b91e73557f7354a1
Patch0:		%{name}-locale-names.patch
Patch1:		%{name}-lpr.patch
URL:		http://www.xfce.org/
BuildRequires:	a2ps-devel
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	cups-devel
BuildRequires:	gettext-devel
BuildRequires:	gtk+2-devel >= 2:2.10.6
BuildRequires:	intltool
BuildRequires:	libtool
BuildRequires:	libxfce4mcs-devel >= %{version}
BuildRequires:	libxfcegui4-devel >= %{version}
BuildRequires:	openssl-devel >= 0.9.7d
BuildRequires:	pkgconfig >= 1:0.9.0
BuildRequires:	xfce-mcs-manager-devel >= %{version}
BuildRequires:	xfce4-dev-tools >= %{version}
Requires:	%{name}-print-backend = %{version}-%{release}
Requires:	a2ps
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Xfprint contains a print dialog and a printer manager for the Xfce
Desktop Environment.

%description -l pl
Xfprint zawiera okno dialogowe wydruku i zarz±dcê drukarek dla
¶rodowiska Xfce.

%package cups
Summary:	CUPS plugin for xfprint
Summary(pl):	Wtyczka CUPS dla xfprint
Group:		X11/Applications
Requires:	%{name} = %{version}-%{release}
Provides:	%{name}-print-backend = %{version}-%{release}

%description cups
This package contains plugin for xfprint allowing to use CUPS printing
system directly.

%description cups -l pl
Paczka ta zawiera wtyczkê dla xfprint, która umo¿liwia bezpo¶rednie
korzystanie z systemu wydruku CUPS.

%package bsdlpr
Summary:	bsdlpr plugin for xfprint
Summary(pl):	Wtyczka bsdlpr dla xfprint
Group:		X11/Applications
Requires:	%{name} = %{version}-%{release}
Requires:	/usr/bin/lpr
Provides:	%{name}-print-backend = %{version}-%{release}

%description bsdlpr
This package contains plugin for xfprint allowing to use old bsd style
printing system through lpr program.

%description bsdlpr -l pl
Paczka ta zawiera wtyczkê dla xfprint, która umo¿liwia drukowanie w
stylu bsd poprzez program lpr.

%package devel
Summary:	Headers files for the xfprint library
Summary(pl):	Pliki nag³ówkowe biblioteki xfprint
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for the xfprint library.

%description devel -l pl
Pliki nag³ówkowe biblioteki xfprint.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

mv -f po/{pt_PT,pt}.po

%build
%{__glib_gettextize}
%{__intltoolize}
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-static \
	--enable-cups \
	--enable-bsdlpr

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# unusable (no devel resources)
rm -f $RPM_BUILD_ROOT%{_libdir}/xfce4/mcs-plugins/*.la
rm -f $RPM_BUILD_ROOT%{_libdir}/xfce4/xfprint-plugins/*.la

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/libxfprint.so.*.*.*
%attr(755,root,root) %{_libdir}/xfce4/mcs-plugins/*.so
%dir %{_libdir}/xfce4/xfprint-plugins
%{_desktopdir}/*.desktop
%{_datadir}/xfce4/doc/C/*
%lang(fr) %{_datadir}/xfce4/doc/fr/*

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
