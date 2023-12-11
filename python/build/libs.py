import re
from os.path import abspath

from build.project import Project
from build.zlib import ZlibProject
from build.meson import MesonProject
from build.cmake import CmakeProject
from build.autotools import AutotoolsProject
from build.ffmpeg import FfmpegProject
from build.openssl import OpenSSLProject
from build.boost import BoostProject
from build.jack import JackProject

libmpdclient = MesonProject(
    'https://www.musicpd.org/download/libmpdclient/2/libmpdclient-2.20.tar.xz',
    '18793f68e939c3301e34d8fcadea1f7daa24143941263cecadb80126194e277d',
    'lib/libmpdclient.a',
)

libogg = CmakeProject(
    'http://downloads.xiph.org/releases/ogg/libogg-1.3.5.tar.xz',
    'c4d91be36fc8e54deae7575241e03f4211eb102afb3fc0775fbbc1b740016705',
    'lib/libogg.a',
    [
        '-DBUILD_SHARED_LIBS=OFF',
        '-DINSTALL_DOCS=OFF',
        '-DINSTALL_CMAKE_PACKAGE_MODULE=OFF',
    ],
)

opus = AutotoolsProject(
    'https://downloads.xiph.org/releases/opus/opus-1.4.tar.gz',
    'c9b32b4253be5ae63d1ff16eea06b94b5f0f2951b7a02aceef58e3a3ce49c51f',
    'lib/libopus.a',
    [
        '--disable-shared', '--enable-static',
        '--disable-doc',
        '--disable-extra-programs',
    ],

    # suppress "visibility default" from opus_defines.h
    cppflags='-DOPUS_EXPORT=',
)

flac = AutotoolsProject(
    'http://downloads.xiph.org/releases/flac/flac-1.4.3.tar.xz',
    '6c58e69cd22348f441b861092b825e591d0b822e106de6eb0ee4d05d27205b70',
    'lib/libFLAC.a',
    [
        '--disable-shared', '--enable-static',
        '--disable-stack-smash-protection',
        '--disable-xmms-plugin', '--disable-cpplibs',
        '--disable-doxygen-docs',
        '--disable-programs',
    ],
    subdirs=['include', 'src/libFLAC'],
)

zlib = ZlibProject(
    ('http://zlib.net/zlib-1.3.1.tar.xz',
     'https://github.com/madler/zlib/releases/download/v1.3.1/zlib-1.3.1.tar.xz'),
    '38ef96b8dfe510d42707d9c781877914792541133e1870841463bfa73f883e32',
    'lib/libz.a',
)

libid3tag = AutotoolsProject(
    'ftp://ftp.mars.org/pub/mpeg/libid3tag-0.15.1b.tar.gz',
    'e5808ad997ba32c498803822078748c3',
    'lib/libid3tag.a',
    [
        '--disable-shared', '--enable-static',

        # without this, libid3tag's configure.ac ignores -O* and -f*
        '--disable-debugging',
    ],
    autogen=True,

    edits={
        # fix bug in libid3tag's configure.ac which discards all but the last optimization flag
        'configure.ac': lambda data: re.sub(r'optimize="\$1"', r'optimize="$optimize $1"', data, count=1),
    }
)

libmad = AutotoolsProject(
    'ftp://ftp.mars.org/pub/mpeg/libmad-0.15.1b.tar.gz',
    '1be543bc30c56fb6bea1d7bf6a64e66c',
    'lib/libmad.a',
    [
        '--disable-shared', '--enable-static',

        # without this, libmad's configure.ac ignores -O* and -f*
        '--disable-debugging',
    ],
    autogen=True,
)

liblame = AutotoolsProject(
    'http://downloads.sourceforge.net/project/lame/lame/3.100/lame-3.100.tar.gz',
    'ddfe36cab873794038ae2c1210557ad34857a4b6bdc515785d1da9e175b1da1e',
    'lib/libmp3lame.a',
    [
        '--disable-shared', '--enable-static',
        '--disable-gtktest', '--disable-analyzer-hooks',
        '--disable-decoder', '--disable-frontend',
    ],
)

