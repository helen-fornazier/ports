# $OpenBSD: Makefile,v 1.20 2017/12/26 17:08:02 jca Exp $

COMMENT=	Small Device C Compiler
BROKEN-sparc64=	illegal operands building SDCCval.c
BROKEN-alpha=	sdcc segfaults when building the device library
BROKEN-aarch64=	*** BFD does not support target aarch64-unknown-openbsd6.2.

DISTNAME=	sdcc-src-3.6.0
PKGNAME=	${DISTNAME:S/-src//}
REVISION =	2
EXTRACT_SUFX=	.tar.bz2
CATEGORIES=	devel

HOMEPAGE=	http://sdcc.sourceforge.net/
MAINTAINER=	Brian Callahan <bcallah@openbsd.org>

# GPL
PERMIT_PACKAGE_CDROM=	Yes
WANTLIB=		c m ${COMPILER_LIBCXX} readline termcap z

MASTER_SITES=		${MASTER_SITE_SOURCEFORGE:=sdcc/}

BUILD_DEPENDS=		${RUN_DEPENDS} \
			devel/boost
RUN_DEPENDS=		devel/gputils

CONFIGURE_STYLE=	gnu
CONFIGURE_ARGS+=	docdir=${PREFIX}/share/doc/sdcc
CONFIGURE_ENV+=		sdcc_cv_CCggdb=no \
                        sdcc_cv_c_fms_extensions=no \
			CPPFLAGS="${CPPFLAGS} -I${LOCALBASE}/include" \
			LDFLAGS="${LDFLAGS} -L${LOCALBASE}/lib"

USE_GMAKE=		Yes

WRKDIST=		${WRKDIR}/${PKGNAME}

.include <bsd.port.mk>
