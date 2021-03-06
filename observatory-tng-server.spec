Name:      observatory-tng-server
Version:   2.3.3
Release:   0
Url:       https://github.com/warwick-one-metre/tngd
Summary:   TNG weather feed client for the Warwick La Palma telescopes.
License:   GPL-3.0
Group:     Unspecified
BuildArch: noarch
Requires:  python3, python3-Pyro4, python3-requests, python3-warwick-observatory-common
Requires:  observatory-log-client, %{?systemd_requires}

%description
Part of the observatory software for the Warwick La Palma telescopes.

tngd is a Pyro frontend for querying the TNG weather feed via http.

%build
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_unitdir}

%{__install} %{_sourcedir}/tngd %{buildroot}%{_bindir}
%{__install} %{_sourcedir}/tngd.service %{buildroot}%{_unitdir}

%post
%systemd_post tngd.service

%preun
%systemd_preun tngd.service

%postun
%systemd_postun_with_restart tngd.service

%files
%defattr(0755,root,root,-)
%{_bindir}/tngd
%defattr(-,root,root,-)
%{_unitdir}/tngd.service

%changelog
