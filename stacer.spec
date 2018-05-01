%define         upstream_name Stacer

Name:           stacer
Version:        1.0.9
Release:        %mkrel 1
Summary:        Linux System Optimizer and Monitoring
Group:          Monitoring
License:        MIT
URL:            https://github.com/oguzhaninan/Stacer/
Source0:        https://github.com/oguzhaninan/Stacer/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  qt5-devel
BuildRequires:  qt5charts-devel
BuildRequires:  qt5help-devel
BuildRequires:  pkgconfig(Qt5Svg)
BuildRequires:  cmake

%description
Linux System Optimizer and Monitoring

%prep
%autosetup -n %{upstream_name}-%{version}

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



%changelog
* Tue Apr 10 2018 kekepower <kekepower> 1.0.9-1.mga7
  (not released yet)
+ Revision: 1217314
- imported package stacer

