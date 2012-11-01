%define oname qutim

%define _disable_ld_as_needed 1

%define coreversion		0.2.1.git.630
%define icqversion		0.2.1.136
%define ircversion		0.2.0.38
%define jabberversion		0.2.1.431
%define mrimversion		0.2.1.146
%define vkontakteversion	0.2.0.40
%define yandexnarodversion	0.2.0.21
%define histmanversion		0.2.0.13
%define juickversion		0.2.1.100
%define weatherversion		0.2.1.145
%define massmessagingversion	0.2.1.120
%define plugmanversion		0.2.0.151
%define imagepubversion		10
%define kdeversion		31
%define msnversion		6
%define urlpreviewversion	12
%define cchkversion		0.0.7
%define twitterversion		4

Name:		qutim2
Version:	%{coreversion}
Release:	0.1
Summary:	qutIM - multiplatform multiprotocol (ICQ, Jabber etc) instant messenger
Group:		Networking/Instant messaging
License:	GPLv2
URL:		http://qutim.org/
Source0:	%{oname}-%{coreversion}.tar.bz2
Source1:	qutim-emoticons-0.2.0.tar.bz2
Source2:	qutim-langs-0.2.0.tar.bz2
Source3:	qutim-sounds-0.2.0.tar.bz2
Source4:	qutIM.desktop
Source5:	TributeToQIP.tar.bz2
Source6:	qutim-glass.tar.bz2
Source7:	qutim-red.tar.bz2
Source8:	additional_plugins.tar.bz2
Patch0:		qutim-0.2.0-x86_64.patch
Patch1:		qutim-msn-3-cmake.patch
Patch2:		qutim-0.2.1.git.630-gcc4.7.patch
Patch3:		qutim-0.2.1.git.630-linkage.patch
Patch4:		qutim-0.2.1.git.630-speller.patch
Patch5:		qutim-0.2.1.git.630-qt4.8.patch
BuildRequires:	qt4-devel
BuildRequires:	idn-devel
BuildRequires:	gnutls-devel
BuildRequires:	cmake
BuildRequires:	phonon-devel
BuildRequires:	kdelibs4-devel
Conflicts:	%{oname} >= 0.2.80

%description
qutIM - multiplatform multiprotocol (ICQ, Jabber) instant messenger.

%package -n %{name}-icq
Summary:	ICQ plugin for qutIM
Group:		Networking/Instant messaging
Version:	%{icqversion}
Requires:	%{name} = %{coreversion}

%description -n %{name}-icq
ICQ plugin for qutIM.

%package -n %{name}-jabber
Summary:	Jabber plugin for qutIM
Group:		Networking/Instant messaging
Version:	%{jabberversion}
Requires:	%{name} = %{coreversion}

%description -n %{name}-jabber
Jabber plugin for qutIM.

%package -n %{name}-irc
Summary:	IRC plugin for qutIM
Group:		Networking/Instant messaging
Version:	%{ircversion}
Requires:	%{name} = %{coreversion}

%description -n %{name}-irc
IRC plugin for qutIM.

%package -n %{name}-mrim
Summary:	Mail.ru plugin for qutIM
Group:		Networking/Instant messaging
Version:	%{mrimversion}
Requires:	%{name} = %{coreversion}

%description -n %{name}-mrim
Mail.ru plugin for qutIM.

%package -n %{name}-msn
Summary:	MSN plugin for qutIM
Group:		Networking/Instant messaging
Version:	%{msnversion}
Requires:	%{name} = %{coreversion}

%description -n %{name}-msn
MSN plugin for qutIM.

%package -n %{name}-vkontakte
Summary:	Vkontakte.ru plugin for qutIM
Group:		Networking/Instant messaging
Version:	%{vkontakteversion}
Requires:	%{name} = %{coreversion}

%description -n %{name}-vkontakte
Vkontakte.ru plugin for qutIM.

%package -n %{name}-imagepub
Summary:	Image publishing services plugin for qutIM
Group:		Networking/Instant messaging
Version:	%{imagepubversion}
Requires:	%{name} = %{coreversion}

%description -n %{name}-imagepub
Image publishing services plugin for qutIM.

%package -n %{name}-massmessaging
Summary:	Mass messaging plugin for qutIM
Group:		Networking/Instant messaging
Version:	%{massmessagingversion}
Requires:	%{name} = %{coreversion}

%description -n %{name}-massmessaging
Mass messaging plugin for qutIM.


%package -n %{name}-juick
Summary:	Weather plugin for qutIM
Group:		Networking/Instant messaging
Version:	%{juickversion}
Requires:	%{name} = %{coreversion}

%description -n %{name}-juick
juick plugin for qutIM.

