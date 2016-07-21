Summary:	KDE tool to setup PPP (Point-to-Point Protocol) connections
Name:		kppp
Version:	16.04.3
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
Source0:	http://download.kde.org/stable/applications/%{version}/src/%{name}-%{version}.tar.xz
Source10:	%{name}.rpmlintrc
BuildRequires:	kdelibs-devel
Requires:	ppp
Requires:	%{name}-provider = %{EVRD}
Conflicts:	kdenetwork4-devel < 3:4.11.0

%description
KPPP is used to setup PPP (Point-to-Point Protocol) connections. This is most
useful for connecting with a cell phone "modem" card these days. It is also use
to configure real modem connections.

%files
%{_datadir}/apps/kppp                                                                                  
%{_bindir}/kppp                                                                                        
%{_bindir}/kppplogview                                                                                 
%{_datadir}/applications/kde4/Kppp.desktop                                                             
%{_datadir}/applications/kde4/kppplogview.desktop                                                      
%doc %{_docdir}/HTML/*/kppp                                                                            
%{_iconsdir}/*/*/apps/kppp.*                                                                           
%{_datadir}/dbus-1/interfaces/org.kde.kppp.xml                                                         
%exclude %{_datadir}/apps/kppp/Rules                                                                   
%exclude %{_datadir}/apps/kppp/Provider                                                                
                                        

#-----------------------------------------------------------

%package provider
Summary:	List of providers for KPPP
Group:		Graphical desktop/KDE

%description provider
List of providers for KPPP.

%files provider
%{_datadir}/apps/kppp/Rules                                                                            
%{_datadir}/apps/kppp/Provider  

#-------------------------------------------

%prep
%setup -q

%build
%cmake_kde4 \
	-DCMAKE_MINIMUM_REQUIRED_VERSION=3.1
%make

%install
%makeinstall_std -C build