libmodplug = AutotoolsProject(
    'https://downloads.sourceforge.net/modplug-xmms/libmodplug/0.8.9.0/libmodplug-0.8.9.0.tar.gz',
    '457ca5a6c179656d66c01505c0d95fafaead4329b9dbaa0f997d00a3508ad9de',
    'lib/libmodplug.a',
    [
        '--disable-shared', '--enable-static',
    ],
    patches='src/lib/modplug/patches',
)

libopenmpt = AutotoolsProject(
    'https://lib.openmpt.org/files/libopenmpt/src/libopenmpt-0.7.9+release.autotools.tar.gz',
    '0386e918d75d797e79d5b14edd0847165d8b359e9811ef57652c0a356a2dfcf4',
    'lib/libopenmpt.a',
    [
        '--disable-shared', '--enable-static',
        '--disable-openmpt123',
        '--disable-examples',
        '--disable-tests',
        '--disable-doxygen-doc',
        '--without-mpg123', '--without-ogg', '--without-vorbis', '--without-vorbisfile',
        '--without-portaudio', '--without-portaudiocpp', '--without-sndfile',
        '--without-flac',
    ],
    base='libopenmpt-0.7.9+release.autotools',
)

wildmidi = CmakeProject(
    'https://github.com/Mindwerks/wildmidi/releases/download/wildmidi-0.4.6/wildmidi-0.4.6.tar.gz',
    '24ca992639ce76efa3737029fceb3672385d56e2ac0a15d50b40cc12d26e60de',
    'lib/libWildMidi.a',
    [
        '-DBUILD_SHARED_LIBS=OFF',
        '-DWANT_PLAYER=OFF',
        '-DWANT_STATIC=ON',
    ],
)

gme = CmakeProject(
    'https://bitbucket.org/mpyne/game-music-emu/downloads/game-music-emu-0.6.3.tar.xz',
    'aba34e53ef0ec6a34b58b84e28bf8cfbccee6585cebca25333604c35db3e051d',
    'lib/libgme.a',
    [
        '-DBUILD_SHARED_LIBS=OFF',
        '-DENABLE_UBSAN=OFF',
        '-DZLIB_INCLUDE_DIR=OFF',
        '-DCMAKE_DISABLE_FIND_PACKAGE_SDL2=ON',
    ],
)

