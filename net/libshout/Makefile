# $OpenBSD: Makefile,v 1.26 2016/03/11 19:59:15 naddy Exp $

COMMENT=	library for communicating with an icecast server

DISTNAME=	libshout-2.3.1
SHARED_LIBS=	shout	5.1
CATEGORIES=	net audio

HOMEPAGE=	http://www.icecast.org/

# LGPL
PERMIT_PACKAGE_CDROM=	Yes

WANTLIB += m ogg pthread speex theora>=1 vorbis>=4

MASTER_SITES=	http://downloads.xiph.org/releases/libshout/

LIB_DEPENDS=	audio/libvorbis \
		audio/speex \
		multimedia/libtheora

# LIB_DEPENDS don't propagate if !shared
LIB_DEPENDS +=	audio/libogg

FAKE_FLAGS=	docdir='${PREFIX}/share/examples/libshout'

CONFIGURE_STYLE= gnu

SEPARATE_BUILD=	Yes

.include <bsd.port.mk>
