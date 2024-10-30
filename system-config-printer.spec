#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: configure
# autospec version: v18
# autospec commit: eaa4f711da30
#
# Source0 file verified with key 0xE4522DCC9B246FF7 (zdohnal@redhat.com)
#
Name     : system-config-printer
Version  : 1.5.18
Release  : 16
URL      : https://github.com/OpenPrinting/system-config-printer/releases/download/v1.5.18/system-config-printer-1.5.18.tar.xz
Source0  : https://github.com/OpenPrinting/system-config-printer/releases/download/v1.5.18/system-config-printer-1.5.18.tar.xz
Source1  : https://github.com/OpenPrinting/system-config-printer/releases/download/v1.5.18/system-config-printer-1.5.18.tar.xz.asc
Source2  : E4522DCC9B246FF7.pkey
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0
Requires: system-config-printer-bin = %{version}-%{release}
Requires: system-config-printer-config = %{version}-%{release}
Requires: system-config-printer-data = %{version}-%{release}
Requires: system-config-printer-license = %{version}-%{release}
Requires: system-config-printer-locales = %{version}-%{release}
Requires: system-config-printer-man = %{version}-%{release}
Requires: system-config-printer-python = %{version}-%{release}
Requires: system-config-printer-python3 = %{version}-%{release}
Requires: system-config-printer-services = %{version}-%{release}
BuildRequires : buildreq-configure
BuildRequires : desktop-file-utils
BuildRequires : docbook-xml
BuildRequires : gettext
BuildRequires : gnupg
BuildRequires : libxml2-dev
BuildRequires : libxslt-bin
BuildRequires : perl(XML::Parser)
BuildRequires : pkgconfig(cups)
BuildRequires : pkgconfig(glib-2.0)
BuildRequires : pkgconfig(libudev)
BuildRequires : pkgconfig(libusb-1.0)
BuildRequires : xmlto
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description


%package bin
Summary: bin components for the system-config-printer package.
Group: Binaries
Requires: system-config-printer-data = %{version}-%{release}
Requires: system-config-printer-config = %{version}-%{release}
Requires: system-config-printer-license = %{version}-%{release}
Requires: system-config-printer-services = %{version}-%{release}

%description bin
bin components for the system-config-printer package.


%package config
Summary: config components for the system-config-printer package.
Group: Default

%description config
config components for the system-config-printer package.


%package data
Summary: data components for the system-config-printer package.
Group: Data

%description data
data components for the system-config-printer package.


%package license
Summary: license components for the system-config-printer package.
Group: Default

%description license
license components for the system-config-printer package.


%package locales
Summary: locales components for the system-config-printer package.
Group: Default

%description locales
locales components for the system-config-printer package.


%package man
Summary: man components for the system-config-printer package.
Group: Default

%description man
man components for the system-config-printer package.


%package python
Summary: python components for the system-config-printer package.
Group: Default
Requires: system-config-printer-python3 = %{version}-%{release}

%description python
python components for the system-config-printer package.


%package python3
Summary: python3 components for the system-config-printer package.
Group: Default
Requires: python3-core
Requires: pypi(pycups)

%description python3
python3 components for the system-config-printer package.


%package services
Summary: services components for the system-config-printer package.
Group: Systemd services
Requires: systemd

%description services
services components for the system-config-printer package.


%prep
mkdir .gnupg
chmod 700 .gnupg
gpg --homedir .gnupg --import %{SOURCE2}
gpg --homedir .gnupg --status-fd 1 --verify %{SOURCE1} %{SOURCE0} > gpg.status
grep -E '^\[GNUPG:\] (GOODSIG|EXPKEYSIG) E4522DCC9B246FF7' gpg.status
%setup -q -n system-config-printer-1.5.18
cd %{_builddir}/system-config-printer-1.5.18

%build
## build_prepend content
# workaround https://github.com/pypa/setuptools/issues/3143
sed -i 's/setup.py install --prefix=$(DESTDIR)$(prefix)/setup.py install --root $(DESTDIR) --prefix=$(prefix)/' Makefile*
## build_prepend end
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1725476321
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
%configure --disable-static --with-udev-rules \
--sysconfdir=/usr/share/system-config-printer
make  %{?_smp_mflags}

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make %{?_smp_mflags} check

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1725476321
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/system-config-printer
cp %{_builddir}/system-config-printer-%{version}/COPYING %{buildroot}/usr/share/package-licenses/system-config-printer/4cc77b90af91e615a64ae04893fdffa7939db84c || :
export GOAMD64=v2
GOAMD64=v2
%make_install
%find_lang system-config-printer

%files
%defattr(-,root,root,-)
/usr/lib/udev/udev-add-printer
/usr/lib/udev/udev-configure-printer

%files bin
%defattr(-,root,root,-)
/usr/bin/install-printerdriver
/usr/bin/scp-dbus-service
/usr/bin/system-config-printer
/usr/bin/system-config-printer-applet

%files config
%defattr(-,root,root,-)
/usr/lib/udev/rules.d/70-printers.rules

