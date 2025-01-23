# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-suse-compat
# END SourceDeps(oneline)
%define suse_version 1550
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
#
# spec file for package libart-lgpl (version R14)
#
# Copyright (c) 2014 Trinity Desktop Environment
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.
#
# Please submit bugfixes or comments via http://www.trinitydesktop.org/
#

# TDE variables
%define tde_epoch 2
%if "%{?tde_version}" == ""
%define tde_version 14.1.3
%endif

%define libart %{_lib}art

Name:		tde-libart-lgpl
Version:	14.1.3
Release:	alt1
Summary:	Library of functions for 2D graphics
Group:		System/Libraries
URL:		http://www.trinitydesktop.org/

License:	LGPL-2.0+

#Vendor:			Trinity Project
#Packager:		Francois Andriot <francois.andriot@free.fr>

Source0:		tde-libart-lgpl.tar.gz

BuildRequires: tde-rpm-macros
BuildRequires:	tde-cmake
BuildRequires:	gcc-c++
BuildRequires:	libtool

%description
A library of functions for 2D graphics supporting a superset of the
PostScript imaging model, designed to be integrated with graphics, artwork,
and illustration programs. It is written in optimized C, and is fully
compatible with C++. With a small footprint of 10,000 lines of code, it is
especially suitable for embedded applications.

##########

%package -n %{libart}_lgpl_2-2
Summary:        Library of functions for 2D graphics - runtime files
Group:			System/Libraries
Obsoletes:		libart_lgpl < %{version}-%{release}
Provides:		libart_lgpl = %{version}-%{release}
Obsoletes:		%{_lib}art_lgpl2 < %{version}-%{release}
Provides:		%{_lib}art_lgpl2 = %{version}-%{release}
Provides:		libart_lgpl_2-2 = %{version}-%{release}

%description -n %{libart}_lgpl_2-2
A library of functions for 2D graphics supporting a superset of the
PostScript imaging model, designed to be integrated with graphics, artwork,
and illustration programs. It is written in optimized C, and is fully
compatible with C++. With a small footprint of 10,000 lines of code, it is
especially suitable for embedded applications.

%files -n %{libart}_lgpl_2-2
%{_libdir}/libart_lgpl_2.so.2
%{_libdir}/libart_lgpl_2.so.2.3.21

##########

%package -n %{libart}_lgpl-devel
Summary:        Library of functions for 2D graphics - development files
Group:          Development/Other
Provides:		libart_lgpl-devel = %{version}-%{release}
Requires:       libart_lgpl = %{version}-%{release}

%description -n %{libart}_lgpl-devel
A library of functions for 2D graphics supporting a superset of the
PostScript imaging model, designed to be integrated with graphics, artwork,
and illustration programs. It is written in optimized C, and is fully
compatible with C++. With a small footprint of 10,000 lines of code, it is
especially suitable for embedded applications.

