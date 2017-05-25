# $OpenBSD: Makefile,v 1.76 2017/02/25 16:04:20 danj Exp $


COMMENT=	Google daemon for use with Google Cloud Compute Engine

DISTNAME =	google-compute-engine-2.3.6

GH_ACCOUNT=	GoogleCloudPlatform
GH_PROJECT=	compute-image-packages
GH_TAGNAME=	20170426

CATEGORIES =	net

HOMEPAGE=	https://github.com/GoogleCloudPlatform/compute-image-packages

MAINTAINER=	Helen Koike <helen.koike@collabora.com>

# Apache 2.0
PERMIT_PACKAGE_CDROM =Yes

MODULES=		lang/python

MODPY_PI=		Yes
MODPY_SETUPTOOLS=	Yes

# TODO fpm
BUILD_DEPENDS=	shells/bash
RUN_DEPENDS=	security/sudo \
		net/ntp \
		net/py-boto \
		net/py-netifaces \
		net/py-netaddr \

.include <bsd.port.mk>
