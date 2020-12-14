#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : helloworld
Version  : 4
Release  : 157
URL      : http://localhost/cgit/projects/helloworld/snapshot/helloworld-4.tar.bz2
Source0  : http://localhost/cgit/projects/helloworld/snapshot/helloworld-4.tar.bz2
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0+ GPL-3.0
Requires: helloworld-bin = %{version}-%{release}
Requires: helloworld-license = %{version}-%{release}

%description
No detailed description available

%package bin
Summary: bin components for the helloworld package.
Group: Binaries
Requires: helloworld-license = %{version}-%{release}

%description bin
bin components for the helloworld package.


%package license
Summary: license components for the helloworld package.
Group: Default

%description license
license components for the helloworld package.


%prep
%setup -q -n helloworld-4
cd %{_builddir}/helloworld-4

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1604541085
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
%reconfigure --disable-static
make  %{?_smp_mflags}

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1604541085
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/helloworld
cp %{_builddir}/helloworld-4/COPYING %{buildroot}/usr/share/package-licenses/helloworld/8624bcdae55baeef00cd11d5dfcfa60f68710a02
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/bubble_sort
/usr/bin/helloworld
/usr/bin/matrix_multiplication
/usr/bin/pi_calculation

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/helloworld/8624bcdae55baeef00cd11d5dfcfa60f68710a02
