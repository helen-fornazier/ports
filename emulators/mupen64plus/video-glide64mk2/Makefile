# $OpenBSD: Makefile,v 1.15 2017/11/16 23:20:38 naddy Exp $

COMMENT =		n64 emulator video plugin
REVISION =		4

# GPLv2+
PERMIT_PACKAGE_CDROM =	Yes

COMPILER =		base-clang ports-gcc

WANTLIB =		GL SDL2 boost_filesystem boost_system c m png pthread z ${COMPILER_LIBCXX}
LIB_DEPENDS =		devel/boost devel/sdl2 graphics/png

MUPEN64PLUS_MOD = 	video-glide64mk2

.include <bsd.port.mk>
