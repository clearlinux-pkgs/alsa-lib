#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : alsa-lib
Version  : 1.1.9
Release  : 28
URL      : https://www.alsa-project.org/files/pub/lib/alsa-lib-1.1.9.tar.bz2
Source0  : https://www.alsa-project.org/files/pub/lib/alsa-lib-1.1.9.tar.bz2
Summary  : Advanced Linux Sound Architecture (ALSA) - Library
Group    : Development/Tools
License  : GPL-2.0 LGPL-2.1
Requires: alsa-lib-bin = %{version}-%{release}
Requires: alsa-lib-data = %{version}-%{release}
Requires: alsa-lib-lib = %{version}-%{release}
Requires: alsa-lib-license = %{version}-%{release}
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
The doxygen documentation is created with command 'make doc' in toplevel
directory.

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
%setup -q -n alsa-lib-1.1.9
%patch1 -p1
pushd ..
cp -a alsa-lib-1.1.9 build32
popd
pushd ..
cp -a alsa-lib-1.1.9 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1568830111
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -O3 -falign-functions=32 -fno-lto -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
export FCFLAGS="$CFLAGS -O3 -falign-functions=32 -fno-lto -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
export FFLAGS="$CFLAGS -O3 -falign-functions=32 -fno-lto -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
export CXXFLAGS="$CXXFLAGS -O3 -falign-functions=32 -fno-lto -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
%reconfigure --disable-static --disable-python
make  %{?_smp_mflags}
pushd ../build32/
export PKG_CONFIG_PATH="/usr/lib32/pkgconfig"
export ASFLAGS="${ASFLAGS}${ASFLAGS:+ }--32"
export CFLAGS="${CFLAGS}${CFLAGS:+ }-m32 -mstackrealign"
export CXXFLAGS="${CXXFLAGS}${CXXFLAGS:+ }-m32 -mstackrealign"
export LDFLAGS="${LDFLAGS}${LDFLAGS:+ }-m32 -mstackrealign"
%reconfigure --disable-static --disable-python  --libdir=/usr/lib32 --build=i686-generic-linux-gnu --host=i686-generic-linux-gnu --target=i686-clr-linux-gnu
make  %{?_smp_mflags}
popd
unset PKG_CONFIG_PATH
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=haswell"
export CXXFLAGS="$CXXFLAGS -m64 -march=haswell"
export LDFLAGS="$LDFLAGS -m64 -march=haswell"
%reconfigure --disable-static --disable-python
make  %{?_smp_mflags}
popd

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check
cd ../build32;
make VERBOSE=1 V=1 %{?_smp_mflags} check || :
cd ../buildavx2;
make VERBOSE=1 V=1 %{?_smp_mflags} check || :