%package -n %{name}-weather
Summary:	Weather plugin for qutIM
Group:		Networking/Instant messaging
Version:	%{weatherversion}
Requires:	%{name} = %{coreversion}

%description -n %{name}-weather
Weather plugin for qutIM.

%package -n %{name}-urlpreview
Summary:	Prewiew URLs in messages plugin for qutIM
Group:		Networking/Instant messaging
Version:	%{urlpreviewversion}
Requires:	%{name} = %{coreversion}

%description -n %{name}-urlpreview
Prewiew URLs in messages plugin for qutIM.

%package -n %{name}-yandexnarod
Summary:	Yandex.narod.ru plugin for qutIM
Group:		Networking/Instant messaging
Version:	%{yandexnarodversion}
Requires:	%{name} = %{coreversion}

%description -n %{name}-yandexnarod
Yandex.narod.ru plugin for qutIM. Requires narod.ru account.

%package -n %{name}-twitter
Summary:	Twitter plugin for qutIM
Group:		Networking/Instant messaging
Version:	%{twitterversion}
Requires:	%{name} = %{coreversion}

%description -n %{name}-twitter
Twitter plugin for qutIM.

%package -n %{name}-histman
Summary:	History manager plugin for qutIM
Group:		Networking/Instant messaging
Version:	%{histmanversion}
Requires:	%{name} = %{coreversion}

%description -n %{name}-histman
History manager plugin for qutIM. Import history from clients
like QIP, Miranda, Pidgin, Kopete, Gajim, Psi and others.

%package -n %{name}-plugman
Summary:	Plugin manager for qutIM
Group:		Networking/Instant messaging
Version:	%{plugmanversion}
Requires:	%{name} = %{coreversion}

%description -n %{name}-plugman
Plugin manager for qutIM. Allow install additional themes,
icon packs and other useful staff.

%package -n %{name}-kde-integration
Summary:	KDE integration plugin set for qutIM
Group:		Networking/Instant messaging
Version:	%{kdeversion}
Requires:	%{name} = %{coreversion}

%description -n %{name}-kde-integration
KDE integration plugin set for qutIM.

%package -n task-%{name}
Summary:	Task for qutIM with Jabber & ICQ plugins
Group:		Networking/Instant messaging
Version:	%{coreversion}
Requires:	%{name} = %{coreversion}
Requires:	%{name}-icq = %{icqversion}
Requires:	%{name}-jabber = %{jabberversion}

%description -n task-%{name}
Metapackage for qutIM + Jabber & ICQ plugins.

%prep
%setup -q -n %{oname}-%{version}
%patch0 -p0
pushd plugins
tar xvjf %{SOURCE8}
popd
%patch1 -p0
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1

tar xvjf %{SOURCE1}
tar xvjf %{SOURCE2}
tar xvjf %{SOURCE3}

%build
%cmake_qt4 -DCMAKE_SKIP_RPATH=TRUE
%make

pushd ../plugins/icq
%qmake_qt4
%make
popd

pushd ../plugins/jabber
%cmake_qt4 -DGNUTLS=1
%make
popd

pushd ../plugins/irc
%qmake_qt4
%make
popd

pushd ../plugins/kde-integration
%cmake_kde4
%make
popd

pushd ../plugins/mrim
%cmake_qt4
%make
popd

pushd ../plugins/msn
%cmake_qt4
%make
popd

pushd ../plugins/vkontakte
%qmake_qt4
%make
popd

pushd ../plugins/imagepub
%qmake_qt4
%make
popd


pushd ../plugins/massmessaging
%qmake_qt4
%make
popd

pushd ../plugins/weather
%qmake_qt4
%make
popd

pushd ../plugins/juick
%qmake_qt4
%make
popd

pushd ../plugins/urlpreview
%qmake_qt4
%make
popd

pushd ../plugins/yandexnarod
%qmake_qt4
%make
popd

pushd ../plugins/histman
%qmake_qt4
%make
popd

pushd ../plugins/twitter
%qmake_qt4
%make
popd

pushd ../plugins/plugman
%cmake_qt4
%make
popd

%install
install -D -m 0644 "icons/qutim_64.png" "%{buildroot}%{_datadir}/pixmaps/%{oname}.png"
install -d "%{buildroot}%{_bindir}"
install -d "%{buildroot}%{_datadir}"/applications/
install -d "%{buildroot}%{_libdir}/%{oname}"
install -d "%{buildroot}%{_datadir}/%{oname}/languages/ru"
install -d "%{buildroot}%{_datadir}/%{oname}/webkitstyle"

