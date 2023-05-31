#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
#
# Source0 file verified with key 0xBB463350D6EF31EF (heiko@shruuf.de)
#
Name     : kdegraphics-thumbnailers
Version  : 23.04.1
Release  : 54
URL      : https://download.kde.org/stable/release-service/23.04.1/src/kdegraphics-thumbnailers-23.04.1.tar.xz
Source0  : https://download.kde.org/stable/release-service/23.04.1/src/kdegraphics-thumbnailers-23.04.1.tar.xz
Source1  : https://download.kde.org/stable/release-service/23.04.1/src/kdegraphics-thumbnailers-23.04.1.tar.xz.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0
Requires: kdegraphics-thumbnailers-data = %{version}-%{release}
Requires: kdegraphics-thumbnailers-lib = %{version}-%{release}
Requires: kdegraphics-thumbnailers-license = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : extra-cmake-modules-data
BuildRequires : kdegraphics-mobipocket-dev
BuildRequires : libkdcraw-dev
BuildRequires : libkexiv2-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
No detailed description available

%package data
Summary: data components for the kdegraphics-thumbnailers package.
Group: Data

%description data
data components for the kdegraphics-thumbnailers package.


%package lib
Summary: lib components for the kdegraphics-thumbnailers package.
Group: Libraries
Requires: kdegraphics-thumbnailers-data = %{version}-%{release}
Requires: kdegraphics-thumbnailers-license = %{version}-%{release}

%description lib
lib components for the kdegraphics-thumbnailers package.


%package license
Summary: license components for the kdegraphics-thumbnailers package.
Group: Default

%description license
license components for the kdegraphics-thumbnailers package.


%prep
%setup -q -n kdegraphics-thumbnailers-23.04.1
cd %{_builddir}/kdegraphics-thumbnailers-23.04.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1685569717
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FCFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export CXXFLAGS="$CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
%cmake ..
make  %{?_smp_mflags}
popd
mkdir -p clr-build-avx2
pushd clr-build-avx2
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -Wl,-z,x86-64-v3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd -march=x86-64-v3 "
export FCFLAGS="$FFLAGS -O3 -Wl,-z,x86-64-v3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd -march=x86-64-v3 "
export FFLAGS="$FFLAGS -O3 -Wl,-z,x86-64-v3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd -march=x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -O3 -Wl,-z,x86-64-v3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd -march=x86-64-v3 "
export CFLAGS="$CFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
export CXXFLAGS="$CXXFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
export FFLAGS="$FFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
export FCFLAGS="$FCFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
%cmake ..
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1685569717
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/kdegraphics-thumbnailers
cp %{_builddir}/kdegraphics-thumbnailers-%{version}/COPYING %{buildroot}/usr/share/package-licenses/kdegraphics-thumbnailers/06877624ea5c77efe3b7e39b0f909eda6e25a4ec || :
cp %{_builddir}/kdegraphics-thumbnailers-%{version}/COPYING.LIB %{buildroot}/usr/share/package-licenses/kdegraphics-thumbnailers/c08668a6ace9b36ba46940609040748161b03a37 || :
pushd clr-build-avx2
%make_install_v3  || :
popd
pushd clr-build
%make_install
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/kservices5/blenderthumbnail.desktop
/usr/share/kservices5/gsthumbnail.desktop
/usr/share/kservices5/mobithumbnail.desktop
/usr/share/kservices5/rawthumbnail.desktop
/usr/share/metainfo/org.kde.kdegraphics-thumbnailers.metainfo.xml

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/qt5/plugins/blenderthumbnail.so
/V3/usr/lib64/qt5/plugins/gsthumbnail.so
/V3/usr/lib64/qt5/plugins/mobithumbnail.so
/V3/usr/lib64/qt5/plugins/rawthumbnail.so
/usr/lib64/qt5/plugins/blenderthumbnail.so
/usr/lib64/qt5/plugins/gsthumbnail.so
/usr/lib64/qt5/plugins/mobithumbnail.so
/usr/lib64/qt5/plugins/rawthumbnail.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/kdegraphics-thumbnailers/06877624ea5c77efe3b7e39b0f909eda6e25a4ec
/usr/share/package-licenses/kdegraphics-thumbnailers/c08668a6ace9b36ba46940609040748161b03a37
