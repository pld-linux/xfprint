Summary: 	Print dialog and printer manager for XFce 4
Name: 		xfprint
Version: 	3.90.0
Release: 	0.1
License:	BSD
URL: 		http://www.xfce.org/
Source0: 	http://belnet.dl.sourceforge.net/sourceforge/xfce/%{name}-%{version}.tar.gz
# Source0-md5:	107d69e07a81eb4e4bfefa413b4a937c
Group: 		X11/Applications
Requires:	glib2 >= 2.0.0
Requires:	libxfcegui4
Requires:	a2ps
BuildRequires: 	glib2-devel >= 2.0.0
BuildRequires: 	libxfcegui4-devel
BuildRequires:	a2ps
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Xfprint contains a print dialog and a printer
manager for the XFce 4 Desktop Environment.

%prep
%setup -q

%build
glib-gettextize --copy --force
intltoolize --copy --force
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README ChangeLog NEWS INSTALL COPYING AUTHORS NOTES
%attr(755,root,root) %{_bindir}/*
%{_datadir}/locale/
%attr(755,root,root) %{_libdir}/*.so.*
%{_libdir}/*.la
%{_libdir}/*.a
