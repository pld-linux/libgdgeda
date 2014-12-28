Summary:	Hack of libgd library for gEDA project
Summary(pl.UTF-8):	Zmodyfikowana wersja libgd dla projektu gEDA
Name:		libgdgeda
Version:	2.0.15
Release:	1
License:	BSD-like
Group:		Libraries
Source0:	ftp://ftp.geda.seul.org/pub/geda/devel/support/%{name}-%{version}.tar.gz
# Source0-md5:	1580beb2bd224f38ce8637c67a5512f8
URL:		http://www.geda.seul.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-tools
BuildRequires:	libpng-devel
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Libgdgeda is a hack on libgd, which is a graphics library. It allows
your code to quickly draw images complete with lines, arcs, text,
multiple colors, cut and paste from other images, and flood fills, and
write out the result as a .PNG file.

%description -l pl.UTF-8
libgdgeda jest zmodyfikowaną biblioteką libgd pozwalającą na szybkie
rysowanie obrazków z liniami, łukami, tekstem, wieloma kolorami oraz
kopiowanie i wklejanie z innych obrazków, wypełnianie wzorcami, a w
rezultacie zapisywanie ich do pliku .PNG.

%package devel
Summary:	Header files and develpment documentation for libgdgeda
Summary(pl.UTF-8):	Pliki nagłówkowe i dokumentacja do libgdgeda
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libpng-devel

%description devel
Header files and develpment documentation for libgdgeda.

%description devel -l pl.UTF-8
Pliki nagłówkowe i dokumentacja do libgdgeda.

%package static
Summary:	Static libgdgeda library
Summary(pl.UTF-8):	Biblioteka statyczna libgdgeda
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libgdgeda library.

%description static -l pl.UTF-8
Biblioteka statyczna libgdgeda.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README.1ST COPYING
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*-config
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/gdgeda
%{_pkgconfigdir}/libgdgeda.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
