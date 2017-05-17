#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : alsa-lib
Version  : 1.1.4
Release  : 15
URL      : ftp://ftp.alsa-project.org/pub/lib/alsa-lib-1.1.4.tar.bz2
Source0  : ftp://ftp.alsa-project.org/pub/lib/alsa-lib-1.1.4.tar.bz2
Summary  : Advanced Linux Sound Architecture (ALSA) - Library
Group    : Development/Tools
License  : GPL-2.0 LGPL-2.1
Requires: alsa-lib-bin
Requires: alsa-lib-lib
Requires: alsa-lib-data
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
BuildRequires : python-dev
Patch1: 0001-Support-a-stateless-configuration-by-default-using-P.patch

%description
You can place files named *.conf in this folder and they will be processed
when initialising alsa-lib.

%package bin
Summary: bin components for the alsa-lib package.
Group: Binaries
Requires: alsa-lib-data

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
Requires: alsa-lib-lib
Requires: alsa-lib-bin
Requires: alsa-lib-data
Provides: alsa-lib-devel

%description dev
dev components for the alsa-lib package.


%package dev32
Summary: dev32 components for the alsa-lib package.
Group: Default
Requires: alsa-lib-lib32
Requires: alsa-lib-bin
Requires: alsa-lib-data
Requires: alsa-lib-dev

%description dev32
dev32 components for the alsa-lib package.


%package lib
Summary: lib components for the alsa-lib package.
Group: Libraries
Requires: alsa-lib-data

%description lib
lib components for the alsa-lib package.


%package lib32
Summary: lib32 components for the alsa-lib package.
Group: Default
Requires: alsa-lib-data

%description lib32
lib32 components for the alsa-lib package.


%prep
%setup -q -n alsa-lib-1.1.4
%patch1 -p1
pushd ..
cp -a alsa-lib-1.1.4 build32
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1495033325
%reconfigure --disable-static
make V=1  %{?_smp_mflags}
pushd ../build32/
export PKG_CONFIG_PATH="/usr/lib32/pkgconfig"
export CFLAGS="$CFLAGS -m32"
export CXXFLAGS="$CXXFLAGS -m32"
export LDFLAGS="$LDFLAGS -m32"
%reconfigure --disable-static  --disable-python --libdir=/usr/lib32 --build=i686-generic-linux-gnu --host=i686-generic-linux-gnu --target=i686-clr-linux-gnu
make V=1  %{?_smp_mflags}
popd

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1495033325
rm -rf %{buildroot}
pushd ../build32/
%make_install32
if [ -d  %{buildroot}/usr/lib32/pkgconfig ]
then
pushd %{buildroot}/usr/lib32/pkgconfig
for i in *.pc ; do ln -s $i 32$i ; done
popd
fi
popd
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/aserver

