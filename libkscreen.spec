%define major 7
%define libname %{mklibname KF5Screen %{major}}
%define devname %{mklibname KF5Screen -d}
%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)

Summary:	Library for dealing with screen parameters
Name:		libkscreen
Version:	5.21.2
Release:	1
License:	LGPL
Group:		System/Libraries
Url:		http://kde.org/
Source0:	http://download.kde.org/%{stable}/plasma/%(echo %{version} |cut -d. -f1-3)/libkscreen-%{version}.tar.xz
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(KF5Wayland)
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
# For qch docs
BuildRequires:	doxygen
BuildRequires:	qt5-assistant
Requires:	%{libname} = %{EVRD}

%dependinglibpackage KF5Screen %{major}
%{_libdir}/libKF5Screen.so.5*

%description
Library for dealing with screen parameters.

%files
%{_datadir}/qlogging-categories5/%{name}.categories
%{_bindir}/kscreen-doctor
%{_libdir}/qt5/plugins/kf5/kscreen
%{_libdir}/libexec/kf5/kscreen_backend_launcher
%{_datadir}/dbus-1/services/org.kde.kscreen.service

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
