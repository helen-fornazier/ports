# $OpenBSD: Makefile,v 1.47 2018/01/11 19:27:07 rpe Exp $

COMMENT=	communications server for Jabber/XMPP written in Lua
DISTNAME=	prosody-0.10.0
REVISION=	1
CATEGORIES=	net
MASTER_SITES=	http://prosody.im/downloads/source/

HOMEPAGE=	http://prosody.im/

MAINTAINER=	Henrik Friedrichsen <henrik@diff.cc>

# MIT
PERMIT_PACKAGE_CDROM=	Yes

USE_GMAKE=	Yes
MODULES=	lang/lua
LIB_DEPENDS=	devel/libidn
MODLUA_RUN_DEPENDS+= archivers/luazlib \
		databases/luadbi \
		devel/lua-bitop \
		devel/luafs \
		security/luasec \
		textproc/luaexpat>=1.3.0
TEST_DEPENDS =	${MODLUA_RUN_DEPENDS}
WANTLIB+=	crypto idn

SUBST_VARS+=	FLAVOR MAKE_PROGRAM

CONFIGURE_STYLE=simple
CONFIGURE_ARGS+=--prefix="${PREFIX}" \
		--sysconfdir="${SYSCONFDIR}/prosody" \
		--datadir="${VARBASE}/prosody" \
		--with-lua="${LOCALBASE}" \
		--with-lua-include="${MODLUA_INCL_DIR}" \
		--c-compiler="${CC}" \
		--linker="${CC}" \
		--ldflags="-I/usr/include -I${LOCALBASE}/include -L/usr/lib -L${LOCALBASE}/lib -shared" \
		--cflags="${CFLAGS} -I${LOCALBASE}/include -fPIC"

FAKE_FLAGS+=	CONFIG=${DESTDIR}${PREFIX}/share/examples/prosody

pre-configure:
	${SUBST_CMD} ${WRKSRC}/certs/Makefile
	cd ${WRKSRC}; sed -i -e 's,^#!/usr/bin/env lua,#!${MODLUA_BIN},' -e \
		's,^lua ,${MODLUA_BIN} ,' prosody prosodyctl tests/run_tests.sh

post-install:
	${INSTALL_DATA_DIR} ${PREFIX}/share/doc/prosody
	${INSTALL_DATA} ${WRKSRC}/README \
		${PREFIX}/share/doc/prosody
	touch ${PREFIX}/share/examples/prosody/prosody.log
	rm -f ${PREFIX}/share/examples/prosody/certs/Makefile.*

do-test:
	cd ${WRKSRC}/tests && sh run_tests.sh 0

.include <bsd.port.mk>