cp "build/%{oname}" "%{buildroot}%{_bindir}/%{oname}"
cp %{SOURCE4} "%{buildroot}%{_datadir}/applications/%{oname}.desktop"
cp "plugins/icq/liboscar.so" "%{buildroot}%{_libdir}/%{oname}/liboscar.so"
cp "plugins/jabber/build/libjabber.so" "%{buildroot}%{_libdir}/%{oname}/libjabber.so"
cp "plugins/irc/libirc.so" "%{buildroot}%{_libdir}/%{oname}/libirc.so"
cp "plugins/mrim/build/libmrim.so" "%{buildroot}%{_libdir}/%{oname}/libmrim.so"
cp "plugins/msn/build/libmsn.so" "%{buildroot}%{_libdir}/%{oname}/libmsn.so"
cp "plugins/vkontakte/libvkontakte.so" "%{buildroot}%{_libdir}/%{oname}/libvkontakte.so"
cp "plugins/imagepub/libimagepub.so" "%{buildroot}%{_libdir}/%{oname}/libimagepub.so"
cp "plugins/massmessaging/libmassmessaging.so" "%{buildroot}%{_libdir}/%{oname}/libmassmessaging.so"
cp "plugins/juick/libjuick.so" "%{buildroot}%{_libdir}/%{oname}/libjuick.so"
cp "plugins/weather/libweather.so" "%{buildroot}%{_libdir}/%{oname}/libweather.so"
cp "plugins/urlpreview/liburlpreview.so" "%{buildroot}%{_libdir}/%{oname}/liburlpreview.so"
cp "plugins/yandexnarod/libyandexnarod.so" "%{buildroot}%{_libdir}/%{oname}/libyandexnarod.so"
cp "plugins/histman/libhistman.so" "%{buildroot}%{_libdir}/%{oname}/libhistman.so"
cp "plugins/twitter/libtwitter.so" "%{buildroot}%{_libdir}/%{oname}/libtwitter.so"
cp "plugins/plugman/build/libplugman.so" "%{buildroot}%{_libdir}/%{oname}/libplugman.so"

cp plugins/kde-integration/build/lib/libkde*.so %{buildroot}%{_libdir}/%{oname}/

cp -R "emoticons" "%{buildroot}%{_datadir}/%{oname}/"
cp -R languages/ru/*.qm "%{buildroot}%{_datadir}/%{oname}/languages/ru"
cp -R "sounds" "%{buildroot}%{_datadir}/%{oname}/"
cd "%{buildroot}%{_datadir}/%{oname}/webkitstyle"
tar xvjf %{SOURCE5}
tar xvjf %{SOURCE6}
tar xvjf %{SOURCE7}

%files
%{_bindir}/%{oname}
%{_datadir}/applications/%{oname}.desktop
%{_datadir}/pixmaps/%{oname}.png
%{_datadir}/%{oname}

%files -n %{name}-icq
%{_libdir}/%{oname}/liboscar.so

%files -n %{name}-irc
%{_libdir}/%{oname}/libirc.so

%files -n %{name}-mrim
%{_libdir}/%{oname}/libmrim.so

%files -n %{name}-jabber
%{_libdir}/%{oname}/libjabber.so

%files -n %{name}-msn
%{_libdir}/%{oname}/libmsn.so

%files -n %{name}-weather
%{_libdir}/%{oname}/libweather.so

%files -n %{name}-juick
%{_libdir}/%{oname}/libjuick.so

%files -n %{name}-massmessaging
%{_libdir}/%{oname}/libmassmessaging.so

%files -n %{name}-vkontakte
%{_libdir}/%{oname}/libvkontakte.so

%files -n %{name}-imagepub
%{_libdir}/%{oname}/libimagepub.so

%files -n %{name}-urlpreview
%{_libdir}/%{oname}/liburlpreview.so

%files -n %{name}-yandexnarod
%{_libdir}/%{oname}/libyandexnarod.so

%files -n %{name}-twitter
%{_libdir}/%{oname}/libtwitter.so

%files -n %{name}-histman
%{_libdir}/%{oname}/libhistman.so

%files -n %{name}-plugman
%{_libdir}/%{oname}/libplugman.so

%files -n %{name}-kde-integration
%{_libdir}/%{oname}/libkde*.so

%files -n task-%{name}


%changelog
* Mon Sep 19 2011 Alexander Barakin <abarakin@mandriva.org> 0.2.1.git.630-1mdv2010.1
+ Revision: 700312
- imported package qutim

* Mon Apr 11 2011 Eugeni Dodonov <eugeni@mandriva.com> 0.2.0.529-1
+ Revision: 652698
- Remove connectioncheck plugin for now, does not compiles with gcc 4.6.
- Fix building, cleanup spec.
- Imported qutim to cooker, based on MIB package by Andrey Bondrov
  <bondrov@math.dvgu.ru>.
- Created package structure for qutim.

