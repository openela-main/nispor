Name:           nispor
Version:        1.2.10
Release:        1%{?dist}
Summary:        API for network status querying
License:        ASL 2.0
URL:            https://github.com/nispor/nispor
Source:         https://github.com/nispor/nispor/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        https://github.com/nispor/nispor/releases/download/v%{version}/nispor-vendor-%{version}.tar.xz
BuildRequires:  pkg-config
BuildRequires:  python3-devel
BuildRequires:  rust-toolset
BuildRequires:  systemd-rpm-macros
BuildRequires:  systemd-devel

Provides: bundled(crate(aho-corasick)) = 0.7.18
Provides: bundled(crate(ansi_term)) = 0.12.1
Provides: bundled(crate(anyhow)) = 1.0.58
Provides: bundled(crate(atty)) = 0.2.14
Provides: bundled(crate(autocfg)) = 1.1.0
Provides: bundled(crate(bitflags)) = 1.3.2
Provides: bundled(crate(byteorder)) = 1.4.3
Provides: bundled(crate(bytes)) = 1.1.0
Provides: bundled(crate(cfg-if)) = 1.0.0
Provides: bundled(crate(clap)) = 3.2.6
Provides: bundled(crate(clap_lex)) = 0.2.3
Provides: bundled(crate(ctor)) = 0.1.22
Provides: bundled(crate(diff)) = 0.1.12
Provides: bundled(crate(env_logger)) = 0.9.0
Provides: bundled(crate(ethtool)) = 0.2.3
Provides: bundled(crate(futures)) = 0.3.21
Provides: bundled(crate(futures-channel)) = 0.3.21
Provides: bundled(crate(futures-core)) = 0.3.21
Provides: bundled(crate(futures-executor)) = 0.3.21
Provides: bundled(crate(futures-io)) = 0.3.21
Provides: bundled(crate(futures-macro)) = 0.3.21
Provides: bundled(crate(futures-sink)) = 0.3.21
Provides: bundled(crate(futures-task)) = 0.3.21
Provides: bundled(crate(futures-util)) = 0.3.21
Provides: bundled(crate(genetlink)) = 0.2.3
Provides: bundled(crate(hashbrown)) = 0.12.1
Provides: bundled(crate(hermit-abi)) = 0.1.19
Provides: bundled(crate(humantime)) = 2.1.0
Provides: bundled(crate(indexmap)) = 1.9.1
Provides: bundled(crate(itoa)) = 1.0.2
Provides: bundled(crate(libc)) = 0.2.126
Provides: bundled(crate(linked-hash-map)) = 0.5.4
Provides: bundled(crate(log)) = 0.4.17
Provides: bundled(crate(memchr)) = 2.5.0
Provides: bundled(crate(mio)) = 0.8.4
Provides: bundled(crate(mptcp-pm)) = 0.1.1
Provides: bundled(crate(netlink-packet-core)) = 0.4.2
Provides: bundled(crate(netlink-packet-generic)) = 0.3.1
Provides: bundled(crate(netlink-packet-route)) = 0.12.0
Provides: bundled(crate(netlink-packet-utils)) = 0.5.1
Provides: bundled(crate(netlink-proto)) = 0.10.0
Provides: bundled(crate(netlink-sys)) = 0.8.3
Provides: bundled(crate(nix)) = 0.24.1
Provides: bundled(crate(once_cell)) = 1.12.0
Provides: bundled(crate(os_str_bytes)) = 6.1.0
Provides: bundled(crate(output_vt100)) = 0.1.3
Provides: bundled(crate(paste)) = 1.0.7
Provides: bundled(crate(pin-project-lite)) = 0.2.9
Provides: bundled(crate(pin-utils)) = 0.1.0
Provides: bundled(crate(pretty_assertions)) = 1.2.1
Provides: bundled(crate(proc-macro2)) = 1.0.40
Provides: bundled(crate(quote)) = 1.0.20
Provides: bundled(crate(regex)) = 1.5.6
Provides: bundled(crate(regex-syntax)) = 0.6.26
Provides: bundled(crate(rtnetlink)) = 0.10.1
Provides: bundled(crate(ryu)) = 1.0.10
Provides: bundled(crate(serde)) = 1.0.137
Provides: bundled(crate(serde_derive)) = 1.0.137
Provides: bundled(crate(serde_json)) = 1.0.81
Provides: bundled(crate(serde_yaml)) = 0.8.24
Provides: bundled(crate(slab)) = 0.4.6
Provides: bundled(crate(socket2)) = 0.4.4
Provides: bundled(crate(strsim)) = 0.10.0
Provides: bundled(crate(syn)) = 1.0.98
Provides: bundled(crate(termcolor)) = 1.1.3
Provides: bundled(crate(textwrap)) = 0.15.0
Provides: bundled(crate(thiserror)) = 1.0.31
Provides: bundled(crate(thiserror-impl)) = 1.0.31
Provides: bundled(crate(tokio)) = 1.19.2
Provides: bundled(crate(tokio-macros)) = 1.8.0
Provides: bundled(crate(unicode-ident)) = 1.0.1
Provides: bundled(crate(wasi)) = 0.11.0
Provides: bundled(crate(winapi)) = 0.3.9
Provides: bundled(crate(winapi-i686-pc-windows-gnu)) = 0.4.0
Provides: bundled(crate(winapi-util)) = 0.1.5
Provides: bundled(crate(winapi-x86_64-pc-windows-gnu)) = 0.4.0
Provides: bundled(crate(windows-sys)) = 0.36.1
Provides: bundled(crate(windows_aarch64_msvc)) = 0.36.1
Provides: bundled(crate(windows_i686_gnu)) = 0.36.1
Provides: bundled(crate(windows_i686_msvc)) = 0.36.1
Provides: bundled(crate(windows_x86_64_gnu)) = 0.36.1
Provides: bundled(crate(windows_x86_64_msvc)) = 0.36.1
Provides: bundled(crate(yaml-rust)) = 0.4.5

