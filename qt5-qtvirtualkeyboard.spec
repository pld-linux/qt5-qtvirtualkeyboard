#
# Conditional build:
%bcond_without	doc	# Documentation
%bcond_without	lipi	# lipi-toolkit based handwriting

%define		orgname		qtvirtualkeyboard
%define		qtbase_ver		%{version}
%define		qtdeclarative_ver	%{version}
%define		qtquickcontrols2_ver	%{version}
%define		qtsvg_ver		%{version}
%define		qttools_ver		%{version}
Summary:	The Qt5 VirtualKeyboard library
Summary(pl.UTF-8):	Biblioteka Qt5 VirtualKeyboard
Name:		qt5-%{orgname}
Version:	5.15.14
Release:	1
License:	GPL v3+ or commercial
Group:		X11/Libraries
Source0:	https://download.qt.io/official_releases/qt/5.15/%{version}/submodules/%{orgname}-everywhere-opensource-src-%{version}.tar.xz
# Source0-md5:	3500a043b301b8301e0868525d768308
URL:		https://www.qt.io/
BuildRequires:	Qt5Core-devel >= %{qtbase_ver}
BuildRequires:	Qt5Gui-devel >= %{qtbase_ver}
BuildRequires:	Qt5Qml-devel >= %{qtdeclarative_ver}
BuildRequires:	Qt5Quick-devel >= %{qtdeclarative_ver}
BuildRequires:	Qt5Quick-controls2-devel >= %{qtquickcontrols2_ver}
BuildRequires:	Qt5Svg-devel >= %{qtsvg_ver}
BuildRequires:	hunspell-devel
BuildRequires:	libxcb-devel
BuildRequires:	pkgconfig
%if %{with doc}
BuildRequires:	qt5-assistant >= %{qttools_ver}
BuildRequires:	qt5-doc-common >= %{qttools_ver}
%endif
BuildRequires:	qt5-build >= %{qtbase_ver}
BuildRequires:	qt5-qmake >= %{qtbase_ver}
BuildRequires:	rpm-build >= 4.6
BuildRequires:	rpmbuild(macros) >= 2.016
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		specflags	-fno-strict-aliasing
%define		qt5dir		%{_libdir}/qt5

%description
Qt is a cross-platform application and UI framework. Using Qt, you can
write web-enabled applications once and deploy them across desktop,
mobile and embedded systems without rewriting the source code.

This package contains Qt5 VirtualKeyboard library.

%description -l pl.UTF-8
Qt to wieloplatformowy szkielet aplikacji i interfejsów użytkownika.
Przy użyciu Qt można pisać aplikacje powiązane z WWW i wdrażać je w
systemach biurkowych, przenośnych i wbudowanych bez przepisywania kodu
źródłowego.

Ten pakiet zawiera bibliotekę Qt5 VirtualKeyboard.

%package -n Qt5VirtualKeyboard
Summary:	The Qt5 VirtualKeyboard library
Summary(pl.UTF-8):	Biblioteka Qt5 VirtualKeyboard
Group:		X11/Libraries
Requires:	Qt5Core >= %{qtbase_ver}
Requires:	Qt5Gui >= %{qtbase_ver}
Requires:	Qt5Qml >= %{qtdeclarative_ver}
Requires:	Qt5Quick >= %{qtdeclarative_ver}

%description -n Qt5VirtualKeyboard
Qt5 VirtualKeyboard library.

%description -n Qt5VirtualKeyboard -l pl.UTF-8
Biblioteka Qt5 VirtualKeyboard.

%package -n Qt5VirtualKeyboard-devel
Summary:	Qt5 VirtualKeyboard - development files
Summary(pl.UTF-8):	Biblioteka Qt5 VirtualKeyboard - pliki programistyczne
Group:		X11/Development/Libraries
Requires:	Qt5Core-devel >= %{qtbase_ver}
Requires:	Qt5Gui-devel >= %{qtbase_ver}
Requires:	Qt5Qml-devel >= %{qtdeclarative_ver}
Requires:	Qt5Quick-devel >= %{qtdeclarative_ver}
Requires:	Qt5VirtualKeyboard = %{version}-%{release}

%description -n Qt5VirtualKeyboard-devel
Qt5 VirtualKeyboard - development files.

%description -n Qt5VirtualKeyboard-devel -l pl.UTF-8
Biblioteka Qt5 VirtualKeyboard - pliki programistyczne.

