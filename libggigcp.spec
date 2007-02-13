Summary:	LibGGIGCP - generic color and palette management extension
Summary(pl.UTF-8):	LibGGIGCP - ogólne rozszerzenie do zarządzania kolorami i paletą
Name:		libggigcp
Version:	0.9.2
Release:	1
License:	Public Domain
Group:		Libraries
Source0:	http://www.ggi-project.org/ftp/ggi/v2.1/%{name}-%{version}.src.tar.bz2
# Source0-md5:	b99ae02ec479ca9eaf295a97e2789d43
URL:		http://www.ggi-project.org/packages/libggigcp.html
BuildRequires:	libggi-devel >= 2.1.2
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
Requires:	libggi-devel >= 2.1.2

%description devel
Header files for libggigcp library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki libggigcp.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/ggi/gcp/default/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc COPYING ChangeLog README doc/{TODO,colors*.faq}
%attr(755,root,root) %{_libdir}/libggigcp.so.*.*.*
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
