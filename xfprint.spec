Summary:	Print dialog and printer manager for Xfce
Summary(pl):	Okno dialogowe wydruku i zarz�dca drukarek dla Xfce
Name:		xfprint
Version:	4.2.3
Release:	1
License:	BSD
Group:		X11/Applications
Source0:	http://hannelore.f1.fhtw-berlin.de/mirrors/xfce4/xfce-%{version}/src/%{name}-%{version}.tar.gz
# Source0-md5:	64c983a6d7778cbd5d6c93ee1dbbd3f9
Patch0:		%{name}-locale-names.patch
Patch1:		%{name}-lpr.patch
URL:		http://www.xfce.org/
BuildRequires:	a2ps-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	cups-devel
BuildRequires:	gettext-devel
BuildRequires:	glib2-devel >= 2.2.0
BuildRequires:	intltool
BuildRequires:	libtool
BuildRequires:	libxfce4mcs-devel >= 4.2.0
BuildRequires:	libxfcegui4-devel >= 4.2.0
BuildRequires:	openssl-devel >= 0.9.7d
BuildRequires:	pkgconfig >= 1:0.9.0
BuildRequires:	xfce-mcs-manager-devel >= 4.2.0
BuildRequires:	xfce4-dev-tools
Requires:	%{name}-print-backend = %{version}-%{release}
Requires:	a2ps
Requires:	glib2 >= 2.2.0
Requires:	libxfcegui4 >= 4.2.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Xfprint contains a print dialog and a printer manager for the Xfce
Desktop Environment.

%description -l pl
Xfprint zawiera okno dialogowe wydruku i zarz�dc� drukarek dla
�rodowiska Xfce.

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
Paczka ta zawiera wtyczk� dla xfprint, kt�ra umo�liwia bezpo�rednie
korzystanie z systemu wydruku CUPS.

%package bsdlpr
Summary:	bsdlpr plugin for xfprint
Summary(pl):	Wtyczka bsdlpr dla xfprint
Group:		X11/Applications
Requires:	%{name} = %{version}-%{release}
Requires:	/usr/bin/lpr
Provides:	%{name}-print-backend = %{version}-%{release}

%description bsdlpr
This package contains plugin for xfprint allowing to use old bsd
style printing system through lpr program.

%description bsdlpr -l pl
Paczka ta zawiera wtyczk� dla xfprint, kt�ra umo�liwia drukowanie
w stylu bsd poprzez program lpr.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

mv -f po/{pt_PT,pt}.po

%build
glib-gettextize --copy --force
intltoolize --copy --force
%{__libtoolize}
%{__aclocal} -I %{_datadir}/xfce4/dev-tools/m4macros
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
%doc AUTHORS COPYING ChangeLog README
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/xfce4/mcs-plugins/*.so
%{_iconsdir}/hicolor/*/*/*
%{_desktopdir}/*.desktop
%{_datadir}/xfce4/doc/C/*
%lang(fr) %{_datadir}/xfce4/doc/fr/*
%lang(he) %{_datadir}/xfce4/doc/he/*

%files cups
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/xfce4/xfprint-plugins/cups_plugin.so

%files bsdlpr
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/xfce4/xfprint-plugins/bsdlpr_plugin.so