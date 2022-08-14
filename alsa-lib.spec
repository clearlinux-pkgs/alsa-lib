#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x8380596DA6E59C91 (release@alsa-project.org)
#
Name     : alsa-lib
Version  : 1.2.7.2
Release  : 53
URL      : https://www.alsa-project.org/files/pub/lib/alsa-lib-1.2.7.2.tar.bz2
Source0  : https://www.alsa-project.org/files/pub/lib/alsa-lib-1.2.7.2.tar.bz2
Source1  : https://www.alsa-project.org/files/pub/lib/alsa-lib-1.2.7.2.tar.bz2.sig
Summary  : Advanced Linux Sound Architecture (ALSA) - Library
Group    : Development/Tools
License  : GPL-2.0 LGPL-2.1
Requires: alsa-lib-bin = %{version}-%{release}
Requires: alsa-lib-data = %{version}-%{release}
Requires: alsa-lib-filemap = %{version}-%{release}
Requires: alsa-lib-lib = %{version}-%{release}
Requires: alsa-lib-license = %{version}-%{release}
Requires: alsa-ucm-conf-data
BuildRequires : automake
BuildRequires : automake-dev
BuildRequires : gcc-dev32
BuildRequires : gcc-libgcc32
BuildRequires : gcc-libstdc++32
BuildRequires : gettext-bin
BuildRequires : glibc-dev32
BuildRequires : glibc-libc32
BuildRequires : libtool
BuildRequires : libtool-dev
BuildRequires : m4
BuildRequires : pkg-config-dev
Patch1: 0001-Support-a-stateless-configuration-by-default-using-P.patch

