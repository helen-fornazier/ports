# $OpenBSD: Makefile,v 1.16 2018/01/11 19:27:07 rpe Exp $

COMMENT =	lightweight irc server

DISTNAME =	ngircd-24
REVISION =	0

CATEGORIES =	net

HOMEPAGE =	http://ngircd.barton.de/

MAINTAINER =	Giannis Tsaraias <tsg@openbsd.org>

# GPLv2
PERMIT_PACKAGE_CDROM =	Yes

WANTLIB =	c crypto iconv ssl z

MASTER_SITES =	http://ngircd.barton.de/pub/ngircd/ \
		http://ngircd.mirror.3rz.org/pub/ngircd/

LIB_DEPENDS =	converters/libiconv
TEST_DEPENDS =	lang/expect \
		${BASE_PKGPATH}

SYSCONFDIR =	${BASESYSCONFDIR}/ngircd

CONFIGURE_STYLE = gnu
CONFIGURE_ARGS += --with-iconv=${LOCALBASE} \
		  --with-openssl \
		  --enable-ipv6

.include <bsd.port.mk>
