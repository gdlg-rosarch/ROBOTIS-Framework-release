Name:           ros-kinetic-robotis-device
Version:        0.2.3
Release:        0%{?dist}
Summary:        ROS robotis_device package

Group:          Development/Libraries
License:        BSD
URL:            http://wiki.ros.org/robotis_device
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-kinetic-dynamixel-sdk
Requires:       ros-kinetic-roscpp
Requires:       ros-kinetic-rospy
BuildRequires:  ros-kinetic-catkin
BuildRequires:  ros-kinetic-dynamixel-sdk
BuildRequires:  ros-kinetic-roscpp
BuildRequires:  ros-kinetic-rospy

%description
The package that manages device information of ROBOTIS robots. This package is
used when reading device information with the robot information file from the
robotis_controller package.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/kinetic" \
        -DCMAKE_PREFIX_PATH="/opt/ros/kinetic" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/kinetic

%changelog
* Tue May 23 2017 Pyo <pyo@robotis.com> - 0.2.3-0
- Autogenerated by Bloom

* Mon Apr 24 2017 Pyo <pyo@robotis.com> - 0.2.2-0
- Autogenerated by Bloom

* Wed Nov 23 2016 Pyo <pyo@robotis.com> - 0.2.1-0
- Autogenerated by Bloom

* Wed Aug 31 2016 Pyo <pyo@robotis.com> - 0.2.0-0
- Autogenerated by Bloom

* Thu Aug 18 2016 Pyo <pyo@robotis.com> - 0.1.1-0
- Autogenerated by Bloom

* Sat Aug 13 2016 robotis <zerom@robotis.com> - 0.1.0-0
- Autogenerated by Bloom

