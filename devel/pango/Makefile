# $OpenBSD: Makefile,v 1.115 2017/11/18 10:00:13 ajacoutot Exp $

COMMENT=		library for layout and rendering of text

GNOME_VERSION=		1.40.14
GNOME_PROJECT=		pango

SHARED_LIBS +=  pango-1.0            3800.1   # 4000.14
SHARED_LIBS +=  pangoft2-1.0         3800.1   # 4000.14
SHARED_LIBS +=  pangoxft-1.0         3800.1   # 4000.14
SHARED_LIBS +=  pangocairo-1.0       3800.1   # 4000.14

CATEGORIES=		devel x11

HOMEPAGE=		http://www.pango.org/

MAINTAINER=		Antoine Jacoutot <ajacoutot@openbsd.org>

# LGPLv2
PERMIT_PACKAGE_CDROM=	Yes

WANTLIB += X11 Xext Xft Xrender c cairo expat ffi fontconfig freetype
WANTLIB += glib-2.0 gobject-2.0 graphite2 gthread-2.0 harfbuzz
WANTLIB += iconv intl m pcre pixman-1 png pthread
WANTLIB += xcb xcb-render xcb-shm z

MODULES=		x11/gnome

MODGNOME_TOOLS=		gobject-introspection

LIB_DEPENDS=		devel/glib2 \
			devel/harfbuzz

AUTOCONF_VERSION=	2.69
CONFIGURE_STYLE=	autoconf

.include <bsd.port.mk>