%files data
%defattr(-,root,root,-)
/usr/share/applications/system-config-printer.desktop
/usr/share/dbus-1/interfaces/org.fedoraproject.Config.Printing.xml
/usr/share/dbus-1/services/org.fedoraproject.Config.Printing.service
/usr/share/metainfo/system-config-printer.appdata.xml
/usr/share/system-config-printer/HIG.py
/usr/share/system-config-printer/OpenPrintingRequest.py
/usr/share/system-config-printer/PhysicalDevice.py
/usr/share/system-config-printer/SearchCriterion.py
/usr/share/system-config-printer/ToolbarSearchEntry.py
/usr/share/system-config-printer/applet.py
/usr/share/system-config-printer/asyncconn.py
/usr/share/system-config-printer/asyncipp.py
/usr/share/system-config-printer/asyncpk1.py
/usr/share/system-config-printer/authconn.py
/usr/share/system-config-printer/check-device-ids.py
/usr/share/system-config-printer/config.py
/usr/share/system-config-printer/cupshelpers/preferreddrivers.xml
/usr/share/system-config-printer/cupspk.py
/usr/share/system-config-printer/dbus-1/system.d/com.redhat.NewPrinterNotification.conf
/usr/share/system-config-printer/dbus-1/system.d/com.redhat.PrinterDriversInstaller.conf
/usr/share/system-config-printer/debug.py
/usr/share/system-config-printer/dnssdresolve.py
/usr/share/system-config-printer/errordialogs.py
/usr/share/system-config-printer/firewallsettings.py
/usr/share/system-config-printer/gtkinklevel.py
/usr/share/system-config-printer/gui.py
/usr/share/system-config-printer/icons/i-network-printer.png
/usr/share/system-config-printer/install-printerdriver.py
/usr/share/system-config-printer/installpackage.py
/usr/share/system-config-printer/jobviewer.py
/usr/share/system-config-printer/killtimer.py
/usr/share/system-config-printer/monitor.py
/usr/share/system-config-printer/newprinter.py
/usr/share/system-config-printer/options.py
/usr/share/system-config-printer/optionwidgets.py
/usr/share/system-config-printer/ppdcache.py
/usr/share/system-config-printer/ppdippstr.py
/usr/share/system-config-printer/ppdsloader.py
/usr/share/system-config-printer/printerproperties.py
/usr/share/system-config-printer/probe_printer.py
/usr/share/system-config-printer/pysmb.py
/usr/share/system-config-printer/scp-dbus-service.py
/usr/share/system-config-printer/serversettings.py
/usr/share/system-config-printer/smburi.py
/usr/share/system-config-printer/statereason.py
/usr/share/system-config-printer/system-config-printer.py
/usr/share/system-config-printer/timedops.py
/usr/share/system-config-printer/troubleshoot/CheckLocalServerPublishing.py
/usr/share/system-config-printer/troubleshoot/CheckNetworkServerSanity.py
/usr/share/system-config-printer/troubleshoot/CheckPPDSanity.py
/usr/share/system-config-printer/troubleshoot/CheckPrinterSanity.py
/usr/share/system-config-printer/troubleshoot/CheckSELinux.py
/usr/share/system-config-printer/troubleshoot/CheckUSBPermissions.py
/usr/share/system-config-printer/troubleshoot/ChooseNetworkPrinter.py
/usr/share/system-config-printer/troubleshoot/ChoosePrinter.py
/usr/share/system-config-printer/troubleshoot/DeviceListed.py
/usr/share/system-config-printer/troubleshoot/ErrorLogCheckpoint.py
/usr/share/system-config-printer/troubleshoot/ErrorLogFetch.py
/usr/share/system-config-printer/troubleshoot/ErrorLogParse.py
/usr/share/system-config-printer/troubleshoot/LocalOrRemote.py
/usr/share/system-config-printer/troubleshoot/Locale.py
/usr/share/system-config-printer/troubleshoot/NetworkCUPSPrinterShared.py
/usr/share/system-config-printer/troubleshoot/PrintTestPage.py
/usr/share/system-config-printer/troubleshoot/PrinterStateReasons.py
/usr/share/system-config-printer/troubleshoot/QueueNotEnabled.py
/usr/share/system-config-printer/troubleshoot/QueueRejectingJobs.py
/usr/share/system-config-printer/troubleshoot/RemoteAddress.py
/usr/share/system-config-printer/troubleshoot/SchedulerNotRunning.py
/usr/share/system-config-printer/troubleshoot/ServerFirewalled.py
/usr/share/system-config-printer/troubleshoot/Shrug.py
/usr/share/system-config-printer/troubleshoot/VerifyPackages.py
/usr/share/system-config-printer/troubleshoot/Welcome.py
/usr/share/system-config-printer/troubleshoot/__init__.py
/usr/share/system-config-printer/troubleshoot/base.py
/usr/share/system-config-printer/ui/AboutDialog.ui
/usr/share/system-config-printer/ui/ConnectDialog.ui
/usr/share/system-config-printer/ui/ConnectingDialog.ui
/usr/share/system-config-printer/ui/InstallDialog.ui
/usr/share/system-config-printer/ui/JobsWindow.ui
/usr/share/system-config-printer/ui/NewPrinterName.ui
/usr/share/system-config-printer/ui/NewPrinterWindow.ui
/usr/share/system-config-printer/ui/PrinterPropertiesDialog.ui
/usr/share/system-config-printer/ui/PrintersWindow.ui
/usr/share/system-config-printer/ui/SMBBrowseDialog.ui
/usr/share/system-config-printer/ui/ServerSettingsDialog.ui
/usr/share/system-config-printer/ui/WaitWindow.ui
/usr/share/system-config-printer/ui/statusicon_popupmenu.ui
/usr/share/system-config-printer/userdefault.py
/usr/share/system-config-printer/xdg/autostart/print-applet.desktop
/usr/share/system-config-printer/xml/preferreddrivers.rng
/usr/share/system-config-printer/xml/validate.py

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/system-config-printer/4cc77b90af91e615a64ae04893fdffa7939db84c

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/system-config-printer-applet.1
/usr/share/man/man1/system-config-printer.1

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*

%files services
%defattr(-,root,root,-)
/usr/lib/systemd/system/configure-printer@.service

%files locales -f system-config-printer.lang
%defattr(-,root,root,-)