%files -n %{libart}_lgpl-devel
%{_bindir}/libart2-config
%{_libdir}/libart_lgpl_2.a
%{_libdir}/libart_lgpl_2.so
%dir %{_includedir}/libart-2.0
%dir %{_includedir}/libart-2.0/libart_lgpl
%{_includedir}/libart-2.0/libart_lgpl/art_affine.h
%{_includedir}/libart-2.0/libart_lgpl/art_alphagamma.h
%{_includedir}/libart-2.0/libart_lgpl/art_bpath.h
%{_includedir}/libart-2.0/libart_lgpl/art_config.h
%{_includedir}/libart-2.0/libart_lgpl/art_filterlevel.h
%{_includedir}/libart-2.0/libart_lgpl/art_gray_svp.h
%{_includedir}/libart-2.0/libart_lgpl/art_misc.h
%{_includedir}/libart-2.0/libart_lgpl/art_pathcode.h
%{_includedir}/libart-2.0/libart_lgpl/art_pixbuf.h
%{_includedir}/libart-2.0/libart_lgpl/art_point.h
%{_includedir}/libart-2.0/libart_lgpl/art_rect.h
%{_includedir}/libart-2.0/libart_lgpl/art_rect_svp.h
%{_includedir}/libart-2.0/libart_lgpl/art_rect_uta.h
%{_includedir}/libart-2.0/libart_lgpl/art_render.h
%{_includedir}/libart-2.0/libart_lgpl/art_render_gradient.h
%{_includedir}/libart-2.0/libart_lgpl/art_render_mask.h
%{_includedir}/libart-2.0/libart_lgpl/art_render_svp.h
%{_includedir}/libart-2.0/libart_lgpl/art_rgb.h
%{_includedir}/libart-2.0/libart_lgpl/art_rgb_a_affine.h
%{_includedir}/libart-2.0/libart_lgpl/art_rgb_affine.h
%{_includedir}/libart-2.0/libart_lgpl/art_rgb_bitmap_affine.h
%{_includedir}/libart-2.0/libart_lgpl/art_rgb_pixbuf_affine.h
%{_includedir}/libart-2.0/libart_lgpl/art_rgb_rgba_affine.h
%{_includedir}/libart-2.0/libart_lgpl/art_rgb_svp.h
%{_includedir}/libart-2.0/libart_lgpl/art_rgba.h
%{_includedir}/libart-2.0/libart_lgpl/art_svp.h
%{_includedir}/libart-2.0/libart_lgpl/art_svp_intersect.h
%{_includedir}/libart-2.0/libart_lgpl/art_svp_ops.h
%{_includedir}/libart-2.0/libart_lgpl/art_svp_point.h
%{_includedir}/libart-2.0/libart_lgpl/art_svp_render_aa.h
%{_includedir}/libart-2.0/libart_lgpl/art_svp_vpath.h
%{_includedir}/libart-2.0/libart_lgpl/art_svp_vpath_stroke.h
%{_includedir}/libart-2.0/libart_lgpl/art_svp_wind.h
%{_includedir}/libart-2.0/libart_lgpl/art_uta.h
%{_includedir}/libart-2.0/libart_lgpl/art_uta_ops.h
%{_includedir}/libart-2.0/libart_lgpl/art_uta_rect.h
%{_includedir}/libart-2.0/libart_lgpl/art_uta_svp.h
%{_includedir}/libart-2.0/libart_lgpl/art_uta_vpath.h
%{_includedir}/libart-2.0/libart_lgpl/art_vpath.h
%{_includedir}/libart-2.0/libart_lgpl/art_vpath_bpath.h
%{_includedir}/libart-2.0/libart_lgpl/art_vpath_dash.h
%{_includedir}/libart-2.0/libart_lgpl/art_vpath_svp.h
%{_includedir}/libart-2.0/libart_lgpl/libart-features.h
%{_includedir}/libart-2.0/libart_lgpl/libart.h
%{_libdir}/pkgconfig/libart-2.0.pc
%{_mandir}/man1/libart2-config.*

##########

%prep
%setup -q -n %name


%build
unset QTDIR QTINC QTLIB

#было:
#if ! rpm -E %%cmake|grep -e 'cd build\|cd ${CMAKE_BUILD_DIR:-build}'; then
#  mkdir -p build
#  cd build
#fi
#стало:

%{suse_cmake} \
  -DCMAKE_BUILD_TYPE="RelWithDebInfo" \
  -DCMAKE_C_FLAGS="${RPM_OPT_FLAGS}" \
  -DCMAKE_CXX_FLAGS="${RPM_OPT_FLAGS}" \
  -DCMAKE_SKIP_RPATH=OFF \
  -DCMAKE_SKIP_INSTALL_RPATH=OFF \
  -DCMAKE_VERBOSE_MAKEFILE=ON \
  -DWITH_GCC_VISIBILITY=OFF \
  \
  -DCMAKE_INSTALL_PREFIX="%{_prefix}" \
  -DLIB_INSTALL_DIR="%{_libdir}" \
  -DSHARE_INSTALL_PREFIX="%{_datadir}" \
  \
  -DWITH_ALL_OPTIONS=ON \
  -DWITH_GCC_VISIBILITY=ON \
  \
  -DBUILD_ALL=ON \
  -DBUILD_DOC=ON \
  -DBUILD_TRANSLATIONS=ON \
  \
  ..

make %{?_smp_mflags} || make


%install
make install DESTDIR=$RPM_BUILD_ROOT -C build


%changelog
* Thu Jan 23 2025 Petr Akhlamov <ahlamovpm@basealt.ru> 14.1.3_1
- converted for ALT Linux by srpmconvert tools

