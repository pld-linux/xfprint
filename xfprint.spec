Summary:	Print dialog and printer manager for XFce
Summary(pl):	Okno dialogowe wydruku i zarz�dca drukarek dla XFce
Name:		xfprint
Version:	4.0.0
Release:	1
License:	BSD
Group:		X11/Applications
Source0:	http://www.xfce.org/archive/xfce-%{version}/src/%{name}-%{version}.tar.gz
# Source0-md5:	b2ba1fa91737294785ce7a8b8a282d78
URL:		http://www.xfce.org/
BuildRequires:	glib2-devel >= 2.0.0
BuildRequires:	intltool
BuildRequires:	libxfcegui4-devel >= %{version}
BuildRequires:	pkgconfig >= 0.9.0
Requires:	a2ps
Requires:	glib2 >= 2.0.0
Requires:	libxfcegui4 >= %{version}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Xfprint contains a print dialog and a printer manager for the XFce
Desktop Environment.

%description -l pl
Xfprint zawiera okno dialogowe wydruku i zarz�dc� drukarek dla
�rodowiska XFce.

%prep
%setup -q

%build
glib-gettextize --copy --force
intltoolize --copy --force
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# unusable (no devel resources)
rm -f $RPM_BUILD_ROOT%{_libdir}/lib*.{la,a}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog README
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/lib*.so.*.*