%description
Unified interface for Linux network state querying.

%package -n     python3-%{name}
Summary:        %{summary}
Requires:       nispor = %{?epoch:%{epoch}:}%{version}-%{release}
BuildArch:      noarch

%description -n python3-%{name}

This package contains python3 binding of %{name}.

%package        devel
Summary:        %{summary}
Requires:       nispor%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}

%description devel

This package contains C binding of %{name}.

%prep
%autosetup -p1

# Source1 is vendored dependencies
%cargo_prep -V 1

# The cargo_prep will create `.cargo/config` which take precedence over
# `.cargo/config.toml` shipped by upstream which fix the SONAME of cdylib.
# To workaround that, merge upstream rustflags into cargo_prep created one.
_FLAGS=`sed -ne 's/rustflags = "\(.\+\)"/\1/p' .cargo/config.toml`
sed -i -e "s/rustflags = \[\(.\+\), \]$/rustflags = [\1, \"$_FLAGS\"]/" \
    .cargo/config

%build
make
pushd src/python
%py3_build
popd

%post
/sbin/ldconfig

%postun
/sbin/ldconfig

%install
env SKIP_PYTHON_INSTALL=1 PREFIX=%{_prefix} LIBDIR=%{_libdir} %make_install

pushd src/python
%py3_install
popd

%files
%doc AUTHORS CHANGELOG DEVEL.md README.md
%license LICENSE
%{_bindir}/npc
%{_libdir}/libnispor.so.*

%files -n       python3-%{name}
%license LICENSE
%{python3_sitelib}/nispor*

%files devel
%license LICENSE
%{_libdir}/libnispor.so
%{_includedir}/nispor.h
%{_libdir}/pkgconfig/nispor.pc

%changelog
* Thu Feb 16 2023 Gris Ge <fge@redhat.com> - 1.2.10-1
- Upgrade to 1.2.10. RHBZ#2153166

* Thu Dec 15 2022 Gris Ge <fge@redhat.com> - 1.2.9-1
- Upgrade to 1.2.9. RHBZ#2153166

* Tue Jul 26 2022 Gris Ge <fge@redhat.com> - 1.2.7-1
- Upgrade to 1.2.7. RHBZ#2064295

* Tue Apr 12 2022 Gris Ge <fge@redhat.com> - 1.2.5-1
- Upgrade to 1.2.5. RHBZ#2064295

* Tue Mar 15 2022 Gris Ge <fge@redhat.com> - 1.2.4-1
- Upgrade to 1.2.4. RHBZ#2064295

* Thu Jan 13 2022  - 1.2.3-1
- Update to 1.2.3. RHBZ#1996619

