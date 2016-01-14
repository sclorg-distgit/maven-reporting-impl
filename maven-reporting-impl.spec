%global pkg_name maven-reporting-impl
%{?scl:%scl_package %{pkg_name}}
%{?maven_find_provides_and_requires}

Name:           %{?scl_prefix}%{pkg_name}
Version:        2.2
Release:        8.9%{?dist}
Summary:        Abstract classes to manage report generation
License:        ASL 2.0
URL:            http://maven.apache.org/shared/maven-reporting-impl
# svn export http://svn.apache.org/repos/asf/maven/shared/tags/maven-reporting-impl-2.2 maven-reporting-impl-2.2
# tar caf maven-reporting-impl-2.2.tar.xz maven-reporting-impl-2.2/
Source0:        %{pkg_name}-%{version}.tar.xz
# ASL mandates that the licence file be included in redistributed source
Source1:        http://www.apache.org/licenses/LICENSE-2.0.txt
BuildArch:      noarch

BuildRequires:  %{?scl_prefix_java_common}maven-local
BuildRequires:  %{?scl_prefix}mvn(commons-validator:commons-validator)
BuildRequires:  %{?scl_prefix_java_common}mvn(junit:junit)
BuildRequires:  %{?scl_prefix}mvn(org.apache.maven.doxia:doxia-core)
BuildRequires:  %{?scl_prefix}mvn(org.apache.maven.doxia:doxia-sink-api)
BuildRequires:  %{?scl_prefix}mvn(org.apache.maven.doxia:doxia-site-renderer)
BuildRequires:  %{?scl_prefix}mvn(org.apache.maven.reporting:maven-reporting-api)
BuildRequires:  %{?scl_prefix}mvn(org.apache.maven.shared:maven-shared-components:pom:)
BuildRequires:  %{?scl_prefix}mvn(org.apache.maven:maven-plugin-api)
BuildRequires:  %{?scl_prefix}mvn(org.apache.maven:maven-project)
BuildRequires:  %{?scl_prefix}mvn(org.codehaus.plexus:plexus-utils)
%{?fedora:BuildRequires: junit-addons}


%description
Abstract classes to manage report generation, which can be run both:

* as part of a site generation (as a maven-reporting-api's MavenReport),
* or as a direct standalone invocation (as a maven-plugin-api's Mojo).

This is a replacement package for maven-shared-reporting-impl

%package javadoc
Summary:        Javadoc for %{pkg_name}
    
%description javadoc
API documentation for %{pkg_name}.

%prep
%setup -q -n %{pkg_name}-%{version}
%{?scl:scl enable %{scl_java_common} %{scl_maven} %{scl} - <<"EOF"}
set -e -x
cp -p %{SOURCE1} LICENSE.txt
%{?scl:EOF}

%build
%{?scl:scl enable %{scl_java_common} %{scl_maven} %{scl} - <<"EOF"}
set -e -x
%mvn_build %{!?fedora:-f}
%{?scl:EOF}

%install
%{?scl:scl enable %{scl_java_common} %{scl_maven} %{scl} - <<"EOF"}
set -e -x
%mvn_install
%{?scl:EOF}

%files -f .mfiles
%{_javadir}/%{pkg_name}
%dir %{_mavenpomdir}/%{pkg_name}
%doc LICENSE.txt

%files javadoc -f .mfiles-javadoc
%doc LICENSE.txt

%changelog
* Thu Jan 15 2015 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.2-8.9
- Add directory ownership on %%{_mavenpomdir} subdir

* Wed Jan 14 2015 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.2-8.8
- Fix BR on maven-shared POM

* Tue Jan 13 2015 Michael Simacek <msimacek@redhat.com> - 2.2-8.8
- Mass rebuild 2015-01-13

* Tue Jan 06 2015 Michael Simacek <msimacek@redhat.com> - 2.2-8.7
- Mass rebuild 2015-01-06

* Mon May 26 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.2-8.6
- Mass rebuild 2014-05-26

* Wed Feb 19 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.2-8.5
- Mass rebuild 2014-02-19

* Tue Feb 18 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.2-8.4
- Mass rebuild 2014-02-18

* Mon Feb 17 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.2-8.3
- SCL-ize build-requires

* Thu Feb 13 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.2-8.2
- Rebuild to regenerate auto-requires

* Tue Feb 11 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.2-8.1
- First maven30 software collection build

* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 2.2-8
- Mass rebuild 2013-12-27

* Fri Jun 28 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.2-7
- Rebuild to regenerate API documentation
- Resolves: CVE-2013-1571

* Mon Apr  8 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.2-6
- Add missing BuildRequires

* Mon Apr  8 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.2-5
- Skip running tests outsides Fedora

* Tue Feb 19 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.2-4
- Build with xmvn

* Wed Feb 06 2013 Java SIG <java-devel@lists.fedoraproject.org> - 2.2-3
- Update for https://fedoraproject.org/wiki/Fedora_19_Maven_Rebuild
- Replace maven BuildRequires with maven-local

* Tue Feb 05 2013 Michal Srb <msrb@redhat.com> - 2.2-2
- Migrate from maven-doxia to doxia subpackages

* Fri Jan 11 2013 Tomas Radej <tradej@redhat.com> - 2.2-1
- Initial version

