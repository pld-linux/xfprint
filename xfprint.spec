Summary:	Print dialog and printer manager for XFce
Summary(pl):	Okno dialogowe wydruku i zarz±dca drukarek dla XFce
Name:		xfprint
Version:	4.1.99.1
Release:	1
License:	BSD
Group:		X11/Applications
Source0:	ftp://ftp.berlios.de/pub/xfce-goodies/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	af55239d91d52470a6240e682eaea639
Patch0:		%{name}-locale-names.patch
URL:		http://www.xfce.org/
BuildRequires:	a2ps-devel
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	glib2-devel >= 2.0.6
BuildRequires:	intltool
BuildRequires:	libtool
BuildRequires:	libxfcegui4-devel >= 4.1.25
BuildRequires:	pkgconfig >= 0.9.0
Requires:	a2ps
Requires:	glib2 >= 2.0.6
Requires:	libxfcegui4 >= 4.1.25
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Xfprint contains a print dialog and a printer manager for the XFce
Desktop Environment.

%description -l pl
Xfprint zawiera okno dialogowe wydruku i zarz±dcê drukarek dla
¶rodowiska XFce.

%prep
%setup -q
%patch0 -p1

mv -f po/{pt_PT,pt}.po

%build
glib-gettextize --copy --force
intltoolize --copy --force
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# unusable (no devel resources)
rm -f $RPM_BUILD_ROOT%{_libdir}/xfce4/mcs-plugins/*.{la,a}
rm -f $RPM_BUILD_ROOT%{_libdir}/xfce4/xfprint-plugins/*.{la,a}

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
%dir %{_libdir}/xfce4/xfprint-plugins
%attr(755,root,root) %{_libdir}/xfce4/xfprint-plugins/*.so
%{_iconsdir}/hicolor/*/*/*
