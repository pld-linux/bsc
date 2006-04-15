#
# TODO: optflags
# look this: http://dag.wieers.com/packages/bsc/bsc.spec
#
Summary:	Beesoft Commander - NC clone
Summary(pl):	Beesoft Commander - klon NC
Name:		bsc
Version:	2.18
Release:	0.1
License:	GPL
Group:		Applications
Source0:	http://www.beesoft.org/download/%{name}_%{version}_src.tar.gz
# Source0-md5:	19f9bd6d3026bc9a2efa3c99efdcddf2
#Source1:	%{name}.desktop
URL:		http://www.beesoft.org/bsc.html
BuildRequires:	qmake
BuildRequires:	qt-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Beesoft Commander is a Qt file manager (like Norton Commander) for
Linux.

%description -l pl
Beesoft Commander to oparty na Qt zarz±dca plików (podobny do Norton
Commandera) dla Linuksa.

%prep
%setup -q -n %{name}

%build
export QTDIR=%{_prefix}
qmake bsc.pro
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_desktopdir}}
install bsc $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
#%doc readme.txt
%attr(755,root,root) %{_bindir}/bsc
#%{_desktopdir}/*.desktop
