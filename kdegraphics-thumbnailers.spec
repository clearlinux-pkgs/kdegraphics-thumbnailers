#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xDBD2CE893E2D1C87 (cfeck@kde.org)
#
Name     : kdegraphics-thumbnailers
Version  : 19.12.0
Release  : 16
URL      : https://download.kde.org/stable/release-service/19.12.0/src/kdegraphics-thumbnailers-19.12.0.tar.xz
Source0  : https://download.kde.org/stable/release-service/19.12.0/src/kdegraphics-thumbnailers-19.12.0.tar.xz
Source1  : https://download.kde.org/stable/release-service/19.12.0/src/kdegraphics-thumbnailers-19.12.0.tar.xz.sig
Summary  : Thumbnailers for various graphics file formats
Group    : Development/Tools
License  : GPL-2.0
Requires: kdegraphics-thumbnailers-data = %{version}-%{release}
Requires: kdegraphics-thumbnailers-lib = %{version}-%{release}
Requires: kdegraphics-thumbnailers-license = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : libkdcraw-dev
BuildRequires : libkexiv2-dev
BuildRequires : qtbase-dev mesa-dev

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
%setup -q -n kdegraphics-thumbnailers-19.12.0
cd %{_builddir}/kdegraphics-thumbnailers-19.12.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1576549786
mkdir -p clr-build
pushd clr-build
# -Werror is for werrorists
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%cmake ..
make  %{?_smp_mflags}  VERBOSE=1
popd

%install
export SOURCE_DATE_EPOCH=1576549786
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/kdegraphics-thumbnailers
cp %{_builddir}/kdegraphics-thumbnailers-19.12.0/COPYING %{buildroot}/usr/share/package-licenses/kdegraphics-thumbnailers/06877624ea5c77efe3b7e39b0f909eda6e25a4ec
cp %{_builddir}/kdegraphics-thumbnailers-19.12.0/COPYING.LIB %{buildroot}/usr/share/package-licenses/kdegraphics-thumbnailers/c08668a6ace9b36ba46940609040748161b03a37
pushd clr-build
%make_install
popd

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/kservices5/blenderthumbnail.desktop
/usr/share/kservices5/gsthumbnail.desktop
/usr/share/kservices5/rawthumbnail.desktop
/usr/share/metainfo/org.kde.kdegraphics-thumbnailers.metainfo.xml

%files lib
%defattr(-,root,root,-)
/usr/lib64/qt5/plugins/blenderthumbnail.so
/usr/lib64/qt5/plugins/gsthumbnail.so
/usr/lib64/qt5/plugins/rawthumbnail.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/kdegraphics-thumbnailers/06877624ea5c77efe3b7e39b0f909eda6e25a4ec
/usr/share/package-licenses/kdegraphics-thumbnailers/c08668a6ace9b36ba46940609040748161b03a37
