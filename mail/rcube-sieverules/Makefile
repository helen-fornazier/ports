# $OpenBSD: Makefile,v 1.14 2015/06/05 06:00:21 robert Exp $

COMMENT=	roundcube plugin: sieve rules (managesieve)

GH_ACCOUNT=	JohnDoh
GH_PROJECT=	Roundcube-Plugin-SieveRules-Managesieve
GH_TAGNAME=	2.3
DISTNAME=	sieverules-${GH_TAGNAME}
PKGNAME=	rcube-${DISTNAME}
CATEGORIES=	mail www
HOMEPAGE=	http://www.tehinterweb.co.uk/roundcube/\#pisieverules
REVISION=	0

MAINTAINER=	Stuart Henderson <sthen@openbsd.org>

# GPLv3+
PERMIT_PACKAGE_CDROM=	Yes

NO_BUILD=	Yes
NO_TEST=	Yes
PKG_ARCH=	*

PREFIX=		${VARBASE}/www
INSTDIR=	${PREFIX}/roundcubemail/plugins
TINSTDIR=	${TRUEPREFIX}/roundcubemail/plugins
SUBST_VARS=	INSTDIR TINSTDIR

MODULES=	lang/php
RUN_DEPENDS=	mail/roundcubemail>=1.1

do-install:
	${INSTALL_DATA_DIR} ${INSTDIR}/sieverules
	cp -Rp ${WRKDIST}/* ${INSTDIR}/sieverules
	chown -R ${SHAREOWN}:${SHAREGRP} ${INSTDIR}
	find ${INSTDIR} \( -name \*.orig -or -name \*.src \) -exec rm -f {} \;

.include <bsd.port.mk>