ffmpeg = FfmpegProject(
    'http://ffmpeg.org/releases/ffmpeg-7.1.tar.xz',
    '40973d44970dbc83ef302b0609f2e74982be2d85916dd2ee7472d30678a7abe6',
    'lib/libavcodec.a',
    [
        '--disable-shared', '--enable-static',
        '--enable-gpl',
        '--enable-small',
        '--disable-pthreads',
        '--disable-programs',
        '--disable-doc',
        '--disable-avdevice',
        '--disable-swresample',
        '--disable-swscale',
        '--disable-postproc',
        '--disable-avfilter',
        '--disable-faan',
        '--disable-pixelutils',
        '--disable-network',
        '--disable-encoders',
        '--disable-hwaccels',
        '--disable-muxers',
        '--disable-protocols',
        '--disable-devices',
        '--disable-filters',
        '--disable-v4l2_m2m',

        '--disable-sdl2',
        '--disable-vulkan',
        '--disable-xlib',

        '--disable-parser=bmp',
        '--disable-parser=cavsvideo',
        '--disable-parser=dvbsub',
        '--disable-parser=dvdsub',
        '--disable-parser=dvd_nav',
        '--disable-parser=flac',
        '--disable-parser=g729',
        '--disable-parser=gsm',
        '--disable-parser=h261',
        '--disable-parser=h263',
        '--disable-parser=h264',
        '--disable-parser=hevc',
        '--disable-parser=jpeg2000',
        '--disable-parser=mjpeg',
        '--disable-parser=mlp',
        '--disable-parser=mpeg4video',
        '--disable-parser=mpegvideo',
        '--disable-parser=opus',
        '--disable-parser=qoi',
        '--disable-parser=rv30',
        '--disable-parser=rv40',
        '--disable-parser=vc1',
        '--disable-parser=vp3',
        '--disable-parser=vp8',
        '--disable-parser=vp9',
        '--disable-parser=png',
        '--disable-parser=pnm',
        '--disable-parser=webp',
        '--disable-parser=xma',

        '--disable-demuxer=aqtitle',
        '--disable-demuxer=ass',
        '--disable-demuxer=bethsoftvid',
        '--disable-demuxer=bink',
        '--disable-demuxer=cavsvideo',
        '--disable-demuxer=cdxl',
        '--disable-demuxer=dvbsub',
        '--disable-demuxer=dvbtxt',
        '--disable-demuxer=h261',
        '--disable-demuxer=h263',
        '--disable-demuxer=h264',
        '--disable-demuxer=ico',
        '--disable-demuxer=image2',
        '--disable-demuxer=image2pipe',
        '--disable-demuxer=image_bmp_pipe',
        '--disable-demuxer=image_cri_pipe',
        '--disable-demuxer=image_dds_pipe',
        '--disable-demuxer=image_dpx_pipe',
        '--disable-demuxer=image_exr_pipe',
        '--disable-demuxer=image_gem_pipe',
        '--disable-demuxer=image_gif_pipe',
        '--disable-demuxer=image_j2k_pipe',
        '--disable-demuxer=image_jpeg_pipe',
        '--disable-demuxer=image_jpegls_pipe',
        '--disable-demuxer=image_jpegxl_pipe',
        '--disable-demuxer=image_pam_pipe',
        '--disable-demuxer=image_pbm_pipe',
        '--disable-demuxer=image_pcx_pipe',
        '--disable-demuxer=image_pfm_pipe',
        '--disable-demuxer=image_pgm_pipe',
        '--disable-demuxer=image_pgmyuv_pipe',
        '--disable-demuxer=image_pgx_pipe',
        '--disable-demuxer=image_phm_pipe',
        '--disable-demuxer=image_photocd_pipe',
        '--disable-demuxer=image_pictor_pipe',
        '--disable-demuxer=image_png_pipe',
        '--disable-demuxer=image_ppm_pipe',
        '--disable-demuxer=image_psd_pipe',
        '--disable-demuxer=image_qdraw_pipe',
        '--disable-demuxer=image_qoi_pipe',
        '--disable-demuxer=image_sgi_pipe',
        '--disable-demuxer=image_sunrast_pipe',
        '--disable-demuxer=image_svg_pipe',
        '--disable-demuxer=image_tiff_pipe',
        '--disable-demuxer=image_vbn_pipe',
        '--disable-demuxer=image_webp_pipe',
        '--disable-demuxer=image_xbm_pipe',
        '--disable-demuxer=image_xpm_pipe',
        '--disable-demuxer=image_xwd_pipe',
        '--disable-demuxer=jacosub',
        '--disable-demuxer=lrc',
        '--disable-demuxer=microdvd',
        '--disable-demuxer=mjpeg',
        '--disable-demuxer=mjpeg_2000',
        '--disable-demuxer=mpegps',
        '--disable-demuxer=mpegvideo',
        '--disable-demuxer=mpl2',
        '--disable-demuxer=mpsub',
        '--disable-demuxer=pjs',
        '--disable-demuxer=rawvideo',
        '--disable-demuxer=realtext',
        '--disable-demuxer=sami',
        '--disable-demuxer=scc',
        '--disable-demuxer=srt',
        '--disable-demuxer=stl',
        '--disable-demuxer=subviewer',
        '--disable-demuxer=subviewer1',
        '--disable-demuxer=swf',
        '--disable-demuxer=tedcaptions',
        '--disable-demuxer=vobsub',
        '--disable-demuxer=vplayer',
        '--disable-demuxer=webm_dash_manifest',
        '--disable-demuxer=webvtt',
        '--disable-demuxer=yuv4mpegpipe',

        # we don't need these decoders, because we have the dedicated
        # libraries
        '--disable-decoder=flac',
        '--disable-decoder=opus',
        '--disable-decoder=vorbis',

        # audio codecs nobody uses
        '--disable-decoder=atrac1',
        '--disable-decoder=atrac3',
        '--disable-decoder=atrac3al',
        '--disable-decoder=atrac3p',
        '--disable-decoder=atrac3pal',
        '--disable-decoder=binkaudio_dct',
        '--disable-decoder=binkaudio_rdft',
        '--disable-decoder=bmv_audio',
        '--disable-decoder=dsicinaudio',
        '--disable-decoder=dvaudio',
        '--disable-decoder=metasound',
        '--disable-decoder=paf_audio',
        '--disable-decoder=ra_144',
        '--disable-decoder=ra_288',
        '--disable-decoder=ralf',
        '--disable-decoder=qdm2',
        '--disable-decoder=qdmc',

        # disable lots of image and video codecs
        '--disable-decoder=acelp_kelvin',
        '--disable-decoder=agm',
        '--disable-decoder=aic',
        '--disable-decoder=alias_pix',
        '--disable-decoder=ansi',
        '--disable-decoder=apng',
        '--disable-decoder=arbc',
        '--disable-decoder=argo',
        '--disable-decoder=ass',
        '--disable-decoder=asv1',
        '--disable-decoder=asv2',
        '--disable-decoder=aura',
        '--disable-decoder=aura2',
        '--disable-decoder=avrn',
        '--disable-decoder=avrp',
        '--disable-decoder=avui',
        '--disable-decoder=ayuv',
        '--disable-decoder=bethsoftvid',
        '--disable-decoder=bfi',
        '--disable-decoder=bink',
        '--disable-decoder=bintext',
        '--disable-decoder=bitpacked',
        '--disable-decoder=bmp',
        '--disable-decoder=bmv_video',
        '--disable-decoder=brender_pix',
        '--disable-decoder=c93',
        '--disable-decoder=cavs',
        '--disable-decoder=ccaption',
        '--disable-decoder=cdgraphics',
        '--disable-decoder=cdtoons',
        '--disable-decoder=cdxl',
        '--disable-decoder=cfhd',
        '--disable-decoder=cinepak',
        '--disable-decoder=clearvideo',
        '--disable-decoder=cljr',
        '--disable-decoder=cllc',
        '--disable-decoder=cpia',
        '--disable-decoder=cscd',
        '--disable-decoder=cyuv',
        '--disable-decoder=dds',
        '--disable-decoder=dirac',
        '--disable-decoder=dnxhd',
        '--disable-decoder=dpx',
        '--disable-decoder=dsicinvideo',
        '--disable-decoder=dvbsub',
        '--disable-decoder=dvdsub',
        '--disable-decoder=dvvideo',
        '--disable-decoder=dxa',
        '--disable-decoder=dxtory',
        '--disable-decoder=dxv',
        '--disable-decoder=eacmv',
        '--disable-decoder=eamad',
        '--disable-decoder=eatgq',
        '--disable-decoder=eatgv',
        '--disable-decoder=eatqi',
        '--disable-decoder=eightbps',
        '--disable-decoder=escape124',
        '--disable-decoder=escape130',
        '--disable-decoder=exr',
        '--disable-decoder=ffv1',
        '--disable-decoder=ffvhuff',
        '--disable-decoder=ffwavesynth',
        '--disable-decoder=fic',
        '--disable-decoder=fits',
        '--disable-decoder=flashsv',
        '--disable-decoder=flashsv2',
        '--disable-decoder=flic',
        '--disable-decoder=flv',
        '--disable-decoder=fmvc',
        '--disable-decoder=fraps',
        '--disable-decoder=fourxm',
        '--disable-decoder=frwu',
        '--disable-decoder=g2m',
        '--disable-decoder=gdv',
        '--disable-decoder=gem',
        '--disable-decoder=gif',
        '--disable-decoder=h261',
        '--disable-decoder=h263',
        '--disable-decoder=h263i',
        '--disable-decoder=h263p',
        '--disable-decoder=h264',
        '--disable-decoder=hap',
        '--disable-decoder=hevc',
        '--disable-decoder=hnm4_video',
        '--disable-decoder=hq_hqa',
        '--disable-decoder=hqx',
        '--disable-decoder=huffyuv',
        '--disable-decoder=hymt',
        '--disable-decoder=idcin',
        '--disable-decoder=idf',
        '--disable-decoder=iff_ilbm',
        '--disable-decoder=imm4',
        '--disable-decoder=indeo2',
        '--disable-decoder=indeo3',
        '--disable-decoder=indeo4',
        '--disable-decoder=indeo5',
        '--disable-decoder=interplay_video',
        '--disable-decoder=ipu',
        '--disable-decoder=jacosub',
        '--disable-decoder=jpeg2000',
        '--disable-decoder=jpegls',
        '--disable-decoder=jv',
        '--disable-decoder=kgv1',
        '--disable-decoder=kmvc',
        '--disable-decoder=lagarith',
        '--disable-decoder=lead',
        '--disable-decoder=loco',
        '--disable-decoder=lscr',
        '--disable-decoder=m101',
        '--disable-decoder=magicyuv',
        '--disable-decoder=mdec',
        '--disable-decoder=microdvd',
        '--disable-decoder=mimic',
        '--disable-decoder=mjpeg',
        '--disable-decoder=mmvideo',
        '--disable-decoder=mpl2',
        '--disable-decoder=mobiclip',
        '--disable-decoder=motionpixels',
        '--disable-decoder=movtext',
        '--disable-decoder=mpeg1video',
        '--disable-decoder=mpeg2video',
        '--disable-decoder=mpeg4',
        '--disable-decoder=mpegvideo',
        '--disable-decoder=msa1',
        '--disable-decoder=mscc',
        '--disable-decoder=msmpeg4_crystalhd',
        '--disable-decoder=msmpeg4v1',
        '--disable-decoder=msmpeg4v2',
        '--disable-decoder=msmpeg4v3',
        '--disable-decoder=msp2',
        '--disable-decoder=msrle',
        '--disable-decoder=mss1',
        '--disable-decoder=msvideo1',
        '--disable-decoder=mszh',
        '--disable-decoder=mts2',
        '--disable-decoder=mv30',
        '--disable-decoder=mvc1',
        '--disable-decoder=mvc2',
        '--disable-decoder=mvdv',
        '--disable-decoder=mvha',
        '--disable-decoder=mwsc',
        '--disable-decoder=notchlc',
        '--disable-decoder=nuv',
        '--disable-decoder=on2avc',
        '--disable-decoder=paf_video',
        '--disable-decoder=pam',
        '--disable-decoder=pbm',
        '--disable-decoder=pcx',
        '--disable-decoder=pdv',
        '--disable-decoder=pfm',
        '--disable-decoder=pgm',
        '--disable-decoder=pgmyuv',
        '--disable-decoder=pgssub',
        '--disable-decoder=pgx',
        '--disable-decoder=phm',
        '--disable-decoder=photocd',
        '--disable-decoder=png',
        '--disable-decoder=pictor',
        '--disable-decoder=pixlet',
        '--disable-decoder=pjs',
        '--disable-decoder=ppm',
        '--disable-decoder=prores',
        '--disable-decoder=prosumer',
        '--disable-decoder=psd',
        '--disable-decoder=ptx',
        '--disable-decoder=qdraw',
        '--disable-decoder=qoi',
        '--disable-decoder=qpeg',
        '--disable-decoder=qtrle',
        '--disable-decoder=rawvideo',
        '--disable-decoder=r10k',
        '--disable-decoder=r210',
        '--disable-decoder=rasc',
        '--disable-decoder=realtext',
        '--disable-decoder=rl2',
        '--disable-decoder=rpza',
        '--disable-decoder=roq',
        '--disable-decoder=roq_dpcm',
        '--disable-decoder=rscc',
        '--disable-decoder=rv10',
        '--disable-decoder=rv20',
        '--disable-decoder=rv30',
        '--disable-decoder=rv40',
        '--disable-decoder=sami',
        '--disable-decoder=sanm',
        '--disable-decoder=scpr',
        '--disable-decoder=screenpresso',
        '--disable-decoder=sga',
        '--disable-decoder=sgi',
        '--disable-decoder=sgirle',
        '--disable-decoder=sheervideo',
        '--disable-decoder=simbiosis_imx',
        '--disable-decoder=smc',
        '--disable-decoder=snow',
        '--disable-decoder=speedhq',
        '--disable-decoder=srgc',
        '--disable-decoder=srt',
        '--disable-decoder=ssa',
        '--disable-decoder=stl',
        '--disable-decoder=subrip',
        '--disable-decoder=subviewer',
        '--disable-decoder=subviewer1',
        '--disable-decoder=sunrast',
        '--disable-decoder=svq1',
        '--disable-decoder=svq3',
        '--disable-decoder=targa',
        '--disable-decoder=targa_y216',
        '--disable-decoder=text',
        '--disable-decoder=tiff',
        '--disable-decoder=tiertexseqvideo',
        '--disable-decoder=tmv',
        '--disable-decoder=truemotion1',
        '--disable-decoder=truemotion2',
        '--disable-decoder=truemotion2rt',
        '--disable-decoder=tscc',
        '--disable-decoder=tscc2',
        '--disable-decoder=twinvq',
        '--disable-decoder=txd',
        '--disable-decoder=ulti',
        '--disable-decoder=utvideo',
        '--disable-decoder=v210',
        '--disable-decoder=v210x',
        '--disable-decoder=v308',
        '--disable-decoder=v408',
        '--disable-decoder=v410',
        '--disable-decoder=vb',
        '--disable-decoder=vble',
        '--disable-decoder=vbn',
        '--disable-decoder=vc1',
        '--disable-decoder=vcr1',
        '--disable-decoder=vmdvideo',
        '--disable-decoder=vmnc',
        '--disable-decoder=vp3',
        '--disable-decoder=vp5',
        '--disable-decoder=vp6',
        '--disable-decoder=vp7',
        '--disable-decoder=vp8',
        '--disable-decoder=vp9',
        '--disable-decoder=vplayer',
        '--disable-decoder=vqa',
        '--disable-decoder=webvtt',
        '--disable-decoder=wcmv',
        '--disable-decoder=wmv1',
        '--disable-decoder=wmv2',
        '--disable-decoder=wmv3',
        '--disable-decoder=wnv1',
        '--disable-decoder=wrapped_avframe',
        '--disable-decoder=xan_wc3',
        '--disable-decoder=xan_wc4',
        '--disable-decoder=xbin',
        '--disable-decoder=xbm',
        '--disable-decoder=xface',
        '--disable-decoder=xl',
        '--disable-decoder=xpm',
        '--disable-decoder=xsub',
        '--disable-decoder=xwd',
        '--disable-decoder=y41p',
        '--disable-decoder=ylc',
        '--disable-decoder=yop',
        '--disable-decoder=yuv4',
        '--disable-decoder=zero12v',
        '--disable-decoder=zerocodec',
        '--disable-decoder=zlib',
        '--disable-decoder=zmbv',

        '--disable-bsf=av1_frame_merge',
        '--disable-bsf=av1_frame_split',
        '--disable-bsf=av1_metadata',
        '--disable-bsf=dts2pts',
        '--disable-bsf=h264_metadata',
        '--disable-bsf=h264_mp4toannexb',
        '--disable-bsf=h264_redundant_pps',
        '--disable-bsf=hevc_metadata',
        '--disable-bsf=hevc_mp4toannexb',
        '--disable-bsf=mjpeg2jpeg',
        '--disable-bsf=opus_metadata',
        '--disable-bsf=pgs_frame_merge',
        '--disable-bsf=text2movsub',
        '--disable-bsf=vp9_metadata',
        '--disable-bsf=vp9_raw_reorder',
        '--disable-bsf=vp9_superframe',
        '--disable-bsf=vp9_superframe_split',
    ],
)

