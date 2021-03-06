# $OpenBSD: Makefile,v 1.28 2017/12/24 14:54:58 ajacoutot Exp $

COMMENT=		GObject wrapper around exiv2

GNOME_VERSION=		0.10.7
GNOME_PROJECT=		gexiv2
PKGNAME=		lib${DISTNAME}

CATEGORIES=		graphics

SHARED_LIBS +=  gexiv2               3.0      # 2.0

MAINTAINER=		Jasper Lievisse Adriaanse <jasper@openbsd.org>, \
			Antoine Jacoutot <ajacoutot@openbsd.org>

# GPLv2
PERMIT_PACKAGE_CDROM=	Yes

WANTLIB += ${COMPILER_LIBCXX} exiv2 expat ffi glib-2.0 gobject-2.0
WANTLIB += iconv intl m pcre z

MODULES=		lang/python \
			x11/gnome

MODGNOME_TOOLS=		gobject-introspection vala
MODPY_VERSION=		${MODPY_DEFAULT_VERSION_3}

# C++11
COMPILER =		base-clang ports-gcc
CXXFLAGS +=		-std=c++11

LIB_DEPENDS=		devel/glib2 \
			graphics/exiv2

# import gi
BUILD_DEPENDS=		devel/py-gobject3${MODPY_FLAVOR}
RUN_DEPENDS=		devel/py-gobject3${MODPY_FLAVOR}

CONFIGURE_STYLE=	gnu
CONFIGURE_ENV=		ac_cv_path_PYTHON3_PATH=${MODPY_BIN}

.include <bsd.port.mk>
