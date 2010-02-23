Summary:	Squash - a simple application with a simple purpose - a batch image resizer
Summary(pl.UTF-8):	Squash - prosta aplikacja o prostym zastosowaniu - wsadowe skalowanie obrazów
Name:		squash
Version:	0.3
Release:	1
License:	GPL v2
Group:		X11/Applications/Graphics
Source0:	http://squash.googlecode.com/files/%{name}-%{version}.tar.bz2
# Source0-md5:	a5984bfbf4e61d222582a17a1dd93ccc
Source1:	%{name}.desktop
URL:		http://code.google.com/p/squash/
BuildRequires:	QtCore-devel >= 4.3.0
BuildRequires:	QtGui-devel >= 4.3.0
BuildRequires:	qt4-build >= 4.3.3-3
BuildRequires:	qt4-qmake >= 4.3.3-3
Obsoletes:	squeeze < 0.3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Squash allows resizing of images in a batch mode. It is friendly and
usable and does one thing well - resizing images. It is a
multi-threaded application and is designed to run on Linux, Mac and
Windows.

%description -l pl.UTF-8
Squash umożliwia zmianę rozmiaru obrazów w trybie wsadowym. Jest
przyjazny w użyciu i wykonuje swoje jedyne zadanie bardzo dobrze. Jest
aplikacją wielowątkową, zaprojektowaną do uruchamiania pod Linuksem,
MacOS-em i Windows.

%prep
%setup -q

sed -i -e 's,-O3,%{rpmcxxflags} %{rpmcppflags},;s,-gstabs+,,' Makefile.qmake

%build
qmake-qt4 Makefile.qmake \
	"CONFIG %{!?debug:+}%{?debug:-}= release" \
	"CONFIG %{!?debug:-}%{?debug:+}= debug"
%{__make} \
	CXX="%{__cxx}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_desktopdir},%{_pixmapsdir},%{_bindir}}
install -p squash $RPM_BUILD_ROOT%{_bindir}
cp -a %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}
cp -a qrc/squash.png $RPM_BUILD_ROOT%{_pixmapsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS
%attr(755,root,root) %{_bindir}/squash
%{_desktopdir}/squash.desktop
%{_pixmapsdir}/squash.png
