# $OpenBSD: Makefile,v 1.4 2017/12/26 13:57:47 abieber Exp $

COMMENT =	pass compatible password manager wirtten in go

GH_ACCOUNT =	justwatchcom
GH_PROJECT =	gopass
GH_TAGNAME =	v1.6.6

CATEGORIES =	security

MAINTAINER =	Aaron Bieber <abieber@openbsd.org>

# MIT
PERMIT_PACKAGE_CDROM =	Yes

RUN_DEPENDS =	devel/git \
		security/gnupg2

# uses pledge()
WANTLIB += c pthread

MODULES =	lang/go
MODGO_TYPE =	bin
MODGO_LDFLAGS =	-X "main.version=${GH_TAGNAME:S/v//}"

# Tests require MODGO_ENV, but break in weird ways when it is set.
NO_TEST =	Yes

.include <bsd.port.mk>
