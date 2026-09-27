Name:           bwrenamer
Version:        1.4.0
Release:        1%{?dist}
Summary:        Desktop application for batch renaming files

License:        GPL-3.0-or-later
URL:            https://github.com/bulkware/bwrenamer
Source0:        %{name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-pyside6
BuildRequires:  python3-setuptools
BuildRequires:  pyproject-rpm-macros
BuildRequires:  desktop-file-utils
BuildRequires:  appstream
Requires:       python3-pyside6

%description
bwRenamer renames multiple files using interactive text tools.

%prep
%autosetup

%build
%pyproject_wheel

%check
PYTHONPATH=.. %{python3} -m unittest discover -s tests -v

%install
%pyproject_install
install -D -m 644 data/org.bulkware.bwrenamer.desktop \
    %{buildroot}%{_datadir}/applications/org.bulkware.bwrenamer.desktop
install -D -m 644 data/org.bulkware.bwrenamer.metainfo.xml \
    %{buildroot}%{_metainfodir}/org.bulkware.bwrenamer.metainfo.xml
install -D -m 644 data/icons/hicolor/512x512/apps/org.bulkware.bwrenamer.png \
    %{buildroot}%{_datadir}/icons/hicolor/512x512/apps/org.bulkware.bwrenamer.png

%files
%license gpl.txt
%doc CHANGELOG.md README.md
%{_bindir}/bwrenamer
%{python3_sitelib}/bwrenamer
%{python3_sitelib}/bwrenamer-*.dist-info
%{_datadir}/applications/org.bulkware.bwrenamer.desktop
%{_metainfodir}/org.bulkware.bwrenamer.metainfo.xml
%{_datadir}/icons/hicolor/512x512/apps/org.bulkware.bwrenamer.png

%changelog
* Sun Sep 27 2026 Antti-Pekka Meronen <antice@kapsi.fi> - 1.4.0-1
- Changed: GitHub Actions CI package building.
- Changed: Packaging system for Debian (.deb) and Red Hat (.rpm) based distros.
- Changed: Renewed the Windows packaging system.
