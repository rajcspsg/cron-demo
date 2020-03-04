Summary: Utility for testing RPM creation
Name: utils
Version: 1.0.0
Release: 1
License: GPL
URL: http://www.both.org
Group: System
Packager: Rajkumar Natarajan
Requires: bash
Requires: nodejs >= 8.1.2
BuildRoot: ~/rpmbuild/

%description
A collection of utility scripts for testing RPM creation.


%prep
################################################################################
# Create the build tree and copy the files from the development directories    #
# into the build tree.                                                         #
################################################################################
echo "BUILDROOT = $RPM_BUILD_ROOT"


%pre

%build

%install
sudo mkdir -p /etc/cron.d
sudo mkdir -p /var/log/myapp-services-cron
sudo mkdir -p /var/lock/myapp-services-cron
sudo mkdir -p /opt/myorg/apps/myapp-services
sudo cp -r /home/vagrant/cron-demo %{buildroot}/
sudo cp -r  %{buildroot}/cron-demo/crontab /etc/cron.d/myapp-services-cron-scripts
sudo cp -r %{buildroot}/cron-demo/scripts /opt/myorg/apps/myapp-services/


%post

%files
/cron-demo/

%postun

%clean
sudo rm -rf %{buildroot}/

%changelog
