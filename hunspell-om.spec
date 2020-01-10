Name: hunspell-om
Summary: Oromo hunspell dictionaries
Epoch: 1
Version: 0.04
Release: 6%{?dist}
Group: Applications/Text
Source: http://borel.slu.edu/obair/%{name}-%{version}.oxt
URL: http://borel.slu.edu/crubadan/apps.html
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
License: LGPLv3+
BuildArch: noarch
Requires: hunspell

%description
Oromo hunspell dictionaries.

%prep
%setup -q -c

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/myspell
cp -p dictionaries/om_ET.* $RPM_BUILD_ROOT/%{_datadir}/myspell

pushd $RPM_BUILD_ROOT/%{_datadir}/myspell/
om_ET_aliases="om_KE"
for lang in $om_ET_aliases; do
        ln -s om_ET.aff $lang.aff
        ln -s om_ET.dic $lang.dic
done

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc dictionaries/README_om_ET.txt LICENSES-en.txt
%{_datadir}/myspell/*

%changelog
* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 1:0.04-6
- Mass rebuild 2013-12-27

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:0.04-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:0.04-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:0.04-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:0.04-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Nov 17 2009 Caolan McNamara <caolanm@redhat.com> - 1:0.04-1
- latest version

* Sat Oct 17 2009 Caolan McNamara <caolanm@redhat.com> - 0.20091002-1
- latest version

* Thu Sep 10 2009 Caolan McNamara <caolanm@redhat.com> - 0.20090414-1
- initial version