%files data
%defattr(-,root,root,-)
/usr/share/alsa/alsa.conf
/usr/share/alsa/alsa.conf.d/README
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
/usr/share/alsa/cards/SI7018/sndoc-mixer.alisp
/usr/share/alsa/cards/SI7018/sndop-mixer.alisp
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
/usr/share/alsa/cards/aliases.alisp
/usr/share/alsa/cards/aliases.conf
/usr/share/alsa/cards/pistachio-card.conf
/usr/share/alsa/cards/vc4-hdmi.conf
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
/usr/share/alsa/smixer.conf
/usr/share/alsa/sndo-mixer.alisp
/usr/share/alsa/topology/broadwell/broadwell.conf
/usr/share/alsa/topology/bxtrt298/bxt_i2s.conf
/usr/share/alsa/topology/sklrt286/skl_i2s.conf
/usr/share/alsa/ucm/DAISY-I2S/DAISY-I2S.conf
/usr/share/alsa/ucm/DAISY-I2S/HiFi.conf
/usr/share/alsa/ucm/DB410c/DB410c.conf
/usr/share/alsa/ucm/DB410c/HDMI
/usr/share/alsa/ucm/DB410c/HiFi
/usr/share/alsa/ucm/GoogleNyan/GoogleNyan.conf
/usr/share/alsa/ucm/GoogleNyan/HiFi.conf
/usr/share/alsa/ucm/PAZ00/HiFi.conf
/usr/share/alsa/ucm/PAZ00/PAZ00.conf
/usr/share/alsa/ucm/PAZ00/Record.conf
/usr/share/alsa/ucm/PandaBoard/FMAnalog
/usr/share/alsa/ucm/PandaBoard/PandaBoard.conf
/usr/share/alsa/ucm/PandaBoard/hifi
/usr/share/alsa/ucm/PandaBoard/hifiLP
/usr/share/alsa/ucm/PandaBoard/record
/usr/share/alsa/ucm/PandaBoard/voice
/usr/share/alsa/ucm/PandaBoard/voiceCall
/usr/share/alsa/ucm/PandaBoardES/FMAnalog
/usr/share/alsa/ucm/PandaBoardES/PandaBoardES.conf
/usr/share/alsa/ucm/PandaBoardES/hifi
/usr/share/alsa/ucm/PandaBoardES/hifiLP
/usr/share/alsa/ucm/PandaBoardES/record
/usr/share/alsa/ucm/PandaBoardES/voice
/usr/share/alsa/ucm/PandaBoardES/voiceCall
/usr/share/alsa/ucm/SDP4430/FMAnalog
/usr/share/alsa/ucm/SDP4430/SDP4430.conf
/usr/share/alsa/ucm/SDP4430/hifi
/usr/share/alsa/ucm/SDP4430/hifiLP
/usr/share/alsa/ucm/SDP4430/record
/usr/share/alsa/ucm/SDP4430/voice
/usr/share/alsa/ucm/SDP4430/voiceCall
/usr/share/alsa/ucm/VEYRON-I2S/HiFi.conf
/usr/share/alsa/ucm/VEYRON-I2S/VEYRON-I2S.conf
/usr/share/alsa/ucm/broadwell-rt286/HiFi
/usr/share/alsa/ucm/broadwell-rt286/broadwell-rt286.conf
/usr/share/alsa/ucm/broxton-rt298/Hdmi1
/usr/share/alsa/ucm/broxton-rt298/Hdmi2
/usr/share/alsa/ucm/broxton-rt298/HiFi
/usr/share/alsa/ucm/broxton-rt298/broxton-rt298.conf
/usr/share/alsa/ucm/chtrt5645/HiFi.conf
/usr/share/alsa/ucm/chtrt5645/chtrt5645.conf
/usr/share/alsa/ucm/skylake-rt286/Hdmi1
/usr/share/alsa/ucm/skylake-rt286/Hdmi2
/usr/share/alsa/ucm/skylake-rt286/HiFi
/usr/share/alsa/ucm/skylake-rt286/skylake-rt286.conf
/usr/share/alsa/ucm/tegraalc5632/tegraalc5632.conf
/usr/share/defaults/alsa/asound.conf

%files dev
%defattr(-,root,root,-)
/usr/include/alsa/alisp.h
/usr/include/alsa/asoundef.h
/usr/include/alsa/asoundlib.h
/usr/include/alsa/conf.h
/usr/include/alsa/control.h
/usr/include/alsa/control_external.h
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
/usr/include/alsa/timer.h
/usr/include/alsa/topology.h
/usr/include/alsa/use-case.h
/usr/include/alsa/version.h
/usr/include/sys/asoundlib.h
/usr/lib64/libasound.so
/usr/lib64/pkgconfig/alsa.pc
/usr/share/aclocal/*.m4

%files dev32
%defattr(-,root,root,-)
/usr/lib32/libasound.so
/usr/lib32/pkgconfig/32alsa.pc
/usr/lib32/pkgconfig/alsa.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/alsa-lib/smixer/smixer-ac97.so
/usr/lib64/alsa-lib/smixer/smixer-hda.so
/usr/lib64/alsa-lib/smixer/smixer-python.so
/usr/lib64/alsa-lib/smixer/smixer-sbase.so
/usr/lib64/libasound.so.2
/usr/lib64/libasound.so.2.0.0

%files lib32
%defattr(-,root,root,-)
/usr/lib32/libasound.so.2
/usr/lib32/libasound.so.2.0.0
