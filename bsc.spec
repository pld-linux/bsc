#
# TODO: optflags
# look this: http://dag.wieers.com/packages/bsc/bsc.spec
#
Summary:	Beesoft Commander - NC clone
Summary(pl):	Beesoft Commander - klon NC
Name:		bsc
Version:	2.27
Release:	0.1
License:	GPL
Group:		Applications
Source0:	http://www.beesoft.org/download/%{name}_%{version}_src.tar.gz
# Source0-md5:	9b67bc673bccae149ff8350a876b7720
Source1:	%{name}.desktop
Patch0:		%{name}-optflags.patch
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
qmake bsc.pro \
        QMAKE_CXX="%{__cxx}" \
        QMAKE_LINK="%{__cxx}" \
        QMAKE_CXXFLAGS_RELEASE="%{rpmcflags}" \
        QMAKE_RPATH=

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_desktopdir},%{_datadir}/%{name}/lang}
install bsc $RPM_BUILD_ROOT%{_bindir}
install bsc_*.qm $RPM_BUILD_ROOT%{_datadir}/%{name}/lang

install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog.txt
%attr(755,root,root) %{_bindir}/bsc
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/lang
%lang(cs) %{_datadir}/%{name}/lang/bsc_cs.qm
%lang(de) %{_datadir}/%{name}/lang/bsc_de.qm
%lang(es) %{_datadir}/%{name}/lang/bsc_es.qm
%lang(pl) %{_datadir}/%{name}/lang/bsc_pl.qm
%lang(ru) %{_datadir}/%{name}/lang/bsc_ru.qm
%{_desktopdir}/bsc.desktop
