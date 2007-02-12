Summary:	xtail watches the growth of files
Summary(pl.UTF-8):   xtail obserwuje przyrost zawartości plików
Name:		xtail
Version:	2.1
Release:	1
License:	GPL v2
Group:		Applications/System
Source0:	http://www.unicom.com/sw/xtail/%{name}-%{version}.tar.gz
# Source0-md5:	2e4717c591a2cbbd4aeb63d00c87a0cb
Patch0:		%{name}-Makefile.patch
URL:		http://www.unicom.com/sw/xtail/
BuildRequires:	autoconf
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
xtail is sort of a tail -f for many files. It's a great way to monitor
log files.

%description -l pl.UTF-8
xtail działa jak polecenie tail -f, ale dla wielu plików jednocześnie.
Jest bardzo dobrym sposobem na monitorowanie logów.

%prep
%setup -q
%patch0 -p0

%build
chmod u+w configure
%{__autoconf}
%{__autoheader}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/xtail
%{_mandir}/man1/*
