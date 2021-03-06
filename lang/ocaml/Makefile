# $OpenBSD: Makefile,v 1.79 2017/09/15 09:23:12 ajacoutot Exp $

MULTI_PACKAGES = -graphics -main

COMMENT-main =	   ML language with complete class-based objective system
COMMENT-graphics = OCaml Graphics library providing basic drawing primitives

# XXX Don't even think of updating ocaml alone.
# Do check that the ports that depend on it still work, or repair them.
# Don't forget to bump version in ocaml.port.mk, too!
VERSION=		4.03.0
REVISION=		2

PKGNAME-main =		ocaml-${VERSION}
PKGNAME-graphics =	ocaml-graphics-${VERSION}

# OCaml has no binary compatibility between releases.
PKGSPEC-main =	ocaml-=${VERSION}

CATEGORIES=	lang
# Remove last version component ocaml-X.XX.X -> ocaml-X.XX
BASENAME =	${DISTNAME:C/\.[^.]*$//}
MASTER_SITES=	http://caml.inria.fr/pub/distrib/${BASENAME}/
DOCFILES=	${BASENAME}-refman-html.tar.gz
DISTFILES=	${DISTNAME}.tar.gz ${DOCFILES}
DISTNAME =	ocaml-${VERSION}

HOMEPAGE=	https://ocaml.org/
MAINTAINER=	Anil Madhavapeddy <avsm@openbsd.org>

# QPL/LGPL
PERMIT_PACKAGE_CDROM=	Yes

CONFIGURE_STYLE=	simple dest
CONFIGURE_ARGS+=	-prefix ${PREFIX} \
			-aspp '${CC} ${CFLAGS} -c' \
			-cc '${CC} ${CFLAGS}' \
			-x11include ${X11BASE}/include \
			-x11lib ${X11BASE}/lib
CONFIGURE_ENV+=		OPENBSD_LOCALBASE="${LOCALBASE}"

USE_GMAKE=	Yes

RUN_DEPENDS-graphics +=	lang/ocaml
WANTLIB-main =		c curses m pthread
WANTLIB-graphics =	X11

.if ${MACHINE_ARCH} != aarch64
# for libbfd; devel/gdb doesn't build on aarch64 yet.
BUILD_DEPENDS +=	devel/gdb
WANTLIB-main +=		iberty z
.endif

.include <bsd.port.arch.mk>

.if ${PROPERTIES:Mocaml_native}
ALL_TARGET=	world bootstrap opt opt.opt
PKG_ARGS +=	-Dnative=1
TEST_DEPENDS +=	${BUILD_PKGPATH}

.if ${PROPERTIES:Mocaml_native_dynlink}
PKG_ARGS +=	-Ddynlink=1
.else
PKG_ARGS +=	-Ddynlink=0
.endif

.else
ALL_TARGET=	world bootstrap
PKG_ARGS +=	-Dnative=0
NO_TEST   =	yes
.endif


post-install:
	@${INSTALL_DATA_DIR} ${PREFIX}/share/doc/ocaml/html/libref
	@${INSTALL_DATA} ${WRKDIR}/htmlman/*.{html,gif,css} \
		${PREFIX}/share/doc/ocaml/html
	@${INSTALL_DATA} ${WRKDIR}/htmlman/libref/* \
		${PREFIX}/share/doc/ocaml/html/libref
	@${INSTALL_DATA} \
		${WRKSRC}/{LICENSE,Changes} \
		${PREFIX}/share/doc/ocaml

# PFRAG.native was generated from PLIST with:
# egrep '(ocamlopt|\.cmx|\.cmxa|\.cmxs|\.opt|opt\.1|opt.cmi|\.native|\.o)$'

# One test in the suite (testsocket.ml) requires an active
# connection to internet
TEST_IS_INTERACTIVE =		Yes

do-test:
	@cd ${WRKSRC}/testsuite && ulimit -Sn 256 && ${MAKE_PROGRAM} all

.include <bsd.port.mk>
