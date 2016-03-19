Summary:	Display configuration library
Name:		libkscreen
Version:	1.0.5
Release:	4
License:	GPLv2+
Group:		Graphical desktop/KDE
Url:		https://projects.kde.org/projects/playground/libs/libkscreen
Source0:	ftp://ftp.kde.org/pub/kde/stable/%{name}/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	kdelibs4-devel
BuildRequires:	pkgconfig(xcb)
BuildRequires:	pkgconfig(xcb-image)
BuildRequires:	pkgconfig(xcb-renderutil)
BuildRequires:	pkgconfig(xrandr)
BuildRequires:	pkgconfig(QJson)
Requires:	kdebase4-runtime

%description
LibKScreen is a library that provides access to current configuration
of connected displays and ways to change the configuration.

%files
%{_kde_libdir}/kde4/plugins/kscreen/KSC_Fake.so
%{_kde_libdir}/kde4/plugins/kscreen/KSC_XRandR.so
%{_kde_libdir}/kde4/plugins/kscreen/KSC_XRandR11.so

#------------------------------------------------------------------------------

%define major 1
%define libname %mklibname kscreen %{major}

%package -n %{libname}
Summary:	KDE 4 core library
Group:		System/Libraries

%description -n %{libname}
LibKScreen is a library that provides access to current configuration
of connected displays and ways to change the configuration.

%files -n %{libname}
%{_kde_libdir}/libkscreen.so.%{major}*

#------------------------------------------------------------------------------

%define devname %mklibname kscreen -d

%package -n %{devname}
Summary:	Devel stuff for %{name}
Group:		Development/KDE and Qt
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{devname}
Files needed to build applications based on %{name}.

%files -n %{devname}
%{_kde_includedir}/kscreen
%{_kde_libdir}/cmake/LibKScreen
%{_kde_libdir}/libkscreen.so
%{_kde_libdir}/pkgconfig/kscreen.pc

#------------------------------------------------------------------------------

%prep
%setup -q

%build
%cmake_kde4
%make

%install
%makeinstall_std -C build

