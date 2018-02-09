#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : helloworld
Version  : 4
Release  : 79
URL      : http://localhost/cgit/projects/helloworld/snapshot/helloworld-4.tar.bz2
Source0  : http://localhost/cgit/projects/helloworld/snapshot/helloworld-4.tar.bz2
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0+ GPL-3.0
Requires: helloworld-bin

%description
No detailed description available

%package bin
Summary: bin components for the helloworld package.
Group: Binaries

%description bin
bin components for the helloworld package.


%prep
%setup -q -n helloworld-4

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1510693070
%reconfigure --disable-static
make V=1  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1510693070
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/bubble_sort
/usr/bin/helloworld
/usr/bin/matrix_multiplication
/usr/bin/pi_calculation
