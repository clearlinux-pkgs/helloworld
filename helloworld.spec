#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : helloworld
Version  : 4
Release  : 181
URL      : http://localhost/cgit/projects/helloworld/snapshot/helloworld-4.tar.bz2
Source0  : http://localhost/cgit/projects/helloworld/snapshot/helloworld-4.tar.bz2
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0+ GPL-3.0
Requires: helloworld-bin = %{version}-%{release}
Requires: helloworld-filemap = %{version}-%{release}
Requires: helloworld-license = %{version}-%{release}

%description
No detailed description available

%package bin
Summary: bin components for the helloworld package.
Group: Binaries
Requires: helloworld-license = %{version}-%{release}
Requires: helloworld-filemap = %{version}-%{release}

%description bin
bin components for the helloworld package.


%package filemap
Summary: filemap components for the helloworld package.
Group: Default

%description filemap
filemap components for the helloworld package.


%package license
Summary: license components for the helloworld package.
Group: Default

%description license
license components for the helloworld package.


%prep
%setup -q -n helloworld-4
cd %{_builddir}/helloworld-4
pushd ..
cp -a helloworld-4 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1664210720
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
%reconfigure --disable-static
make  %{?_smp_mflags}
unset PKG_CONFIG_PATH
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3"
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3"
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3"
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3"
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3"
%reconfigure --disable-static
make  %{?_smp_mflags}
popd

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make %{?_smp_mflags} check
cd ../buildavx2;
make %{?_smp_mflags} check || :

%install
export SOURCE_DATE_EPOCH=1664210720
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/helloworld
cp %{_builddir}/helloworld-%{version}/COPYING %{buildroot}/usr/share/package-licenses/helloworld/8624bcdae55baeef00cd11d5dfcfa60f68710a02
pushd ../buildavx2/
%make_install_v3
popd
%make_install
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/bubble_sort
/usr/bin/helloworld
/usr/bin/matrix_multiplication
/usr/bin/pi_calculation
/usr/share/clear/optimized-elf/bin*

%files filemap
%defattr(-,root,root,-)
/usr/share/clear/filemap/filemap-helloworld

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/helloworld/8624bcdae55baeef00cd11d5dfcfa60f68710a02
