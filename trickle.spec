# TODO:
# - doesn't build
# - iniscript needed
# - split into client and daemon
Summary:	portable lightweight userspace bandwidth shaper
Name:		trickle
Version:	1.06
Release:	0.1
License:	BSD
Group:		Applications/Networking
Source0:	http://www.monkey.org/~marius/trickle/%{name}-%{version}.tar.gz
# Source0-md5:	8e9b7fcdd49ee8fb94700dd1653f5537
URL:		http://www.monkey.org/~marius/trickle/
BuildRequires:	libevent-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

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

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR="$RPM_BUILD_ROOT"

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE README TODO
%{_mandir}/man1/trickle.1*
%{_mandir}/man5/trickled.conf.5*
%{_mandir}/man8/trickled.8*
%attr(755,root,root) %{_bindir}/trickle
%attr(755,root,root) %{_bindir}/tricklectl
%attr(755,root,root) %{_bindir}/trickled
%{_libdir}/trickle/
