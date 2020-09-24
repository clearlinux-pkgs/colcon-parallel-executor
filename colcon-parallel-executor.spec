#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : colcon-parallel-executor
Version  : 0.2.4
Release  : 14
URL      : https://files.pythonhosted.org/packages/61/c6/4b4c91a398ecf6f8de4fad2d6f13d6289d4f50db471f13d2433737b1c520/colcon-parallel-executor-0.2.4.tar.gz
Source0  : https://files.pythonhosted.org/packages/61/c6/4b4c91a398ecf6f8de4fad2d6f13d6289d4f50db471f13d2433737b1c520/colcon-parallel-executor-0.2.4.tar.gz
Summary  : Extension for colcon to process packages in parallel.
Group    : Development/Tools
License  : Apache-2.0
Requires: colcon-parallel-executor-python = %{version}-%{release}
Requires: colcon-parallel-executor-python3 = %{version}-%{release}
Requires: colcon-core
BuildRequires : buildreq-distutils3
BuildRequires : colcon-core

%description
========================

%package python
Summary: python components for the colcon-parallel-executor package.
Group: Default
Requires: colcon-parallel-executor-python3 = %{version}-%{release}

%description python
python components for the colcon-parallel-executor package.


%package python3
Summary: python3 components for the colcon-parallel-executor package.
Group: Default
Requires: python3-core
Provides: pypi(colcon_parallel_executor)
Requires: pypi(colcon_core)

%description python3
python3 components for the colcon-parallel-executor package.


%prep
%setup -q -n colcon-parallel-executor-0.2.4
cd %{_builddir}/colcon-parallel-executor-0.2.4

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1583528310
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$CFLAGS -fno-lto "
export FFLAGS="$CFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
