# $OpenBSD: Makefile,v 1.21 2017/11/21 00:13:04 naddy Exp $

COMMENT=	GTK-based BDF font editor

DISTNAME=	gbdfed-1.6
REVISION=	5

CATEGORIES=	x11 fonts

# BSD
PERMIT_PACKAGE_CDROM=	Yes

WANTLIB =  X11 Xau Xcomposite Xcursor Xdamage Xdmcp Xext Xfixes Xi
WANTLIB += Xinerama Xrandr Xrender atk-1.0 c cairo expat fontconfig
WANTLIB += freetype gdk-x11-2.0 gdk_pixbuf-2.0 gio-2.0 glib-2.0
WANTLIB += gmodule-2.0 gobject-2.0 gthread-2.0 gtk-x11-2.0 iconv intl m
WANTLIB += pango-1.0 pangocairo-1.0 pangoft2-1.0 pixman-1 png pthread
WANTLIB += xcb xcb-render xcb-render-util z

MASTER_SITES=	https://www.distfiles.pl/
EXTRACT_SUFX=	.tbz2

LIB_DEPENDS=	x11/gtk+2

CONFIGURE_STYLE=gnu
# leakage from bsd.own.mk
MAKE_ENV=	STATIC=""

NO_TEST=	Yes

do-install:
	${INSTALL_PROGRAM} ${WRKBUILD}/gbdfed ${PREFIX}/bin
	${INSTALL_DATA} ${WRKSRC}/gbdfed.man ${PREFIX}/man/man1/gbdfed.1

.include <bsd.port.mk>
