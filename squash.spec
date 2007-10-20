Summary:	Squeeze is a simple application with a simple purpose - a batch image resizer
Name:		squeeze
Version:	0.2
Release:	0.1
License:	GPL v2
Group:		X11/Applications/Graphics
Source0:	http://squeeze.googlecode.com/files/%{name}-%{version}.tar.bz2
# Source0-md5:	6a996e78b8cf4b638b43a1eaed5fa967
URL:		http://code.google.com/p/squeeze/
BuildRequires:	QtCore-devel
BuildRequires:	QtGui-devel
BuildRequires:	qt4-build
BuildRequires:	qt4-qmake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Squeeze allows resizing of images in a batch mode. It is friendly and
usable and does one thing well - resizing images. It is a
multi-threaded application and is designed to run on Linux, Mac and
Windows.

%prep
%setup -q

%build
qt4-qmake Makefile.qmake "CONFIG %{!?debug:+}%{?debug:-}= release" "CONFIG %{!?debug:-}%{?debug:+}= debug"
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -ls

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS
