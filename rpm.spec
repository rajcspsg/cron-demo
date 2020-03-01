%define __prelink_undo_cmd %{nil}

Summary: Myapp Services
Name: myapp-services
Version: %{_version}
Release: %{_release}%{?_dist}
Source0: %{_source0}
License: Myorg
Group: Application/Internet
Prefix: %{_prefix}
AutoReqProv: no
Requires: at-spi2-atk >= 2.26.2-1.el7
Requires: at-spi2-core >= 2.28.0-1.el7
Requires: gtk3 >= 3.22.30-3.el7
Requires: libXScrnSaver >= 1.2.2-6.1.el7
Requires: nodejs >= 8.11.2

%description
Services for the Myapp Portal.

%prep
%setup -n %{_reponame}-%{version}

%pre
/usr/bin/getent passwd myappcron || useradd -U -r -d /opt/myorg/apps/myapp-services -s /bin/bash myappcron

#This line keeps a debug script from running which fails the builds
%define  debug_package %{nil}

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p ${RPM_BUILD_ROOT}%{_sysconfdir}/systemd/system
mkdir -p $RPM_BUILD_ROOT/opt/myorg/apps/myapp-services
cp -r * $RPM_BUILD_ROOT/opt/myorg/apps/myapp-services
cd $RPM_BUILD_ROOT/opt/myorg/apps/myapp-services
mkdir -p ${RPM_BUILD_ROOT}%{_sysconfdir}/cron.d
mkdir -p ${RPM_BUILD_ROOT}%{_localstatedir}/log/myapp-services-cron
mkdir -p ${RPM_BUILD_ROOT}%{_localstatedir}/lock/myapp-services-cron
cp crontab ${RPM_BUILD_ROOT}%{_sysconfdir}/cron.d/myapp-services-cron-scripts

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,nodejs,nodejs)
/opt/myorg/apps/myapp-services
%attr(0644,root,root)/etc/cron.d/myapp-services-cron-scripts
%defattr(-,myappcron,myappcron)
/var/log/myapp-services-cron
/var/lock/myapp-services-cron

%post
chcon system_u:object_r:system_cron_spool_t:s0 /etc/cron.d/myapp-services-cron-scripts
touch /etc/cron.d/myapp-services-cron-scripts

%changelog
- MyApp Services
