Summary:	LibGGIGCP - generic color and palette management extension
Summary(pl.UTF-8):	LibGGIGCP - ogólne rozszerzenie do zarządzania kolorami i paletą
Name:		libggigcp
Version:	1.0.2
Release:	1
License:	Public Domain
Group:		Libraries
# HTTP 403
#Source0:	http://www.ggi-project.org/ftp/ggi/v2.2/%{name}-%{version}.src.tar.bz2
Source0:	http://downloads.sourceforge.net/ggi/%{name}-%{version}.src.tar.bz2
# Source0-md5:	d8e8a5317db1e3aeac98338a2ad10c69
URL:		http://www.ggi-project.org/packages/libggigcp.html
BuildRequires:	libggi-devel >= 2.2.2
Requires:	libggi >= 2.2.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
LibGGIGCP is a generic color and palette management extension. It
supports conversion between different color spaces such as RGBA, YUV,
HSV and CMYK. Furthermore it supports a generic color-blending, which
can also be used for transluency effects.

%description -l pl.UTF-8
LibGGIGCP to ogólne rozszerzenie do zarządzania kolorami i paletą.
Obsługuje konwersję pomiędzy różnymi przestrzeniami kolorów, takimi
jak RGBA, YUV, HSV i CMYK. Ponadto obsługuje ogólny blending kolorów,
który może być używany także do efektów przezroczystości.

%package devel
Summary:	Header files for libggigcp library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libggigcp
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libggi-devel >= 2.2.2

%description devel
Header files for libggigcp library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki libggigcp.

%package static
Summary:	Static libggigcp library
Summary(pl.UTF-8):	Statyczna biblioteka libggigcp
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libggigcp library.

%description static -l pl.UTF-8
Statyczna biblioteka libggigcp.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/ggi/gcp/default/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc COPYING ChangeLog README doc/{TODO,colors*.faq}
%attr(755,root,root) %{_libdir}/libggigcp.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libggigcp.so.1
%dir %{_libdir}/ggi/gcp
%dir %{_libdir}/ggi/gcp/default
%attr(755,root,root) %{_libdir}/ggi/gcp/default/*.so
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/ggi/libggigcp.conf
%{_mandir}/man7/libggigcp.7*

%files devel
%defattr(644,root,root,755)
%doc doc/*.txt
%attr(755,root,root) %{_libdir}/libggigcp.so
%{_libdir}/libggigcp.la
%{_includedir}/ggi/gcp*.h
%{_includedir}/ggi/internal/gcp.h
%{_mandir}/man3/gcp*.3*

%files static
%defattr(644,root,root,755)
%{_libdir}/libggigcp.a
