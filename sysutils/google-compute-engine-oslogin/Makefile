# $OpenBSD: Makefile.template,v 1.76 2017/02/25 16:04:20 danj Exp $

COMMENT =		OS Login Guest Environment for Google Compute Engine

DISTNAME =		google-compute-engine-oslogin-1.1.2

GH_ACCOUNT =		GoogleCloudPlatform
GH_PROJECT =		compute-image-packages
GH_TAGNAME =		20171213

CATEGORIES =		sysutils

MAINTAINER =		Helen Koike <helen.koike@collabora.com>

# Apache 2.0
PERMIT_PACKAGE_CDROM =	Yes


# "make port-lib-depends-check" can help
WANTLIB +=		curl

DIST_SUBDIR =		google_compute_engine_oslogin

# Dependencies
#
#MODULES =		???
#BUILD_DEPENDS =	???
#RUN_DEPENDS =		???
#LIB_DEPENDS =		???
#TEST_DEPENDS =		???

MAKE_FLAGS =	JSON_INCLUDE_PATH=${LOCALBASE}/include/json-c \
		BIN_INSTALL_PATH=/bin \
		PAM_INSTALL_PATH=/lib \
		AUTHKEYS_INSTALL_PATH=/bin \
		NSS_LIBRARY_SONAME=nss_oslogin.so.1
COMPILER = base-clang

#MAKE_ENV =		???
#FAKE_FLAGS =		???
#TEST_FLAGS =		???

SEPARATE_BUILD =	Yes
USE_GMAKE =		Yes

# Overrides for default values
#
#CFLAGS =		???
#LDFLAGS =		???
#PKG_ARCH =		??? (* for arch-independent packages)
WRKBUILD =		${WRKSRC}/google_compute_engine_oslogin



#ALL_TARGET =		???
#INSTALL_TARGET =	???
#TEST_TARGET =		???

.include <bsd.port.mk>
