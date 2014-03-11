Summary:	KDE tool to setup PPP (Point-to-Point Protocol) connections
Name:		kppp
Version:	4.12.3
Release:	1
Epoch:		3
License:	GPLv2+
Group:		Graphical desktop/KDE
Url:		http://www.kde.org
%define is_beta %(if test `echo %{version} |cut -d. -f3` -ge 70; then echo -n 1; else echo -n 0; fi)
%if %{is_beta}
%define ftpdir unstable
%else
%define ftpdir stable
%endif
Source0:	ftp://ftp.kde.org/pub/kde/%{ftpdir}/%{version}/src/%{name}-%{version}.tar.xz
Source10:	%{name}.rpmlintrc
BuildRequires:	kdelibs4-devel
Requires:	ppp
Requires:	%{name}-provider = %{EVRD}
Conflicts:	kdenetwork4-devel < 3:4.11.0

%description
KPPP is used to setup PPP (Point-to-Point Protocol) connections. This is most
useful for connecting with a cell phone "modem" card these days. It is also use
to configure real modem connections.

%files
%{_kde_appsdir}/kppp
%{_kde_bindir}/kppp
%{_kde_bindir}/kppplogview
%{_kde_applicationsdir}/Kppp.desktop
%{_kde_applicationsdir}/kppplogview.desktop
%{_kde_docdir}/HTML/*/kppp
%{_kde_iconsdir}/*/*/apps/kppp.*
%{_datadir}/dbus-1/interfaces/org.kde.kppp.xml
%exclude %{_kde_appsdir}/kppp/Rules
%exclude %{_kde_appsdir}/kppp/Provider

#-----------------------------------------------------------

%package provider
Summary:	List of providers for KPPP
Group:		Graphical desktop/KDE

%description provider
List of providers for KPPP.

%files provider
%{_kde_appsdir}/kppp/Rules
%{_kde_appsdir}/kppp/Provider

#-------------------------------------------

%prep
%setup -q

%build
%cmake_kde4
%make

%install
%makeinstall_std -C build

%changelog
* Tue Mar 04 2014 Andrey Bondrov <andrey.bondrov@rosalab.ru> 3:4.12.3-1
- New version 4.12.3

* Tue Feb 04 2014 Andrey Bondrov <andrey.bondrov@rosalab.ru> 3:4.12.2-1
- New version 4.12.2

* Tue Jan 14 2014 Andrey Bondrov <andrey.bondrov@rosalab.ru> 3:4.12.1-1
- New version 4.12.1

* Wed Dec 04 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 3:4.11.4-1
- New version 4.11.4

* Wed Nov 06 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 3:4.11.3-1
- New version 4.11.3

* Wed Oct 02 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 3:4.11.2-1
- New version 4.11.2

* Tue Sep 03 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 3:4.11.1-1
- New version 4.11.1

* Wed Aug 14 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 3:4.11.0-1
- New version 4.11.0
- Split from kdenetwork4 package as upstream did
- Add Conflicts with old devel package
