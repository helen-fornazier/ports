# $OpenBSD: Makefile,v 1.30 2017/01/03 19:19:49 landry Exp $

COMMENT=	simplified packaging system for Python modules

MODPY_EGG_VERSION=	28.6.1
DISTNAME=		setuptools-${MODPY_EGG_VERSION}
PKGNAME=		py-${DISTNAME:S/c/./}
EPOCH = 		0
CATEGORIES=		devel
PKG_ARCH=		*
REVISION=		0


HOMEPAGE=		https://setuptools.readthedocs.io/en/latest/

# MIT
PERMIT_PACKAGE_CDROM=	Yes

MODULES=		lang/python

MODPY_PI =	Yes
MODPY_SETUPTOOLS=	Yes

FLAVORS =		python3
FLAVOR ?=

# Override automatic py-setuptools depend to avoid recursion
MODPY_SETUPUTILS_DEPEND=

NO_TEST =		Yes

.include <bsd.port.mk>
