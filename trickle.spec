# TODO:
# - iniscript needed
# - split into client and daemon
Summary:	portable lightweight userspace bandwidth shaper
Name:		trickle
Version:	1.07
Release:	0.6
License:	BSD
Group:		Applications/Networking
Source0:	http://www.monkey.org/~marius/trickle/%{name}-%{version}.tar.gz
# Source0-md5:	860ebc4abbbd82957c20a28bd9390d7d
Patch0:		%{name}-build.patch
Patch1:		%{name}-fwrite.patch
Patch2:		%{name}-1.07-CVE-2009-0415.patch
Patch3:		%{name}-1.07-bwsta_getdelay-stop-if-no-packets.patch
Patch4:		%{name}-1.07-include_netdb.patch
Patch5:		%{name}-1.07-libdir.patch
URL:		http://www.monkey.org/~marius/trickle/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libevent-devel
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# FIXME
%define		filterout_c	-Werror=format-security

%description
trickle is a portable lightweight userspace bandwidth shaper. It can
run in collaborative mode (together with trickled) or in stand alone
mode.

trickle works by taking advantage of the unix loader preloading.
Essentially it provides, to the application, a new version of the
functionality that is required to send and receive data through
sockets. It then limits traffic based on delaying the sending and
receiving of data over a socket. trickle runs entirely in userspace
and does not require root privileges.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1

%build
# ugly hack
:> .c
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_sysconfdir}

%{__make} install \
	DESTDIR="$RPM_BUILD_ROOT"

cp -p trickled.conf $RPM_BUILD_ROOT%{_sysconfdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE README TODO
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/trickled.conf
%attr(755,root,root) %{_bindir}/trickle
%attr(755,root,root) %{_bindir}/tricklectl
%attr(755,root,root) %{_bindir}/trickled
%attr(755,root,root) %{_libdir}/trickle
%{_mandir}/man1/trickle.1*
%{_mandir}/man5/trickled.conf.5*
%{_mandir}/man8/trickled.8*
