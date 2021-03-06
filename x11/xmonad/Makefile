# $OpenBSD: Makefile,v 1.52 2017/11/21 00:02:18 kili Exp $

COMMENT-main =		tiling window manager
COMMENT-lib =		libraries for runtime configuration

DISTNAME =		xmonad-0.12
PKGNAME-main =		${DISTNAME}
PKGNAME-lib =		${DISTNAME:S,-,-lib-,}
CATEGORIES =		x11
HOMEPAGE =		http://www.xmonad.org/

MULTI_PACKAGES =		-main -lib

# BSD3
PERMIT_PACKAGE_CDROM =	Yes

WANTLIB-main =		X11 Xext Xinerama Xrandr Xss c m iconv \
			pthread util
WANTLIB-lib =

MODULES =		lang/ghc
MODGHC_BUILD =		cabal hackage haddock register nort

MODGHC_PACKAGE_KEY =	Gx5TWm0BSEJHl229E6kZrP

# Required because of the nort tag in MODGHC_BUILD
SUBST_VARS +=		MODGHC_PACKAGE_KEY

BUILD_DEPENDS =		${RUN_DEPENDS-lib}
RUN_DEPENDS-lib =	devel/hs-data-default \
			devel/hs-extensible-exceptions \
			devel/hs-mtl \
			devel/hs-utf8-string>=0.3,<1.1 \
			x11/hs-X11>=1.5,<1.7
LIB_DEPENDS-main =	converters/libiconv

# MODGHC_BUILD contains 'nort', an explicity dependency is needed for
# the -lib subpackage (plus the tweaks to MODGHC_SETUP_CONF_ARGS below).
RUN_DEPENDS-lib +=		lang/ghc=${MODGHC_VER}

post-install:
	@${INSTALL_MAN} ${WRKSRC}/man/xmonad.1 ${PREFIX}/man/man1
	@${INSTALL_DATA} ${WRKSRC}/CONFIG ${PREFIX}/share/doc/hs-${DISTNAME}
	@${INSTALL_DATA} ${WRKSRC}/man/xmonad.hs ${PREFIX}/share/doc/hs-${DISTNAME}/xmonad.hs
	@# Don't know why, but it installs the xmonad.hs into that directory:
	@rm -rf ${PREFIX}/share/${DISTNAME}

# Needs to be built with different configuration.
NO_TEST =	Yes

.include <bsd.port.mk>

# Override the 'nort' settings from ghc.port.mk, to get the correct
# flags and directories for the -lib subpackage.
MODGHC_SETUP_CONF_ARGS +=	--enable-library-profiling
MODGHC_SETUP_CONF_ARGS +=	--docdir=\$$datadir/doc/hs-\$$pkgid
MODGHC_SETUP_CONF_ARGS +=	--libsubdir=ghc/\$$pkgid
