# $OpenBSD: Makefile,v 1.43 2017/12/25 01:17:58 gonzalo Exp $

COMMENT =		complete front-end for MPlayer

DISTNAME =		smplayer-17.12.0

CATEGORIES =		multimedia x11

HOMEPAGE =		http://smplayer.sourceforge.net/

MAINTAINER =		Gonzalo L. R. <gonzalo@openbsd.org>

# GPLv2 (docs/en/gpl.html)
PERMIT_PACKAGE_CDROM =	Yes

WANTLIB += ${COMPILER_LIBCXX}
WANTLIB += GL Qt5Core Qt5DBus Qt5Gui Qt5Network Qt5Script Qt5Widgets
WANTLIB += Qt5Xml X11 Xext c m pthread z

MASTER_SITES =		${MASTER_SITE_SOURCEFORGE:=smplayer/}

EXTRACT_SUFX =		.tar.bz2

MODULES =		x11/qt5
RUN_DEPENDS =		x11/mplayer>=20090708 \
			devel/desktop-file-utils \
			x11/gtk+3,-guic

LIB_DEPENDS =		x11/qt5/qtscript

USE_GMAKE =		Yes

NO_TEST =		Yes

ALL_TARGET =		src/smplayer

MAKE_FLAGS =		QMAKE=${MODQT_QMAKE} \
			LRELEASE=${MODQT_LRELEASE}

.include <bsd.port.mk>
