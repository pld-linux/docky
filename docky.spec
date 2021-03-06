Summary:	Docky - a full fledged dock application
Name:		docky
Version:	2.1.1
Release:	0.1
License:	GPL v3+
Group:		X11/Applications
Source0:	http://launchpad.net/docky/2.1/%{version}/+download/%{name}-%{version}.tar.gz
# Source0-md5:	628418e11088b96d47287dac6e838507
URL:		https://launchpad.net/docky/
BuildRequires:	GConf2-devel
BuildRequires:	autoconf >= 2.54
BuildRequires:	automake
BuildRequires:	dotnet-dbus-sharp-devel >= 1:0.7.0
BuildRequires:	dotnet-dbus-sharp-glib-devel >= 0.5.0
BuildRequires:	dotnet-gio-sharp-devel >= 0.2-2
BuildRequires:	dotnet-gnome-desktop-sharp-devel
BuildRequires:	dotnet-gnome-keyring-sharp-devel >= 1.0.0
BuildRequires:	dotnet-gnome-sharp-devel
BuildRequires:	dotnet-notify-sharp-devel
BuildRequires:	gettext-tools
BuildRequires:	glib2-devel >= 1:2.18.1
BuildRequires:	gtk+2-devel >= 1:2.14.3
BuildRequires:	intltool
BuildRequires:	libtool
BuildRequires:	mono-addins-devel
BuildRequires:	mono-csharp >= 1.1.13
BuildRequires:	mono-devel >= 2.2.0
BuildRequires:	pkgconfig
BuildRequires:	python-devel
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
BuildRequires:	rpmbuild(monoautodeps)
BuildRequires:	sed >= 4.0
Requires(post,postun):	gtk-update-icon-cache
Requires(post,postun):	hicolor-icon-theme
Requires:	xdg-utils
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Docky is a full fledged dock application that makes opening common
applications and managing windows easier and quicker. Docky is fully
integrated into the GNOME Desktop and features a no non-sense approach
to configuration and usage. It just works.

%package devel
Summary:	Development information for Docky plugins
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Development information for Docky plugins.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal} -I m4/shamrock
%{__autoconf}
%{__automake}
%configure \
	--enable-release
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	linuxpkgconfigdir=%{_pkgconfigdir}

%py_postclean

%find_lang %{name} --with-gnome

%post
%update_desktop_database_post
%update_icon_cache hicolor

%postun
%update_desktop_database_postun
%update_icon_cache hicolor

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS
%attr(755,root,root) %{_bindir}/docky
%dir %{_libdir}/docky
%attr(755,root,root) %{_libdir}/docky/Docky.exe
%{_libdir}/docky/Docky.addins
#%%{_libdir}/docky/Docky.exe.mdb
%{_libdir}/docky/Docky.*.dll
%{_libdir}/docky/Docky.*.dll.config
#%%{_libdir}/docky/Docky.*.dll.mdb
#%%attr(755,root,root) %{_libdir}/docky/gapi_codegen.exe
#%%{_libdir}/docky/gapi_codegen.exe.mdb
%{_libdir}/docky/gio-sharp.dll
%{_libdir}/docky/gio-sharp.dll.config
%dir %{_libdir}/docky/plugins
%{_libdir}/docky/plugins/*.dll
#%%{_libdir}/docky/plugins/*.dll.mdb
%dir %{_datadir}/docky
%{_datadir}/docky/ClockTheme
%{_datadir}/docky/*.png
#%%dir %{_datadir}/docky/helpers
# keep .py files in that dir
#%%attr(755,root,root) %{_datadir}/docky/helpers/*.py
#%%attr(755,root,root) %{_datadir}/docky/helpers/metadata
%{_datadir}/docky/themes
#%%{_sysconfdir}/xdg/autostart/docky.desktop
%{_desktopdir}/docky.desktop
%{_iconsdir}/hicolor/*/apps/docky.svg
%{_iconsdir}/hicolor/*/apps/gmail.png
%{_iconsdir}/hicolor/*/mimetypes/extension.svg
#%%dir %{py_sitescriptdir}/docky
#%%{py_sitescriptdir}/docky/*.py[co]
%{_mandir}/man1/docky.1*

%files devel
%defattr(644,root,root,755)
%{_pkgconfigdir}/docky.cairohelper.pc
%{_pkgconfigdir}/docky.items.pc
%{_pkgconfigdir}/docky.services.pc
%{_pkgconfigdir}/docky.widgets.pc
#%%{_pkgconfigdir}/docky.windowing.pc
