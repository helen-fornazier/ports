# $OpenBSD: Makefile,v 1.76 2017/02/25 16:04:20 danj Exp $

COMMENT =	Google daemon for use with Google Cloud Compute Engine

MODPY_EGG_VERSION = 2.4.0
DISTNAME =	google-compute-engine-${MODPY_EGG_VERSION}

GH_ACCOUNT =	GoogleCloudPlatform
GH_PROJECT =	compute-image-packages
GH_TAGNAME =	20170609

CATEGORIES =	sysutils

MAINTAINER =	Helen Koike <helen.koike@collabora.com>

# Apache 2.0
PERMIT_PACKAGE_CDROM =	Yes

MODULES =		lang/python

MODPY_SETUPTOOLS =	Yes

RUN_DEPENDS =	net/py-boto \
		net/py-netifaces \
		net/py-netaddr

pre-configure:
	cd ${WRKSRC}/google_compute_engine && ${SUBST_CMD} \
		config_manager.py instance_setup/instance_{config,setup}.py

.include <bsd.port.mk>
