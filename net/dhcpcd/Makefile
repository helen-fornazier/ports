# $OpenBSD: Makefile,v 1.29 2018/01/11 19:27:05 rpe Exp $

COMMENT=		DHCPv4/IPv4LL/IPv6RS/DHCPv6 quad stack client

DISTNAME=		dhcpcd-7.0.0
REVISION=		0

CATEGORIES=		net
EXTRACT_SUFX=		.tar.xz

HOMEPAGE=		https://roy.marples.name/projects/dhcpcd

# BSD-2
PERMIT_PACKAGE_CDROM=	Yes

WANTLIB += c

MAINTAINER=		Stuart Henderson <sthen@openbsd.org>

MASTER_SITES=		https://roy.marples.name/downloads/dhcpcd/ \
			ftp://roy.marples.name/pub/dhcpcd/

CONFIGURE_STYLE=	simple
CONFIGURE_ARGS=		--prefix='${PREFIX}' \
			--sysconfdir='${SYSCONFDIR}' \
			--mandir='${PREFIX}/man' \
			--localstatedir='${LOCALSTATEDIR}'
FAKE_FLAGS=		SYSCONFDIR=${PREFIX}/share/examples/dhcpcd

.include <bsd.port.mk>
