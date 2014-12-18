Name:           ros-indigo-rail-ceiling
Version:        0.0.4
Release:        0%{?dist}
Summary:        ROS rail_ceiling package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/rail_ceiling
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-indigo-ar-track-alvar
Requires:       ros-indigo-ar-track-alvar-msgs
Requires:       ros-indigo-geometry-msgs
Requires:       ros-indigo-image-view
Requires:       ros-indigo-robot-state-publisher
Requires:       ros-indigo-roscpp
Requires:       ros-indigo-roslib
Requires:       ros-indigo-tf
Requires:       ros-indigo-usb-cam
Requires:       ros-indigo-xacro
Requires:       yaml-cpp-devel
BuildRequires:  pkgconfig
BuildRequires:  ros-indigo-ar-track-alvar-msgs
BuildRequires:  ros-indigo-catkin
BuildRequires:  ros-indigo-geometry-msgs
BuildRequires:  ros-indigo-roscpp
BuildRequires:  ros-indigo-roslib
BuildRequires:  ros-indigo-tf
BuildRequires:  yaml-cpp-devel

%description
Overhead Camera System for Tracking AR Tags

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/indigo" \
        -DCMAKE_PREFIX_PATH="/opt/ros/indigo" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/indigo

%changelog
* Thu Dec 18 2014 Russell Toris <rctoris@wpi.edu> - 0.0.4-0
- Autogenerated by Bloom

* Thu Dec 04 2014 Russell Toris <rctoris@wpi.edu> - 0.0.3-0
- Autogenerated by Bloom

* Tue Dec 02 2014 Russell Toris <rctoris@wpi.edu> - 0.0.2-0
- Autogenerated by Bloom

* Wed Aug 27 2014 Russell Toris <rctoris@wpi.edu> - 0.0.1-0
- Autogenerated by Bloom

