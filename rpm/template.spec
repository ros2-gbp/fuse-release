%bcond_without tests
%bcond_without weak_deps

%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')
%global __provides_exclude_from ^/opt/ros/iron/.*$
%global __requires_exclude_from ^/opt/ros/iron/.*$

Name:           ros-iron-fuse-core
Version:        1.0.1
Release:        4%{?dist}%{?release_suffix}
Summary:        ROS fuse_core package

License:        BSD
Source0:        %{name}-%{version}.tar.gz

Requires:       boost-devel
Requires:       boost-python%{python3_pkgversion}-devel
Requires:       ceres-solver-devel
Requires:       eigen3-devel
Requires:       flexiblas-devel
Requires:       glog-devel
Requires:       ros-iron-fuse-msgs
Requires:       ros-iron-pluginlib
Requires:       ros-iron-rcl-interfaces
Requires:       ros-iron-rclcpp
Requires:       ros-iron-rclcpp-components
Requires:       suitesparse-devel
Requires:       ros-iron-ros-workspace
BuildRequires:  boost-devel
BuildRequires:  boost-python%{python3_pkgversion}-devel
BuildRequires:  ceres-solver-devel
BuildRequires:  eigen3-devel
BuildRequires:  flexiblas-devel
BuildRequires:  glog-devel
BuildRequires:  ros-iron-ament-cmake-ros
BuildRequires:  ros-iron-fuse-msgs
BuildRequires:  ros-iron-pluginlib
BuildRequires:  ros-iron-rcl-interfaces
BuildRequires:  ros-iron-rclcpp
BuildRequires:  ros-iron-rclcpp-components
BuildRequires:  suitesparse-devel
BuildRequires:  ros-iron-ros-workspace
Provides:       %{name}-devel = %{version}-%{release}
Provides:       %{name}-doc = %{version}-%{release}
Provides:       %{name}-runtime = %{version}-%{release}

%if 0%{?with_tests}
BuildRequires:  ros-iron-ament-cmake-gtest
BuildRequires:  ros-iron-ament-cmake-pytest
BuildRequires:  ros-iron-ament-lint-auto
BuildRequires:  ros-iron-ament-lint-common
BuildRequires:  ros-iron-geometry-msgs
BuildRequires:  ros-iron-launch
BuildRequires:  ros-iron-launch-pytest
%endif

%description
The fuse_core package provides the base class interfaces for the various fuse
components. Concrete implementations of these interfaces are provided in other
packages.

%prep
%autosetup -p1

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/iron/setup.sh" ]; then . "/opt/ros/iron/setup.sh"; fi
mkdir -p .obj-%{_target_platform} && cd .obj-%{_target_platform}
%cmake3 \
    -UINCLUDE_INSTALL_DIR \
    -ULIB_INSTALL_DIR \
    -USYSCONF_INSTALL_DIR \
    -USHARE_INSTALL_PREFIX \
    -ULIB_SUFFIX \
    -DCMAKE_INSTALL_PREFIX="/opt/ros/iron" \
    -DAMENT_PREFIX_PATH="/opt/ros/iron" \
    -DCMAKE_PREFIX_PATH="/opt/ros/iron" \
    -DSETUPTOOLS_DEB_LAYOUT=OFF \
%if !0%{?with_tests}
    -DBUILD_TESTING=OFF \
%endif
    ..

%make_build

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/iron/setup.sh" ]; then . "/opt/ros/iron/setup.sh"; fi
%make_install -C .obj-%{_target_platform}

%if 0%{?with_tests}
%check
# Look for a Makefile target with a name indicating that it runs tests
TEST_TARGET=$(%__make -qp -C .obj-%{_target_platform} | sed "s/^\(test\|check\):.*/\\1/;t f;d;:f;q0")
if [ -n "$TEST_TARGET" ]; then
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/iron/setup.sh" ]; then . "/opt/ros/iron/setup.sh"; fi
CTEST_OUTPUT_ON_FAILURE=1 \
    %make_build -C .obj-%{_target_platform} $TEST_TARGET || echo "RPM TESTS FAILED"
else echo "RPM TESTS SKIPPED"; fi
%endif

%files
/opt/ros/iron

%changelog
* Sat Apr 20 2024 Stephen Williams <swilliams@locusrobotics.com> - 1.0.1-4
- Autogenerated by Bloom

* Thu Apr 20 2023 Stephen Williams <swilliams@locusrobotics.com> - 1.0.1-3
- Autogenerated by Bloom

* Mon Apr 10 2023 Stephen Williams <swilliams@locusrobotics.com> - 1.0.1-2
- Autogenerated by Bloom

* Tue Mar 28 2023 Stephen Williams <swilliams@locusrobotics.com> - 1.0.1-1
- Autogenerated by Bloom

