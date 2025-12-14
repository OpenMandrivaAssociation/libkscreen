%define major 8
%define libname %{mklibname KF6Screen}
%define devname %{mklibname KF6Screen -d}
%define stable %([ "$(echo %{version} |cut -d. -f2)" -ge 80 -o "$(echo %{version} |cut -d. -f3)" -ge 80 ] && echo -n un; echo -n stable)
#define git 20240222
%define gitbranch Plasma/6.0
%define gitbranchd %(echo %{gitbranch} |sed -e 's,/,-,g')

Summary:	Library for dealing with screen parameters
Name:		libkscreen
Version:	6.5.4
Release:	%{?git:0.%{git}.}1
License:	LGPL
Group:		System/Libraries
Url:		https://kde.org/
%if 0%{?git:1}
Source0:	https://invent.kde.org/plasma/libkscreen/-/archive/%{gitbranch}/libkscreen-%{gitbranchd}.tar.bz2#/libkscreen-%{git}.tar.bz2
%else
Source0:	http://download.kde.org/%{stable}/plasma/%(echo %{version} |cut -d. -f1-3)/libkscreen-%{version}.tar.xz
%endif
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(KWayland) >= 5.90.0
BuildRequires:	cmake(KF6Config)
BuildRequires:	cmake(QtWaylandScanner)
BuildRequires:	cmake(WaylandScanner)
BuildRequires:	pkgconfig(wayland-scanner)
BuildRequires:	pkgconfig(xkbcommon)
BuildRequires:	cmake(Qt6)
BuildRequires:	cmake(Qt6Core)
BuildRequires:	cmake(Qt6DBus)
BuildRequires:	cmake(Qt6Gui)
BuildRequires:	cmake(Qt6Test)
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(xcb)
BuildRequires:	pkgconfig(xcb-randr)
BuildRequires:	pkgconfig(xext)
BuildRequires:	pkgconfig(xrandr)
BuildRequires:	cmake(PlasmaWaylandProtocols) > 1.10
BuildRequires:	cmake(Qt6WaylandClient)
# For qch docs
BuildRequires:	doxygen
BuildRequires:	cmake(Qt6ToolsTools)
BuildSystem:	cmake
BuildOption:	-DBUILD_QCH:BOOL=ON
BuildOption:	-DBUILD_TESTING:BOOL=ON
BuildOption:	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON
Requires:	%{libname} = %{EVRD}
Requires:	%{name}-backend = %{EVRD}
# Renamed after 6.0 2025-04-27
%rename plasma6-libkscreen
# This was split out for coinstallability with Plasma 5, no longer needed
%rename plasma6-libkscreen-dbus-service

%package -n %{libname}
Summary: The KScreen library
Group: System/Libraries
Requires: %{name} = %{EVRD}

%description -n %{libname}
The KScreen library

%files -n %{libname}
%{_libdir}/libKF6Screen.so.%{major}*
%{_libdir}/libKF6Screen.so.6*
%{_libdir}/libKF6ScreenDpms.so.%{major}*
%{_libdir}/libKF6ScreenDpms.so.6*

%description
Library for dealing with screen parameters.

%files -f %{name}.lang
%{_datadir}/qlogging-categories6/libkscreen.categories
%dir %{_qtdir}/plugins/kf6/kscreen
%{_qtdir}/plugins/kf6/kscreen/KSC_Fake.so
%{_libdir}/libexec/kf6/kscreen_backend_launcher
%{_datadir}/dbus-1/services/org.kde.kscreen.service
%{_prefix}/lib/systemd/user/plasma-kscreen.service

%package x11
Summary:	X11 support for KScreen
Group:		System/Libraries
Requires:	%{name} = %{EVRD}
Provides:	%{name}-backend = %{EVRD}
# Renamed after 6.0 2025-04-27
%rename plasma6-libkscreen-x11

%description x11
X11 support for KScreen

%files x11
%{_qtdir}/plugins/kf6/kscreen/KSC_XRandR.so

%package wayland
Summary:	Wayland support for KScreen
Group:		System/Libraries
Requires:	%{name} = %{EVRD}
Provides:	%{name}-backend = %{EVRD}
# Renamed after 6.0 2025-04-27
%rename plasma6-libkscreen-wayland

%description wayland
Wayland support for KScreen

%files wayland
%{_qtdir}/plugins/kf6/kscreen/KSC_KWayland.so

%package -n %{devname}
Summary:	Development files for %{name}
Group:		Development/KDE and Qt
Requires:	%{libname} = %{EVRD}

%description -n %{devname}
Development files for %{name}.

%files -n %{devname}
%{_includedir}/KF6/KScreen
%{_includedir}/KF6/kscreen_version.h
%{_libdir}/cmake/KF6Screen
%{_libdir}/libKF6Screen.so
%{_libdir}/libKF6ScreenDpms.so
%{_libdir}/pkgconfig/*.pc

%package -n kscreen-doctor
Summary:	Tool for examining KScreen
Group:		Development/KDE and Qt
Requires:	%{libname} = %{EVRD}
# Renamed after 6.0 2025-04-27
%rename plasma6-kscreen-doctor

%description -n kscreen-doctor
Tool for examining KScreen

%files -n kscreen-doctor
%{_bindir}/kscreen-doctor
%{_datadir}/zsh/site-functions/_kscreen-doctor

#----------------------------------------------------------------------------

%package -n %{name}-devel-docs
Summary: Developer documentation for %{name} for use with Qt Assistant
Group: Documentation
Suggests: %{devname} = %{EVRD}
# Renamed after 6.0 2025-04-27
%rename plasma6-libkscreen-devel-docs

%description -n %{name}-devel-docs
Developer documentation for %{name} for use with Qt Assistant

%files -n %{name}-devel-docs
%{_qtdir}/doc/KF?Screen.*
