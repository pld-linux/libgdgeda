Summary:	Hack of libgd library for gEDA project
Summary(pl):	Zmodyfikowana wersja libgd dla projektu gEDA
Name:		libgdgeda
Version:	2.0.15
Release:	1
License:	GPL
Group:		Libraries
Source0:	ftp://ftp.geda.seul.org/pub/geda/devel/support/%{name}-%{version}.tar.gz
# Source0-md5:	1580beb2bd224f38ce8637c67a5512f8
Patch0:		%{name}-am15.patch
URL:		http://www.geda.seul.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libpng-devel
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Libgdgeda is a hack on libgd, which is a graphics library. It allows
your code to quickly draw images complete with lines, arcs, text,
multiple colors, cut and paste from other images, and flood fills, and
write out the result as a .PNG file.

%description -l pl
libgdgeda jest zmodyfikowan± bibliotek± libgd pozwalaj±c± na szybkie
rysowanie obrazków z liniami, ³ukami, tekstem, wieloma kolorami oraz
kopiowanie i wklejanie z innych obrazków, wype³nianie wzorcami, a w
rezultacie zapisywanie ich do pliku .PNG.

%package devel
Summary:	Header files and develpment documentation for libgdgeda
Summary(pl):	Pliki nag³ówkowe i dokumetacja do libgdgeda
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description devel
Header files and develpment documentation for libgdgeda.

%description devel -l pl
Pliki nag³ówkowe i dokumetacja do libgdgeda.

%package static
Summary:	Static libgdgeda library
Summary(pl):	Biblioteka statyczna libgdgeda
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
Static libgdgeda library.

%description static -l pl
Biblioteka statyczna libgdgeda.

%prep
%setup -q
#%patch0 -p1

%build
rm -f missing acinclude.m4
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README* COPY*
%attr(755,root,root) %{_libdir}/lib*.so.*.* 
%{_libdir}/pkgconfig/libgdgeda.pc


%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*-config
%{_includedir}/gdgeda
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
