Summary:	hack of libgd library for gEDA project
Summary(pl):	Zmodyfikowana wersja libgd dla projektu gEDA
Name:		libgdgeda
Version:	1.8
Release:	1
License:	GPL
Group:		Libraries
BuildRequires:	zlib-devel
BuildRequires:	libpng-devel
Source0:	ftp://ftp.geda.seul.org/pub/geda/devel/support/%{name}-%{version}.tar.gz
URL:		http://www.geda.seul.org/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Libgdgeda is a hack on libgd, which is a graphics library. It allows
your code to quickly draw images complete with lines, arcs, text,
multiple colors, cut and paste from other images, and flood fills, and
write out the result as a .PNG file.

%description -l pl
libgdgeda jest zmodyfikowaną biblioteką libgd pozwalającą na szybkie
rysowanie obrazków z liniami, łukami, tekstem, wieloma kolorami oraz
kopiowanie i wklejanie z innych obrazków, wypełnianie wzorcami, a w
rezultacie zapisywanie ich do pliku .PNG.

%package devel
Summary:	Header files and develpment documentation for libgdgeda
Summary(pl):	Pliki nagłówkowe i dokumetacja do libgdgeda
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description devel
Header files and develpment documentation for libgdgeda.

%description -l pl devel
Pliki nagłówkowe i dokumetacja do libgdgeda.

%package static
Summary:	Static libgdgeda library
Summary(pl):	Biblioteka statyczna libgdgeda
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
Static libgdgeda library.

%description -l pl static
Biblioteka statyczna libgdgeda.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

gzip -9nf README* COPY*

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*-config
%{_includedir}/gdgeda
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