%description
# alsa-lib
## Advanced Linux Sound Architecture (ALSA) project
[![Build alsa-lib](https://github.com/alsa-project/alsa-lib/workflows/Build%20alsa-lib/badge.svg?branch=master)](https://github.com/alsa-project/alsa-lib/actions/workflows/build.yml)

%package bin
Summary: bin components for the alsa-lib package.
Group: Binaries
Requires: alsa-lib-data = %{version}-%{release}
Requires: alsa-lib-license = %{version}-%{release}
Requires: alsa-lib-filemap = %{version}-%{release}

%description bin
bin components for the alsa-lib package.


%package data
Summary: data components for the alsa-lib package.
Group: Data

%description data
data components for the alsa-lib package.


%package dev
Summary: dev components for the alsa-lib package.
Group: Development
Requires: alsa-lib-lib = %{version}-%{release}
Requires: alsa-lib-bin = %{version}-%{release}
Requires: alsa-lib-data = %{version}-%{release}
Provides: alsa-lib-devel = %{version}-%{release}
Requires: alsa-lib = %{version}-%{release}

%description dev
dev components for the alsa-lib package.


%package dev32
Summary: dev32 components for the alsa-lib package.
Group: Default
Requires: alsa-lib-lib32 = %{version}-%{release}
Requires: alsa-lib-bin = %{version}-%{release}
Requires: alsa-lib-data = %{version}-%{release}
Requires: alsa-lib-dev = %{version}-%{release}

%description dev32
dev32 components for the alsa-lib package.


%package filemap
Summary: filemap components for the alsa-lib package.
Group: Default

%description filemap
filemap components for the alsa-lib package.


%package lib
Summary: lib components for the alsa-lib package.
Group: Libraries
Requires: alsa-lib-data = %{version}-%{release}
Requires: alsa-lib-license = %{version}-%{release}
Requires: alsa-lib-filemap = %{version}-%{release}

%description lib
lib components for the alsa-lib package.


%package lib32
Summary: lib32 components for the alsa-lib package.
Group: Default
Requires: alsa-lib-data = %{version}-%{release}
Requires: alsa-lib-license = %{version}-%{release}

%description lib32
lib32 components for the alsa-lib package.


%package license
Summary: license components for the alsa-lib package.
Group: Default

%description license
license components for the alsa-lib package.


%prep
%setup -q -n alsa-lib-1.2.7.2
cd %{_builddir}/alsa-lib-1.2.7.2
%patch1 -p1
pushd ..
cp -a alsa-lib-1.2.7.2 build32
popd
pushd ..
cp -a alsa-lib-1.2.7.2 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1657310849
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -Ofast -falign-functions=32 -fno-lto -fno-semantic-interposition -mprefer-vector-width=256 "
export FCFLAGS="$FFLAGS -Ofast -falign-functions=32 -fno-lto -fno-semantic-interposition -mprefer-vector-width=256 "
export FFLAGS="$FFLAGS -Ofast -falign-functions=32 -fno-lto -fno-semantic-interposition -mprefer-vector-width=256 "
export CXXFLAGS="$CXXFLAGS -Ofast -falign-functions=32 -fno-lto -fno-semantic-interposition -mprefer-vector-width=256 "
%reconfigure --disable-static --disable-python
make  %{?_smp_mflags}
pushd ../build32/
export PKG_CONFIG_PATH="/usr/lib32/pkgconfig:/usr/share/pkgconfig"
export ASFLAGS="${ASFLAGS}${ASFLAGS:+ }--32"
export CFLAGS="${CFLAGS}${CFLAGS:+ }-m32 -mstackrealign"
export CXXFLAGS="${CXXFLAGS}${CXXFLAGS:+ }-m32 -mstackrealign"
export LDFLAGS="${LDFLAGS}${LDFLAGS:+ }-m32 -mstackrealign"
%reconfigure --disable-static --disable-python  --libdir=/usr/lib32 --build=i686-generic-linux-gnu --host=i686-generic-linux-gnu --target=i686-clr-linux-gnu
make  %{?_smp_mflags}
popd
unset PKG_CONFIG_PATH
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3"
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3"
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3"
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3"
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3"
%reconfigure --disable-static --disable-python
make  %{?_smp_mflags}
popd

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make %{?_smp_mflags} check
cd ../build32;
make %{?_smp_mflags} check || :
cd ../buildavx2;
make %{?_smp_mflags} check || :

%install
export SOURCE_DATE_EPOCH=1657310849
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/alsa-lib
cp %{_builddir}/alsa-lib-1.2.7.2/COPYING %{buildroot}/usr/share/package-licenses/alsa-lib/597bf5f9c0904bd6c48ac3a3527685818d11246d
cp %{_builddir}/alsa-lib-1.2.7.2/aserver/COPYING %{buildroot}/usr/share/package-licenses/alsa-lib/e5872dbffaaad55b275bdbcb8b377385c655c5bc
pushd ../build32/
%make_install32
if [ -d  %{buildroot}/usr/lib32/pkgconfig ]
then
pushd %{buildroot}/usr/lib32/pkgconfig
for i in *.pc ; do ln -s $i 32$i ; done
popd
fi
if [ -d %{buildroot}/usr/share/pkgconfig ]
then
pushd %{buildroot}/usr/share/pkgconfig
for i in *.pc ; do ln -s $i 32$i ; done
popd
fi
popd
pushd ../buildavx2/
%make_install_v3
popd
%make_install
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/aserver
/usr/share/clear/optimized-elf/bin*

%files data
%defattr(-,root,root,-)
/usr/share/alsa/alsa.conf
/usr/share/alsa/cards/AACI.conf
/usr/share/alsa/cards/ATIIXP-MODEM.conf
/usr/share/alsa/cards/ATIIXP-SPDMA.conf
/usr/share/alsa/cards/ATIIXP.conf
/usr/share/alsa/cards/AU8810.conf
/usr/share/alsa/cards/AU8820.conf
/usr/share/alsa/cards/AU8830.conf
/usr/share/alsa/cards/Audigy.conf
/usr/share/alsa/cards/Audigy2.conf
/usr/share/alsa/cards/Aureon51.conf
/usr/share/alsa/cards/Aureon71.conf
/usr/share/alsa/cards/CA0106.conf
/usr/share/alsa/cards/CMI8338-SWIEC.conf
/usr/share/alsa/cards/CMI8338.conf
/usr/share/alsa/cards/CMI8738-MC6.conf
/usr/share/alsa/cards/CMI8738-MC8.conf
/usr/share/alsa/cards/CMI8788.conf
/usr/share/alsa/cards/CS46xx.conf
/usr/share/alsa/cards/EMU10K1.conf
/usr/share/alsa/cards/EMU10K1X.conf
/usr/share/alsa/cards/ENS1370.conf
/usr/share/alsa/cards/ENS1371.conf
/usr/share/alsa/cards/ES1968.conf
/usr/share/alsa/cards/Echo_Echo3G.conf
/usr/share/alsa/cards/FM801.conf
/usr/share/alsa/cards/FWSpeakers.conf
/usr/share/alsa/cards/FireWave.conf
/usr/share/alsa/cards/GUS.conf
/usr/share/alsa/cards/HDA-Intel.conf
/usr/share/alsa/cards/HdmiLpeAudio.conf
/usr/share/alsa/cards/ICE1712.conf
/usr/share/alsa/cards/ICE1724.conf
/usr/share/alsa/cards/ICH-MODEM.conf
/usr/share/alsa/cards/ICH.conf
/usr/share/alsa/cards/ICH4.conf
/usr/share/alsa/cards/Loopback.conf
/usr/share/alsa/cards/Maestro3.conf
/usr/share/alsa/cards/NFORCE.conf
/usr/share/alsa/cards/PC-Speaker.conf
/usr/share/alsa/cards/PMac.conf
/usr/share/alsa/cards/PMacToonie.conf
/usr/share/alsa/cards/PS3.conf
/usr/share/alsa/cards/RME9636.conf
/usr/share/alsa/cards/RME9652.conf
/usr/share/alsa/cards/SB-XFi.conf
/usr/share/alsa/cards/SI7018.conf
/usr/share/alsa/cards/TRID4DWAVENX.conf
/usr/share/alsa/cards/USB-Audio.conf
/usr/share/alsa/cards/VIA686A.conf
/usr/share/alsa/cards/VIA8233.conf
/usr/share/alsa/cards/VIA8233A.conf
/usr/share/alsa/cards/VIA8237.conf
/usr/share/alsa/cards/VX222.conf
/usr/share/alsa/cards/VXPocket.conf
/usr/share/alsa/cards/VXPocket440.conf
/usr/share/alsa/cards/YMF744.conf
/usr/share/alsa/cards/aliases.conf
/usr/share/alsa/cards/pistachio-card.conf
/usr/share/alsa/cards/vc4-hdmi.conf
/usr/share/alsa/ctl/default.conf
/usr/share/alsa/pcm/center_lfe.conf
/usr/share/alsa/pcm/default.conf
/usr/share/alsa/pcm/dmix.conf
/usr/share/alsa/pcm/dpl.conf
/usr/share/alsa/pcm/dsnoop.conf
/usr/share/alsa/pcm/front.conf
/usr/share/alsa/pcm/hdmi.conf
/usr/share/alsa/pcm/iec958.conf
/usr/share/alsa/pcm/modem.conf
/usr/share/alsa/pcm/rear.conf
/usr/share/alsa/pcm/side.conf
/usr/share/alsa/pcm/surround21.conf
/usr/share/alsa/pcm/surround40.conf
/usr/share/alsa/pcm/surround41.conf
/usr/share/alsa/pcm/surround50.conf
/usr/share/alsa/pcm/surround51.conf
/usr/share/alsa/pcm/surround71.conf
/usr/share/defaults/alsa/asound.conf

%files dev
%defattr(-,root,root,-)
/usr/include/alsa/asoundef.h
/usr/include/alsa/asoundlib.h
/usr/include/alsa/conf.h
/usr/include/alsa/control.h
/usr/include/alsa/control_external.h
/usr/include/alsa/control_plugin.h
/usr/include/alsa/error.h
/usr/include/alsa/global.h
/usr/include/alsa/hwdep.h
/usr/include/alsa/input.h
/usr/include/alsa/mixer.h
/usr/include/alsa/mixer_abst.h
/usr/include/alsa/output.h
/usr/include/alsa/pcm.h
/usr/include/alsa/pcm_external.h
/usr/include/alsa/pcm_extplug.h
/usr/include/alsa/pcm_ioplug.h
/usr/include/alsa/pcm_old.h
/usr/include/alsa/pcm_plugin.h
/usr/include/alsa/pcm_rate.h
/usr/include/alsa/rawmidi.h
/usr/include/alsa/seq.h
/usr/include/alsa/seq_event.h
/usr/include/alsa/seq_midi_event.h
/usr/include/alsa/seqmid.h
/usr/include/alsa/sound/asoc.h
/usr/include/alsa/sound/asound_fm.h
/usr/include/alsa/sound/emu10k1.h
/usr/include/alsa/sound/hdsp.h
/usr/include/alsa/sound/hdspm.h
/usr/include/alsa/sound/sb16_csp.h
/usr/include/alsa/sound/sscape_ioctl.h
/usr/include/alsa/sound/tlv.h
/usr/include/alsa/sound/type_compat.h
/usr/include/alsa/sound/uapi/asoc.h
/usr/include/alsa/sound/uapi/asound_fm.h
/usr/include/alsa/sound/uapi/emu10k1.h
/usr/include/alsa/sound/uapi/hdsp.h
/usr/include/alsa/sound/uapi/hdspm.h
/usr/include/alsa/sound/uapi/sb16_csp.h
/usr/include/alsa/sound/uapi/sscape_ioctl.h
/usr/include/alsa/sound/uapi/tlv.h
/usr/include/alsa/timer.h
/usr/include/alsa/topology.h
/usr/include/alsa/use-case.h
/usr/include/alsa/version.h
/usr/include/asoundlib.h
/usr/include/sys/asoundlib.h
/usr/lib64/glibc-hwcaps/x86-64-v3/libasound.so
/usr/lib64/glibc-hwcaps/x86-64-v3/libatopology.so
/usr/lib64/libasound.so
/usr/lib64/libatopology.so
/usr/lib64/pkgconfig/alsa-topology.pc
/usr/lib64/pkgconfig/alsa.pc
/usr/share/aclocal/*.m4

%files dev32
%defattr(-,root,root,-)
/usr/lib32/libasound.so
/usr/lib32/libatopology.so
/usr/lib32/pkgconfig/32alsa-topology.pc
/usr/lib32/pkgconfig/32alsa.pc
/usr/lib32/pkgconfig/alsa-topology.pc
/usr/lib32/pkgconfig/alsa.pc

%files filemap
%defattr(-,root,root,-)
/usr/share/clear/filemap/filemap-alsa-lib

%files lib
%defattr(-,root,root,-)
/usr/lib64/glibc-hwcaps/x86-64-v3/libasound.so.2
/usr/lib64/glibc-hwcaps/x86-64-v3/libasound.so.2.0.0
/usr/lib64/glibc-hwcaps/x86-64-v3/libatopology.so.2
/usr/lib64/glibc-hwcaps/x86-64-v3/libatopology.so.2.0.0
/usr/lib64/libasound.so.2
/usr/lib64/libasound.so.2.0.0
/usr/lib64/libatopology.so.2
/usr/lib64/libatopology.so.2.0.0

%files lib32
%defattr(-,root,root,-)
/usr/lib32/libasound.so.2
/usr/lib32/libasound.so.2.0.0
/usr/lib32/libatopology.so.2
/usr/lib32/libatopology.so.2.0.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/alsa-lib/597bf5f9c0904bd6c48ac3a3527685818d11246d
/usr/share/package-licenses/alsa-lib/e5872dbffaaad55b275bdbcb8b377385c655c5bc