openssl = OpenSSLProject(
    ('https://www.openssl.org/source/openssl-3.1.4.tar.gz',
     'https://artfiles.org/openssl.org/source/openssl-3.1.4.tar.gz'),
    '840af5366ab9b522bde525826be3ef0fb0af81c6a9ebd84caa600fea1731eee3',
    'include/openssl/ossl_typ.h',
)

libnfs = AutotoolsProject(
    'https://github.com/sahlberg/libnfs/archive/libnfs-5.0.3.tar.gz',
    'd945cb4f4c8f82ee1f3640893a168810f794a28e1010bb007ec5add345e9df3e',
    'lib/libnfs.a',
    [
        '--disable-shared', '--enable-static',
        '--disable-debug',

        # work around -Wtautological-compare
        '--disable-werror',

        '--disable-utils', '--disable-examples',
    ],
    base='libnfs-libnfs-5.0.3',
    autoreconf=True,
)

jack = JackProject(
    'https://github.com/jackaudio/jack2/archive/v1.9.17.tar.gz',
    '38f674bbc57852a8eb3d9faa1f96a0912d26f7d5df14c11005ad499c8ae352f2',
    'lib/pkgconfig/jack.pc',
)

boost = BoostProject(
    'https://boostorg.jfrog.io/artifactory/main/release/1.81.0/source/boost_1_81_0.tar.bz2',
    '71feeed900fbccca04a3b4f2f84a7c217186f28a940ed8b7ed4725986baf99fa',
    'include/boost/version.hpp',
)