* Fri Jan 07 2022 Gris Ge <fge@redhat.com> - 1.2.2-2
- Fix bridge vlan filtering on i40e. RHBZ#2026621

* Tue Nov 30 2021 Gris Ge <fge@redhat.com> - 1.2.2-1
- Upgrade to 1.2.2. RHBZ#1996619

* Thu Nov 25 2021 Gris Ge <fge@redhat.com> - 1.2.1-1
- Upgrade to 1.2.1. RHBZ#1996619

* Wed Nov 24 2021 Gris Ge <fge@redhat.com> - 1.2.0-1
- Upgrade to 1.2.0. RHBZ#1996619

* Sat Jun 19 2021 Gris Ge <fge@redhat.com> - 1.1.1-1
- Upgrade to 1.1.1. RHBZ#1942459

* Fri Jun 18 2021 Gris Ge <fge@redhat.com> - 1.1.0-3
- Include SPEC information for bundled rust crates. RHBZ#1927789

* Tue Jun 08 2021 Gris Ge <fge@redhat.com> - 1.1.0-2
- Fix cli output, loopback interface and ethtool features.

* Tue May 25 2021 Wen Liang <wenliang@redhat.com> - 1.1.0-1
- Upgrade to 1.1.0. RHBZ#1942459

* Thu Feb 18 2021 Fernando Fernandez Mancera <ferferna@redhat.com> - 1.0.2-4
- Remove the varlink support. RHBZ#1926941

* Tue Feb 02 2021 Fernando Fernandez Mancera <ferferna@redhat.com> - 1.0.1-3
- Add support to bond vlan+srcmac tx hashing option. RHBZ#1919986

* Fri Nov 13 2020 Gris Ge <fge@redhat.com> - 1.0.1-2
- Upload new cargo vendor tarbal without crates used for windows platform.

* Tue Nov 10 2020 Fernando Fernandez Mancera <ferferna@redhat.com> - 1.0.1-1
- Upgrade to 1.0.1

* Mon Nov 09 2020 Gris Ge <fge@redhat.com> - 1.0.0-1
- Upgrade to 1.0.0

* Mon Oct 19 2020 Gris Ge <fge@redhat.com> - 0.6.1-2
- Rebuild to load the compose settings.

* Tue Oct 13 2020 Gris Ge <fge@redhat.com> - 0.6.1-1
- Upgrade to 0.6.1

* Fri Oct 09 2020 Fernando Fernandez Mancera <ferferna@redhat.com> - 0.6.0-2
- VXLAN Python fix incorrect destination port

* Fri Oct 09 2020 Fernando Fernandez Mancera <ferferna@redhat.com> - 0.6.0-1
- Upgrade to 0.6.0

* Sun Sep 20 2020 Gris Ge <fge@redhat.com> - 0.5.1-1
- Upgrade to 0.5.1

* Thu Sep 17 2020 Gris Ge <fge@redhat.com> - 0.5.0-3
- Trigger rebuild for CI gating

* Tue Sep 08 2020 Gris Ge <fge@redhat.com> - 0.5.0-2
- Fix the python3-nispor requirement

* Fri Sep 04 2020 Gris Ge <fge@redhat.com> - 0.5.0-1
- Upgrade to 0.5.0

* Sat Aug 29 2020 Gris Ge <fge@redhat.com> - 0.4.0-3
- Fix the ldconfig

* Wed Aug 26 2020 Gris Ge <fge@redhat.com> - 0.4.0-2
- Add ldconfig to post and postun scripts

* Wed Aug 26 2020 Gris Ge <fge@redhat.com> - 0.4.0-1
- Upgrade to 0.4.0

* Mon Aug 17 2020 Gris Ge <fge@redhat.com> - 0.3.0-2
- Fix python linux bridge vlan filtering

* Sun Aug 16 2020 Gris Ge <fge@redhat.com> - 0.3.0-1
- Upgrade to 0.3.0

* Tue Aug 11 2020 Gris Ge <fge@redhat.com> - 0.2.0-1
- Upgrade to 0.2.0

* Thu Jul 09 2020 Gris Ge <fge@redhat.com> - 0.1.1-2
- Include license and documents

* Wed Jul 08 2020 Gris Ge <fge@redhat.com> - 0.1.1-1
- Initial build.
