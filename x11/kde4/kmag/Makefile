# $OpenBSD: Makefile,v 1.7 2017/07/27 11:57:49 sthen Exp $

COMMENT =	KDE screen magnifier
DISTNAME =	kmag-${MODKDE4_VERSION}
REVISION =	2

WANTLIB =  c m pthread
WANTLIB += ${COMPILER_LIBCXX}
WANTLIB += lib/qt4/QtDBus lib/qt4/QtGui lib/qt4/QtNetwork lib/qt4/QtSvg
WANTLIB += lib/qt4/QtXml
WANTLIB += ${KDE4LIB}/kdeui ${KDE4LIB}/kio
WANTLIB += qaccessibilityclient

LIB_DEPENDS =	x11/libqaccessibilityclient

RUN_DEPENDS =	devel/desktop-file-utils \
		x11/gtk+3,-guic

.include <bsd.port.mk>
