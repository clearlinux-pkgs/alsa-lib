#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: configure
# autospec version: v10
# autospec commit: 5905be9
#
# Source0 file verified with key 0x8380596DA6E59C91 (release@alsa-project.org)
#
Name     : alsa-lib
Version  : 1.2.11
Release  : 65
URL      : https://www.alsa-project.org/files/pub/lib/alsa-lib-1.2.11.tar.bz2
Source0  : https://www.alsa-project.org/files/pub/lib/alsa-lib-1.2.11.tar.bz2
Source1  : https://www.alsa-project.org/files/pub/lib/alsa-lib-1.2.11.tar.bz2.sig
Source2  : 8380596DA6E59C91.pkey
Summary  : Advanced Linux Sound Architecture (ALSA) - Topology Library
Group    : Development/Tools
License  : GPL-2.0 LGPL-2.1
Requires: alsa-lib-bin = %{version}-%{release}
Requires: alsa-lib-data = %{version}-%{release}
Requires: alsa-lib-lib = %{version}-%{release}
Requires: alsa-lib-license = %{version}-%{release}
Requires: alsa-ucm-conf-data
BuildRequires : buildreq-configure
BuildRequires : file
BuildRequires : gcc-dev32
BuildRequires : gcc-libgcc32
BuildRequires : gcc-libstdc++32
BuildRequires : glibc-dev32
BuildRequires : glibc-libc32
BuildRequires : gnupg
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}
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


%package lib
Summary: lib components for the alsa-lib package.
Group: Libraries
Requires: alsa-lib-data = %{version}-%{release}
Requires: alsa-lib-license = %{version}-%{release}

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
mkdir .gnupg
chmod 700 .gnupg
gpg --homedir .gnupg --import %{SOURCE2}
gpg --homedir .gnupg --status-fd 1 --verify %{SOURCE1} %{SOURCE0} > gpg.status
grep -E '^\[GNUPG:\] (GOODSIG|EXPKEYSIG) 8380596DA6E59C91' gpg.status
%setup -q -n alsa-lib-1.2.11
cd %{_builddir}/alsa-lib-1.2.11
%patch -P 1 -p1
pushd ..
cp -a alsa-lib-1.2.11 build32
popd
pushd ..
cp -a alsa-lib-1.2.11 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1713219907
export GCC_IGNORE_WERROR=1
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -Ofast -falign-functions=32 -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -Ofast -falign-functions=32 -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -Ofast -falign-functions=32 -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -Ofast -falign-functions=32 -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
%reconfigure --disable-static --disable-python
make  %{?_smp_mflags}
pushd ../build32/
export PKG_CONFIG_PATH="/usr/lib32/pkgconfig:/usr/share/pkgconfig"
ASFLAGS="${CLEAR_INTERMEDIATE_ASFLAGS}${CLEAR_INTERMEDIATE_ASFLAGS:+ }--32"
CFLAGS="${CLEAR_INTERMEDIATE_CFLAGS}${CLEAR_INTERMEDIATE_CFLAGS:+ }-m32 -mstackrealign"
CXXFLAGS="${CLEAR_INTERMEDIATE_CXXFLAGS}${CLEAR_INTERMEDIATE_CXXFLAGS:+ }-m32 -mstackrealign"
LDFLAGS="${CLEAR_INTERMEDIATE_LDFLAGS}${CLEAR_INTERMEDIATE_LDFLAGS:+ }-m32 -mstackrealign"
%reconfigure --disable-static --disable-python  --libdir=/usr/lib32 --build=i686-generic-linux-gnu --host=i686-generic-linux-gnu --target=i686-clr-linux-gnu
make  %{?_smp_mflags}
popd
unset PKG_CONFIG_PATH
pushd ../buildavx2/
GOAMD64=v3
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS -march=x86-64-v3 "
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
export GCC_IGNORE_WERROR=1
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -Ofast -falign-functions=32 -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -Ofast -falign-functions=32 -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -Ofast -falign-functions=32 -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -Ofast -falign-functions=32 -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1713219907
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/alsa-lib
cp %{_builddir}/alsa-lib-%{version}/COPYING %{buildroot}/usr/share/package-licenses/alsa-lib/597bf5f9c0904bd6c48ac3a3527685818d11246d || :
cp %{_builddir}/alsa-lib-%{version}/aserver/COPYING %{buildroot}/usr/share/package-licenses/alsa-lib/e5872dbffaaad55b275bdbcb8b377385c655c5bc || :
export GOAMD64=v2
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
GOAMD64=v3
pushd ../buildavx2/
%make_install_v3
popd
GOAMD64=v2
%make_install
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/V3/usr/bin/aserver
/usr/bin/aserver

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
/usr/include/alsa/ump.h
/usr/include/alsa/ump_msg.h
/usr/include/alsa/use-case.h
/usr/include/alsa/version.h
/usr/include/asoundlib.h
/usr/include/sys/asoundlib.h
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

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/libasound.so.2.0.0
/V3/usr/lib64/libatopology.so.2.0.0
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
