# TODO
# - CC, optflags
Summary:	Squeeze is a simple application with a simple purpose - a batch image resizer
Name:		squeeze
Version:	0.2
Release:	2
License:	GPL v2
Group:		X11/Applications/Graphics
Source0:	http://squeeze.googlecode.com/files/%{name}-%{version}.tar.bz2
# Source0-md5:	6a996e78b8cf4b638b43a1eaed5fa967
URL:		http://code.google.com/p/squeeze/
BuildRequires:	QtCore-devel >= 4.3.0
BuildRequires:	QtGui-devel >= 4.3.0
BuildRequires:	qt4-build >= 4.3.3-3
BuildRequires:	qt4-qmake >= 4.3.3-3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Squeeze allows resizing of images in a batch mode. It is friendly and
usable and does one thing well - resizing images. It is a
multi-threaded application and is designed to run on Linux, Mac and
Windows.

%prep
%setup -q

%build
qmake-qt4 Makefile.qmake \
	"CONFIG %{!?debug:+}%{?debug:-}= release" \
	"CONFIG %{!?debug:-}%{?debug:+}= debug"
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}
install squeeze $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS
%attr(755,root,root) %{_bindir}/squeeze
