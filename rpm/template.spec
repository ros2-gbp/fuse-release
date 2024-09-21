%bcond_without tests
%bcond_without weak_deps

%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')
%global __provides_exclude_from ^/opt/ros/rolling/.*$
%global __requires_exclude_from ^/opt/ros/rolling/.*$

Name:           ros-rolling-fuse-optimizers
Version:        1.2.1
Release:        1%{?dist}%{?release_suffix}
Summary:        ROS fuse_optimizers package

License:        BSD
Source0:        %{name}-%{version}.tar.gz

Requires:       boost-devel
Requires:       boost-python%{python3_pkgversion}-devel
Requires:       ceres-solver-devel
Requires:       eigen3-devel
Requires:       flexiblas-devel
Requires:       ros-rolling-diagnostic-updater
Requires:       ros-rolling-fuse-constraints
Requires:       ros-rolling-fuse-core
Requires:       ros-rolling-fuse-graphs
Requires:       ros-rolling-fuse-msgs
Requires:       ros-rolling-fuse-variables
Requires:       ros-rolling-pluginlib
Requires:       ros-rolling-rclcpp
Requires:       ros-rolling-rclcpp-components
Requires:       ros-rolling-std-srvs
Requires:       suitesparse-devel
Requires:       ros-rolling-ros-workspace
BuildRequires:  boost-devel
BuildRequires:  boost-python%{python3_pkgversion}-devel
BuildRequires:  ceres-solver-devel
BuildRequires:  eigen3-devel
BuildRequires:  flexiblas-devel
BuildRequires:  ros-rolling-ament-cmake-ros
BuildRequires:  ros-rolling-diagnostic-updater
BuildRequires:  ros-rolling-fuse-constraints
BuildRequires:  ros-rolling-fuse-core
BuildRequires:  ros-rolling-fuse-graphs
BuildRequires:  ros-rolling-fuse-msgs
BuildRequires:  ros-rolling-fuse-variables
BuildRequires:  ros-rolling-pluginlib
BuildRequires:  ros-rolling-rclcpp
BuildRequires:  ros-rolling-rclcpp-components
BuildRequires:  ros-rolling-std-srvs
BuildRequires:  suitesparse-devel
BuildRequires:  ros-rolling-ros-workspace
Provides:       %{name}-devel = %{version}-%{release}
Provides:       %{name}-doc = %{version}-%{release}
Provides:       %{name}-runtime = %{version}-%{release}

%if 0%{?with_tests}
BuildRequires:  ros-rolling-ament-cmake-gtest
BuildRequires:  ros-rolling-ament-lint-auto
BuildRequires:  ros-rolling-ament-lint-common
BuildRequires:  ros-rolling-fuse-models
BuildRequires:  ros-rolling-geometry-msgs
BuildRequires:  ros-rolling-launch
BuildRequires:  ros-rolling-launch-pytest
BuildRequires:  ros-rolling-launch-ros
BuildRequires:  ros-rolling-nav-msgs
%endif

%description
The fuse_optimizers package provides a set of optimizer implementations. An
optimizer is the object responsible \ for coordinating the sensors and motion
model inputs, computing the optimal state values, and providing access to \ to
the optimal state via the publishers.

%prep
%autosetup -p1

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/rolling/setup.sh" ]; then . "/opt/ros/rolling/setup.sh"; fi
mkdir -p .obj-%{_target_platform} && cd .obj-%{_target_platform}
%cmake3 \
    -UINCLUDE_INSTALL_DIR \
    -ULIB_INSTALL_DIR \
    -USYSCONF_INSTALL_DIR \
    -USHARE_INSTALL_PREFIX \
    -ULIB_SUFFIX \
    -DCMAKE_INSTALL_PREFIX="/opt/ros/rolling" \
    -DAMENT_PREFIX_PATH="/opt/ros/rolling" \
    -DCMAKE_PREFIX_PATH="/opt/ros/rolling" \
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
if [ -f "/opt/ros/rolling/setup.sh" ]; then . "/opt/ros/rolling/setup.sh"; fi
%make_install -C .obj-%{_target_platform}

%if 0%{?with_tests}
%check
# Look for a Makefile target with a name indicating that it runs tests
TEST_TARGET=$(%__make -qp -C .obj-%{_target_platform} | sed "s/^\(test\|check\):.*/\\1/;t f;d;:f;q0")
if [ -n "$TEST_TARGET" ]; then
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/rolling/setup.sh" ]; then . "/opt/ros/rolling/setup.sh"; fi
CTEST_OUTPUT_ON_FAILURE=1 \
    %make_build -C .obj-%{_target_platform} $TEST_TARGET || echo "RPM TESTS FAILED"
else echo "RPM TESTS SKIPPED"; fi
%endif

%files
/opt/ros/rolling

%changelog
* Sat Sep 21 2024 Stephen Williams <swilliams@locusrobotics.com> - 1.2.1-1
- Autogenerated by Bloom

* Thu May 02 2024 Stephen Williams <swilliams@locusrobotics.com> - 1.2.0-1
- Autogenerated by Bloom

* Sat Apr 20 2024 Stephen Williams <swilliams@locusrobotics.com> - 1.1.0-1
- Autogenerated by Bloom

* Wed Mar 06 2024 Stephen Williams <swilliams@locusrobotics.com> - 1.0.1-3
- Autogenerated by Bloom