%package doc
Summary:	Qt5 VirtualKeyboard documentation in HTML format
Summary(pl.UTF-8):	Dokumentacja do biblioteki Qt5 VirtualKeyboard w formacie HTML
Group:		Documentation
Requires:	qt5-doc-common >= %{qtbase_ver}
BuildArch:	noarch

%description doc
Qt5 VirtualKeyboard documentation in HTML format.

%description doc -l pl.UTF-8
Dokumentacja do biblioteki Qt5 VirtualKeyboard w formacie HTML.

%package doc-qch
Summary:	Qt5 VirtualKeyboard documentation in QCH format
Summary(pl.UTF-8):	Dokumentacja do biblioteki Qt5 VirtualKeyboard w formacie QCH
Group:		Documentation
Requires:	qt5-doc-common >= %{qtbase_ver}
BuildArch:	noarch

%description doc-qch
Qt5 VirtualKeyboard documentation in QCH format.

%description doc-qch -l pl.UTF-8
Dokumentacja do biblioteki Qt5 VirtualKeyboard w formacie QCH.

%package examples
Summary:	Qt5 VirtualKeyboard examples
Summary(pl.UTF-8):	Przykłady do biblioteki Qt5 VirtualKeyboard
Group:		X11/Development/Libraries
BuildArch:	noarch

%description examples
Qt5 VirtualKeyboard examples.

%description examples -l pl.UTF-8
Przykłady do biblioteki Qt5 VirtualKeyboard.

%prep
%setup -q -n %{orgname}-everywhere-src-%{version}

%build
%{qmake_qt5} \
	%{?with_lipi:CONFIG+=handwriting}
%{__make}

%{?with_doc:%{__make} docs}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	INSTALL_ROOT=$RPM_BUILD_ROOT

%if %{with doc}
%{__make} install_docs \
	INSTALL_ROOT=$RPM_BUILD_ROOT
%endif

# useless symlinks
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libQt5*.so.5.??
# obsoleted by pkg-config
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libQt5*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-n Qt5VirtualKeyboard -p /sbin/ldconfig
%postun	-n Qt5VirtualKeyboard -p /sbin/ldconfig

