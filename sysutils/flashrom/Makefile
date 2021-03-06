# $OpenBSD: Makefile,v 1.7 2018/01/16 22:16:41 sthen Exp $

ONLY_FOR_ARCHS=	i386 amd64

COMMENT=	flash ROM programmer for BIOS etc

DISTNAME=	flashrom-1.0
EXTRACT_SUFX=	.tar.bz2

CATEGORIES=	sysutils

HOMEPAGE=	https://www.flashrom.org/

MAINTAINER=	Stuart Henderson <sthen@openbsd.org>

# GPLv2
PERMIT_PACKAGE_CDROM=	Yes

WANTLIB=	c ftdi usb-1.0 usb z

MASTER_SITES=	https://download.flashrom.org/releases/

# pciutils' libpci.a is linked statically; a patched version is required.
BUILD_DEPENDS=	sysutils/pciutils:patch
RUN_DEPENDS=	sysutils/dmidecode
LIB_DEPENDS=	devel/libusb-compat \
		devel/libftdi
MAKE_FLAGS=	LDFLAGS="-L./pciutils/lib" WARNERROR=no
FAKE_FLAGS=	PREFIX="${TRUEPREFIX}" MANDIR="${TRUEPREFIX}/man"

PATCHORIG=	.orig.port
USE_GMAKE=	Yes
NO_TEST=	Yes

pre-patch:
	mv ${WRKDIR}/sysutils/pciutils/pciutils-* ${WRKSRC}/pciutils

do-configure:
	cd ${WRKSRC}/pciutils; ${MAKE_PROGRAM} CC="${CC}" OPT="${CFLAGS}"

.include <bsd.port.mk>
