%define major 8
%define libname %{mklibname KF5Screen}
%define oldlibname %{mklibname KF5Screen 7}
%define devname %{mklibname KF5Screen -d}
%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)

Summary:	Library for dealing with screen parameters
Name:		libkscreen
Version:	5.27.1
Release:	1
License:	LGPL
Group:		System/Libraries
Url:		http://kde.org/
Source0:	http://download.kde.org/%{stable}/plasma/%(echo %{version} |cut -d. -f1-3)/libkscreen-%{version}.tar.xz
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(KF5Wayland)
BuildRequires:	cmake(KF5Config)
BuildRequires:	cmake(QtWaylandScanner)
BuildRequires:	cmake(WaylandScanner)
BuildRequires:	pkgconfig(wayland-scanner)
BuildRequires:	pkgconfig(Qt5Core)
BuildRequires:	pkgconfig(Qt5DBus)
BuildRequires:	pkgconfig(Qt5Gui)
BuildRequires:	pkgconfig(Qt5Test)
BuildRequires:	pkgconfig(Qt5X11Extras)
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(xcb)
BuildRequires:	pkgconfig(xcb-randr)
BuildRequires:	pkgconfig(xext)
BuildRequires:	pkgconfig(xrandr)
BuildRequires:	cmake(PlasmaWaylandProtocols) >= 1.4.0
BuildRequires:	pkgconfig(Qt5WaylandClient)
BuildRequires:	qt5-qtwayland
# For qch docs
BuildRequires:	doxygen
BuildRequires:	qt5-assistant
Requires:	%{libname} = %{EVRD}
Requires:	%{name}-backend = %{EVRD}

%package -n %{libname}
Summary: The KScreen library
Group: System/Libraries
Requires: %{name} = %{EVRD}
%rename %{oldlibname}

%description -n %{libname}
The KScreen library

%files -n %{libname}
%{_libdir}/libKF5Screen.so.%{major}*
%{_libdir}/libKF5Screen.so.5*
%{_libdir}/libKF5ScreenDpms.so.%{major}*
%{_libdir}/libKF5ScreenDpms.so.5*

%description
Library for dealing with screen parameters.

%files -f libkscreen5_qt.lang
%{_datadir}/qlogging-categories5/%{name}.categories
%{_bindir}/kscreen-doctor
%dir %{_libdir}/qt5/plugins/kf5/kscreen
%{_libdir}/qt5/plugins/kf5/kscreen/KSC_Fake.so
%{_libdir}/qt5/plugins/kf5/kscreen/KSC_QScreen.so
%{_libdir}/libexec/kf5/kscreen_backend_launcher
%{_datadir}/dbus-1/services/org.kde.kscreen.service
%{_prefix}/lib/systemd/user/plasma-kscreen.service
%{_datadir}/zsh/site-functions/_kscreen-doctor

%package x11
Summary:	X11 support for KScreen
Group:		System/Libraries
Requires:	%{name} = %{EVRD}
Provides:	%{name}-backend = %{EVRD}

%description x11
X11 support for KScreen

%files x11
%{_libdir}/qt5/plugins/kf5/kscreen/KSC_XRandR.so
%{_libdir}/qt5/plugins/kf5/kscreen/KSC_XRandR11.so

%package wayland
Summary:	Wayland support for KScreen
Group:		System/Libraries
Requires:	%{name} = %{EVRD}
Provides:	%{name}-backend = %{EVRD}

%description wayland
Wayland support for KScreen

%files wayland
%{_libdir}/qt5/plugins/kf5/kscreen/KSC_KWayland.so

%package -n %{devname}
Summary:	Development files for %{name}
Group:		Development/KDE and Qt
Requires:	%{libname} = %{EVRD}

%description -n %{devname}
Development files for %{name}.

%files -n %{devname}
%{_includedir}/KF5/KScreen
%{_includedir}/KF5/kscreen_version.h
%{_libdir}/cmake/KF5Screen
%{_libdir}/libKF5Screen.so
%{_libdir}/libKF5ScreenDpms.so
%{_libdir}/pkgconfig/*.pc
%{_libdir}/qt5/mkspecs/modules/*

#----------------------------------------------------------------------------

%package -n %{name}-devel-docs
Summary: Developer documentation for %{name} for use with Qt Assistant
Group: Documentation
Suggests: %{devname} = %{EVRD}

%description -n %{name}-devel-docs
Developer documentation for %{name} for use with Qt Assistant

%files -n %{name}-devel-docs
%{_docdir}/qt5/*.{tags,qch}

#----------------------------------------------------------------------------

%prep
%autosetup -n libkscreen-%{version} -p1
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build
%find_lang libkscreen5_qt --all-name --with-qt