%files -n Qt5VirtualKeyboard
%defattr(644,root,root,755)
%doc README.md dist/changes-*
# R: Qt5Core Qt5VirtualKeyboard hunspell
%attr(755,root,root) %{_libdir}/libQt5HunspellInputMethod.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libQt5HunspellInputMethod.so.5
# R: Qt5Core Qt5Gui Qt5Qml Qt5Quick libxcb libxcb-fixes
%attr(755,root,root) %{_libdir}/libQt5VirtualKeyboard.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libQt5VirtualKeyboard.so.5
# R: Qt5Core Qt5Gui Qt5Qml Qt5VirtualKeyboard
%attr(755,root,root) %{qt5dir}/plugins/platforminputcontexts/libqtvirtualkeyboardplugin.so
%dir %{qt5dir}/plugins/virtualkeyboard
# R: Qt5Core Qt5Qml Qt5VirtualKeyboard
%attr(755,root,root) %{qt5dir}/plugins/virtualkeyboard/libqtvirtualkeyboard_hangul.so
# R: Qt5Core Qt5HunspellInputMethod Qt5Qml Qt5VirtualKeyboard
%attr(755,root,root) %{qt5dir}/plugins/virtualkeyboard/libqtvirtualkeyboard_hunspell.so
%if %{with lipi}
# R: Qt5Core Qt5HunspellInputMethod Qt5Qml Qt5VirtualKeyboard
%attr(755,root,root) %{qt5dir}/plugins/virtualkeyboard/libqtvirtualkeyboard_lipi.so
%endif
# R: Qt5Core Qt5Gui Qt5Qml Qt5VirtualKeyboard
%attr(755,root,root) %{qt5dir}/plugins/virtualkeyboard/libqtvirtualkeyboard_openwnn.so
# R: Qt5Core Qt5Qml Qt5VirtualKeyboard
%attr(755,root,root) %{qt5dir}/plugins/virtualkeyboard/libqtvirtualkeyboard_pinyin.so
# R: Qt5Core Qt5Qml Qt5VirtualKeyboard
%attr(755,root,root) %{qt5dir}/plugins/virtualkeyboard/libqtvirtualkeyboard_tcime.so
# R: Qt5Core Qt5HunspellInputMethod Qt5Qml Qt5VirtualKeyboard
%attr(755,root,root) %{qt5dir}/plugins/virtualkeyboard/libqtvirtualkeyboard_thai.so
%dir %{qt5dir}/qml/QtQuick/VirtualKeyboard
# R: Qt5Core Qt5Qml Qt5VirtualKeyboard
%attr(755,root,root) %{qt5dir}/qml/QtQuick/VirtualKeyboard/libqtquickvirtualkeyboardplugin.so
%{qt5dir}/qml/QtQuick/VirtualKeyboard/plugins.qmltypes
%{qt5dir}/qml/QtQuick/VirtualKeyboard/qmldir
%dir %{qt5dir}/qml/QtQuick/VirtualKeyboard/Settings
# R: Qt5Core Qt5Qml Qt5VirtualKeyboard
%attr(755,root,root) %{qt5dir}/qml/QtQuick/VirtualKeyboard/Settings/libqtquickvirtualkeyboardsettingsplugin.so
%{qt5dir}/qml/QtQuick/VirtualKeyboard/Settings/plugins.qmltypes
%{qt5dir}/qml/QtQuick/VirtualKeyboard/Settings/qmldir
%dir %{qt5dir}/qml/QtQuick/VirtualKeyboard/Styles
# R: Qt5Core Qt5Gui Qt5Qml Qt5Quick Qt5Svg
%attr(755,root,root) %{qt5dir}/qml/QtQuick/VirtualKeyboard/Styles/libqtquickvirtualkeyboardstylesplugin.so
%{qt5dir}/qml/QtQuick/VirtualKeyboard/Styles/plugins.qmltypes
%{qt5dir}/qml/QtQuick/VirtualKeyboard/Styles/qmldir
%if %{with lipi}
%dir %{qt5dir}/plugins/lipi_toolkit
%attr(755,root,root) %{qt5dir}/plugins/lipi_toolkit/libactivedtw.so
%attr(755,root,root) %{qt5dir}/plugins/lipi_toolkit/libboxfld.so
%attr(755,root,root) %{qt5dir}/plugins/lipi_toolkit/libl7.so
%attr(755,root,root) %{qt5dir}/plugins/lipi_toolkit/liblipiengine.so
%attr(755,root,root) %{qt5dir}/plugins/lipi_toolkit/liblogger.so
%attr(755,root,root) %{qt5dir}/plugins/lipi_toolkit/libneuralnet.so
%attr(755,root,root) %{qt5dir}/plugins/lipi_toolkit/libnn.so
%attr(755,root,root) %{qt5dir}/plugins/lipi_toolkit/libnpen.so
%attr(755,root,root) %{qt5dir}/plugins/lipi_toolkit/libpointfloat.so
%attr(755,root,root) %{qt5dir}/plugins/lipi_toolkit/libpreproc.so
%attr(755,root,root) %{qt5dir}/plugins/lipi_toolkit/libsubstroke.so
%dir %{_datadir}/qt5/qtvirtualkeyboard
%{_datadir}/qt5/qtvirtualkeyboard/lipi_toolkit
%endif

%files -n Qt5VirtualKeyboard-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libQt5HunspellInputMethod.so
%attr(755,root,root) %{_libdir}/libQt5VirtualKeyboard.so
%{_libdir}/libQt5HunspellInputMethod.prl
%{_libdir}/libQt5VirtualKeyboard.prl
%{_includedir}/qt5/QtHunspellInputMethod
%{_includedir}/qt5/QtVirtualKeyboard
%{_pkgconfigdir}/Qt5VirtualKeyboard.pc
%{_libdir}/cmake/Qt5Gui/Qt5Gui_QVirtualKeyboardPlugin.cmake
%{_libdir}/cmake/Qt5HunspellInputMethod
%{_libdir}/cmake/Qt5VirtualKeyboard
%{qt5dir}/mkspecs/modules/qt_lib_hunspellinputmethod_private.pri
%{qt5dir}/mkspecs/modules/qt_lib_virtualkeyboard.pri
%{qt5dir}/mkspecs/modules/qt_lib_virtualkeyboard_private.pri

%if %{with doc}
%files doc
%defattr(644,root,root,755)
%{_docdir}/qt5-doc/qtvirtualkeyboard

%files doc-qch
%defattr(644,root,root,755)
%{_docdir}/qt5-doc/qtvirtualkeyboard.qch
%endif

%files examples
%defattr(644,root,root,755)
# XXX: dir shared with qt5-qtbase-examples
%dir %{_examplesdir}/qt5
%{_examplesdir}/qt5/virtualkeyboard