%install
export SOURCE_DATE_EPOCH=1568830111
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/alsa-lib
cp COPYING %{buildroot}/usr/share/package-licenses/alsa-lib/COPYING
cp aserver/COPYING %{buildroot}/usr/share/package-licenses/alsa-lib/aserver_COPYING
pushd ../build32/
%make_install32
if [ -d  %{buildroot}/usr/lib32/pkgconfig ]
then
pushd %{buildroot}/usr/lib32/pkgconfig
for i in *.pc ; do ln -s $i 32$i ; done
popd
fi
popd
pushd ../buildavx2/
%make_install_avx2
popd
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/aserver
/usr/bin/haswell/aserver

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
/usr/share/alsa/topology/broadwell/broadwell.conf
/usr/share/alsa/topology/bxtrt298/bxt_i2s.conf
/usr/share/alsa/topology/sklrt286/skl_i2s.conf
/usr/share/alsa/ucm/ASUSTeKCOMPUTERINC.-T100HAN-1.0-T100HAN/ASUSTeKCOMPUTERINC.-T100HAN-1.0-T100HAN.conf
/usr/share/alsa/ucm/ASUSTeKCOMPUTERINC.-T100HAN-1.0-T100HAN/HiFi.conf
/usr/share/alsa/ucm/DAISY-I2S/DAISY-I2S.conf
/usr/share/alsa/ucm/DAISY-I2S/HiFi.conf
/usr/share/alsa/ucm/DB410c/DB410c.conf
/usr/share/alsa/ucm/DB410c/HDMI
/usr/share/alsa/ucm/DB410c/HiFi
/usr/share/alsa/ucm/DB820c/DB820c.conf
/usr/share/alsa/ucm/DB820c/HDMI
/usr/share/alsa/ucm/DB820c/HiFi
/usr/share/alsa/ucm/Dell-WD15-Dock/Dell-WD15-Dock.conf
/usr/share/alsa/ucm/Dell-WD15-Dock/HiFi.conf
/usr/share/alsa/ucm/GoogleNyan/GoogleNyan.conf
/usr/share/alsa/ucm/GoogleNyan/HiFi.conf
/usr/share/alsa/ucm/HDAudio-Gigabyte-ALC1220DualCodecs/HDAudio-Gigabyte-ALC1220DualCodecs.conf
/usr/share/alsa/ucm/HDAudio-Gigabyte-ALC1220DualCodecs/HiFi.conf
/usr/share/alsa/ucm/HDAudio-Lenovo-DualCodecs/HDAudio-Lenovo-DualCodecs.conf
/usr/share/alsa/ucm/HDAudio-Lenovo-DualCodecs/HiFi.conf
/usr/share/alsa/ucm/LENOVO-80XF-LenovoMIIX320_10ICR-LNVNB161216/HiFi.conf
/usr/share/alsa/ucm/LENOVO-80XF-LenovoMIIX320_10ICR-LNVNB161216/LENOVO-80XF-LenovoMIIX320_10ICR-LNVNB161216.conf
/usr/share/alsa/ucm/PAZ00/HiFi.conf
/usr/share/alsa/ucm/PAZ00/PAZ00.conf
/usr/share/alsa/ucm/PAZ00/Record.conf
/usr/share/alsa/ucm/PIPO-W2S-Defaultstring-CherryTrailCR/HiFi.conf
/usr/share/alsa/ucm/PIPO-W2S-Defaultstring-CherryTrailCR/PIPO-W2S-Defaultstring-CherryTrailCR.conf
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
/usr/share/alsa/ucm/TECLAST-X80Pro-Defaultstring-CherryTrailCR/TECLAST-X80Pro-Defaultstring-CherryTrailCR.conf
/usr/share/alsa/ucm/VEYRON-I2S/HiFi.conf
/usr/share/alsa/ucm/VEYRON-I2S/VEYRON-I2S.conf
/usr/share/alsa/ucm/broadwell-rt286/HiFi
/usr/share/alsa/ucm/broadwell-rt286/broadwell-rt286.conf
/usr/share/alsa/ucm/broxton-rt298/Hdmi1
/usr/share/alsa/ucm/broxton-rt298/Hdmi2
/usr/share/alsa/ucm/broxton-rt298/HiFi
/usr/share/alsa/ucm/broxton-rt298/broxton-rt298.conf
/usr/share/alsa/ucm/bytcht-es8316-mono-spk-in1-mic/HiFi.conf
/usr/share/alsa/ucm/bytcht-es8316-mono-spk-in1-mic/bytcht-es8316-mono-spk-in1-mic.conf
/usr/share/alsa/ucm/bytcht-es8316-mono-spk-in2-mic/HiFi.conf
/usr/share/alsa/ucm/bytcht-es8316-mono-spk-in2-mic/bytcht-es8316-mono-spk-in2-mic.conf
/usr/share/alsa/ucm/bytcht-es8316-stereo-spk-in1-mic/HiFi.conf
/usr/share/alsa/ucm/bytcht-es8316-stereo-spk-in1-mic/bytcht-es8316-stereo-spk-in1-mic.conf
/usr/share/alsa/ucm/bytcht-es8316-stereo-spk-in2-mic/HiFi.conf
/usr/share/alsa/ucm/bytcht-es8316-stereo-spk-in2-mic/bytcht-es8316-stereo-spk-in2-mic.conf
/usr/share/alsa/ucm/bytcht-es8316/HiFi.conf
/usr/share/alsa/ucm/bytcht-es8316/bytcht-es8316.conf
/usr/share/alsa/ucm/bytcr-rt5640-mono-spk-dmic1-mic/HiFi.conf
/usr/share/alsa/ucm/bytcr-rt5640-mono-spk-dmic1-mic/bytcr-rt5640-mono-spk-dmic1-mic.conf
/usr/share/alsa/ucm/bytcr-rt5640-mono-spk-in1-mic/HiFi.conf
/usr/share/alsa/ucm/bytcr-rt5640-mono-spk-in1-mic/bytcr-rt5640-mono-spk-in1-mic.conf
/usr/share/alsa/ucm/bytcr-rt5640-mono-spk-in3-mic/HiFi.conf
/usr/share/alsa/ucm/bytcr-rt5640-mono-spk-in3-mic/bytcr-rt5640-mono-spk-in3-mic.conf
/usr/share/alsa/ucm/bytcr-rt5640-stereo-spk-dmic1-mic/HiFi.conf
/usr/share/alsa/ucm/bytcr-rt5640-stereo-spk-dmic1-mic/bytcr-rt5640-stereo-spk-dmic1-mic.conf
/usr/share/alsa/ucm/bytcr-rt5640-stereo-spk-in1-mic/HiFi.conf
/usr/share/alsa/ucm/bytcr-rt5640-stereo-spk-in1-mic/bytcr-rt5640-stereo-spk-in1-mic.conf
/usr/share/alsa/ucm/bytcr-rt5640-stereo-spk-in3-mic/HiFi.conf
/usr/share/alsa/ucm/bytcr-rt5640-stereo-spk-in3-mic/bytcr-rt5640-stereo-spk-in3-mic.conf
/usr/share/alsa/ucm/bytcr-rt5640/HiFi.conf
/usr/share/alsa/ucm/bytcr-rt5640/bytcr-rt5640.conf
/usr/share/alsa/ucm/bytcr-rt5651-mono-spk-in1-mic/HiFi.conf
/usr/share/alsa/ucm/bytcr-rt5651-mono-spk-in1-mic/bytcr-rt5651-mono-spk-in1-mic.conf
/usr/share/alsa/ucm/bytcr-rt5651-mono-spk-in2-mic-hp-swapped/HiFi.conf
/usr/share/alsa/ucm/bytcr-rt5651-mono-spk-in2-mic-hp-swapped/bytcr-rt5651-mono-spk-in2-mic-hp-swapped.conf
/usr/share/alsa/ucm/bytcr-rt5651-mono-spk-in2-mic/HiFi.conf
/usr/share/alsa/ucm/bytcr-rt5651-mono-spk-in2-mic/bytcr-rt5651-mono-spk-in2-mic.conf
/usr/share/alsa/ucm/bytcr-rt5651-stereo-spk-dmic-mic/HiFi.conf
/usr/share/alsa/ucm/bytcr-rt5651-stereo-spk-dmic-mic/bytcr-rt5651-stereo-spk-dmic-mic.conf
/usr/share/alsa/ucm/bytcr-rt5651-stereo-spk-in1-mic/HiFi.conf
/usr/share/alsa/ucm/bytcr-rt5651-stereo-spk-in1-mic/bytcr-rt5651-stereo-spk-in1-mic.conf
/usr/share/alsa/ucm/bytcr-rt5651-stereo-spk-in12-mic/HiFi.conf
/usr/share/alsa/ucm/bytcr-rt5651-stereo-spk-in12-mic/bytcr-rt5651-stereo-spk-in12-mic.conf
/usr/share/alsa/ucm/bytcr-rt5651-stereo-spk-in2-mic/HiFi.conf
/usr/share/alsa/ucm/bytcr-rt5651-stereo-spk-in2-mic/bytcr-rt5651-stereo-spk-in2-mic.conf
/usr/share/alsa/ucm/bytcr-rt5651/HiFi.conf
/usr/share/alsa/ucm/bytcr-rt5651/bytcr-rt5651.conf
/usr/share/alsa/ucm/chtnau8824/HiFi.conf
/usr/share/alsa/ucm/chtnau8824/chtnau8824.conf
/usr/share/alsa/ucm/chtrt5645-mono-speaker-analog-mic/HiFi.conf
/usr/share/alsa/ucm/chtrt5645-mono-speaker-analog-mic/chtrt5645-mono-speaker-analog-mic.conf
/usr/share/alsa/ucm/chtrt5645/HiFi.conf
/usr/share/alsa/ucm/chtrt5645/chtrt5645.conf
/usr/share/alsa/ucm/chtrt5650/HiFi.conf
/usr/share/alsa/ucm/chtrt5650/chtrt5650.conf
/usr/share/alsa/ucm/codecs/es8316/EnableSeq.conf
/usr/share/alsa/ucm/codecs/es8316/HeadPhones.conf
/usr/share/alsa/ucm/codecs/es8316/IN1-HeadsetMic.conf
/usr/share/alsa/ucm/codecs/es8316/IN1-InternalMic.conf
/usr/share/alsa/ucm/codecs/es8316/IN2-HeadsetMic.conf
/usr/share/alsa/ucm/codecs/es8316/IN2-InternalMic.conf
/usr/share/alsa/ucm/codecs/es8316/MonoSpeaker.conf
/usr/share/alsa/ucm/codecs/es8316/Speaker.conf
/usr/share/alsa/ucm/codecs/nau8824/EnableSeq.conf
/usr/share/alsa/ucm/codecs/nau8824/HeadPhones.conf
/usr/share/alsa/ucm/codecs/nau8824/HeadsetMic.conf
/usr/share/alsa/ucm/codecs/nau8824/InternalMic.conf
/usr/share/alsa/ucm/codecs/nau8824/MonoSpeaker.conf
/usr/share/alsa/ucm/codecs/nau8824/Speaker.conf
/usr/share/alsa/ucm/codecs/rt5640/DigitalMics.conf
/usr/share/alsa/ucm/codecs/rt5640/EnableSeq.conf
/usr/share/alsa/ucm/codecs/rt5640/HeadPhones.conf
/usr/share/alsa/ucm/codecs/rt5640/HeadsetMic.conf
/usr/share/alsa/ucm/codecs/rt5640/IN1-InternalMic.conf
/usr/share/alsa/ucm/codecs/rt5640/IN3-InternalMic.conf
/usr/share/alsa/ucm/codecs/rt5640/MonoSpeaker.conf
/usr/share/alsa/ucm/codecs/rt5640/Speaker.conf
/usr/share/alsa/ucm/codecs/rt5645/AnalogMic.conf
/usr/share/alsa/ucm/codecs/rt5645/DigitalMicDisableSeq.conf
/usr/share/alsa/ucm/codecs/rt5645/DigitalMicEnableSeq.conf
/usr/share/alsa/ucm/codecs/rt5645/DisableSeq.conf
/usr/share/alsa/ucm/codecs/rt5645/EnableSeq.conf
/usr/share/alsa/ucm/codecs/rt5645/HSMicDisableSeq.conf
/usr/share/alsa/ucm/codecs/rt5645/HSMicEnableSeq.conf
/usr/share/alsa/ucm/codecs/rt5645/HeadphonesEnableSeq.conf
/usr/share/alsa/ucm/codecs/rt5645/SpeakerEnableSeq.conf
/usr/share/alsa/ucm/codecs/rt5651/DigitalMic.conf
/usr/share/alsa/ucm/codecs/rt5651/EnableSeq.conf
/usr/share/alsa/ucm/codecs/rt5651/HeadPhones-swapped.conf
/usr/share/alsa/ucm/codecs/rt5651/HeadPhones.conf
/usr/share/alsa/ucm/codecs/rt5651/IN1-InternalMic.conf
/usr/share/alsa/ucm/codecs/rt5651/IN12-InternalMic.conf
/usr/share/alsa/ucm/codecs/rt5651/IN2-HeadsetMic.conf
/usr/share/alsa/ucm/codecs/rt5651/IN2-InternalMic.conf
/usr/share/alsa/ucm/codecs/rt5651/IN3-HeadsetMic.conf
/usr/share/alsa/ucm/codecs/rt5651/MonoSpeaker.conf
/usr/share/alsa/ucm/codecs/rt5651/Speaker.conf
/usr/share/alsa/ucm/cube-i1_TF-Defaultstring-CherryTrailCR/HiFi.conf
/usr/share/alsa/ucm/cube-i1_TF-Defaultstring-CherryTrailCR/cube-i1_TF-Defaultstring-CherryTrailCR.conf
/usr/share/alsa/ucm/gpd-win-pocket-rt5645/gpd-win-pocket-rt5645.conf
/usr/share/alsa/ucm/kblrt5660/Hdmi1
/usr/share/alsa/ucm/kblrt5660/Hdmi2
/usr/share/alsa/ucm/kblrt5660/HiFi
/usr/share/alsa/ucm/kblrt5660/kblrt5660.conf
/usr/share/alsa/ucm/platforms/bytcr/PlatformDisableSeq.conf
/usr/share/alsa/ucm/platforms/bytcr/PlatformEnableSeq.conf
/usr/share/alsa/ucm/skylake-rt286/Hdmi1
/usr/share/alsa/ucm/skylake-rt286/Hdmi2
/usr/share/alsa/ucm/skylake-rt286/HiFi
/usr/share/alsa/ucm/skylake-rt286/skylake-rt286.conf
/usr/share/alsa/ucm/tegraalc5632/tegraalc5632.conf
/usr/share/defaults/alsa/asound.conf

%files dev
%defattr(-,root,root,-)
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
/usr/include/asoundlib.h
/usr/include/sys/asoundlib.h
/usr/lib64/haswell/libasound.so
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
/usr/lib64/haswell/libasound.so.2
/usr/lib64/haswell/libasound.so.2.0.0
/usr/lib64/libasound.so.2
/usr/lib64/libasound.so.2.0.0

%files lib32
%defattr(-,root,root,-)
/usr/lib32/libasound.so.2
/usr/lib32/libasound.so.2.0.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/alsa-lib/COPYING
/usr/share/package-licenses/alsa-lib/aserver_COPYING
