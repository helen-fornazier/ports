# $OpenBSD: Makefile,v 1.4 2017/06/02 10:51:56 schwarze Exp $

COMMENT=	small tools to operate on patch files

DISTNAME=	patchutils-0.3.4
REVISION=	0
EXTRACT_SUFX=	.tar.xz

CATEGORIES=	textproc devel

HOMEPAGE=	http://cyberelk.net/tim/software/patchutils/

MAINTAINER=	Stuart Henderson <sthen@openbsd.org>

# GPLv2+
PERMIT_PACKAGE_CDROM=	Yes

WANTLIB += c

MASTER_SITES=	http://cyberelk.net/tim/data/patchutils/stable/

BUILD_DEPENDS=	${RUN_DEPENDS} \
		textproc/xmlto
RUN_DEPENDS=	devel/gpatch
TEST_DEPENDS=	misc/rpm \
		shells/bash
TEST_FLAGS=	PATCH=${LOCALBASE}/bin/gpatch

# only needed for tests
USE_GMAKE=	Yes

CONFIGURE_STYLE= gnu
CONFIGURE_ARGS+= --with-patch=${LOCALBASE}/bin/gpatch

pre-test:
	chmod +x ${WRKSRC}/scripts/*diff
	@sed -i "s|/bin/echo -ne '\\\t'|printf '\\\t'|" \
	    ${WRKSRC}/tests/flip*/run-test
	@sed -Ei 's,!/bin/(ba)?sh,!${LOCALBASE}/bin/bash,g' \
	    ${WRKSRC}/tests/*/run-test

.include <bsd.port.mk>
