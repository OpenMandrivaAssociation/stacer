%define oname Stacer

Name:           stacer
Version:        1.0.9
Release:        1
Summary:        Linux System Optimizer and Monitoring
Group:          Monitoring
License:        MIT
URL:            https://github.com/oguzhaninan/Stacer/
Source0:        https://github.com/oguzhaninan/Stacer/archive/v%{version}/%{oname}-%{version}.tar.gz
Patch0:         stacer-1.0.9-fix-build-against-qt-5.11.0.patch

BuildRequires:  qt5-devel
BuildRequires:	pkgconfig(Qt5Core)
BuildRequires:  qt5-linguist-tools
BuildRequires:	pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Charts)
BuildRequires:  pkgconfig(Qt5Concurrent)
BuildRequires:  pkgconfig(Qt5Help)
BuildRequires:  pkgconfig(Qt5Svg)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  cmake


%description
Linux System Optimizer and Monitoring

%prep
%setup -q -n Stacer-%{version}
%patch0 -p1

%build
%cmake_qt5
%make_build
%install
%make_install -C build

%files
%doc README.md
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/%{name}.*
