# $OpenBSD: Makefile,v 1.7 2017/11/10 19:13:34 kili Exp $

COMMENT =		monad morphisms

DISTNAME =		mmorph-1.0.9
REVISION =		0
CATEGORIES =		devel

MAINTAINER =		Matthias Kilian <kili@openbsd.org>

# BSD3
PERMIT_PACKAGE_CDROM =	Yes

MODULES =		lang/ghc

MODGHC_BUILD =		cabal hackage haddock register

MODGHC_PACKAGE_KEY =	DmSwQqk5nLj7roLAcydGz

BUILD_DEPENDS =		${RUN_DEPENDS}

RUN_DEPENDS =		devel/hs-mtl>=2.0.1,<2.3 \
			devel/hs-transformers-compat>=0.3,<0.6

.include <bsd.port.mk>
