# $OpenBSD: Makefile,v 1.5 2016/07/06 16:11:52 krw Exp $

COMMENT =	declarative definition of command line interfaces
CATEGORIES =	devel

# When V changes, remember to bump REVISION for build dependents like opam!
V =		0.9.8
NAME =		cmdliner
DISTNAME =	${NAME}-${V}
EXTRACT_SUFX =	.tbz
PKGNAME =	ocaml-${DISTNAME}
MASTER_SITES =	http://erratique.ch/software/${NAME}/releases/

HOMEPAGE =	http://erratique.ch/software/${NAME}


# BSD3
PERMIT_PACKAGE_CDROM =		Yes

MODULES =	lang/ocaml

BUILD_DEPENDS =	sysutils/findlib devel/ocaml-ocamlbuild
RUN_DEPENDS =	lang/ocaml

ALL_TARGET =	${NAME}.{cma,cmi,mli}
.include <bsd.port.arch.mk>
.if ${PROPERTIES:Mocaml_native}
ALL_TARGET +=	${NAME}.{a,cmx,cmxa}
.if ${PROPERTIES:Mocaml_native_dynlink}
ALL_TARGET +=	${NAME}.cmxs
.endif
.endif


do-build:
	cd ${WRKSRC} && ocamlbuild ${ALL_TARGET}

do-install:
	env -i ${MAKE_ENV} ocamlfind install ${NAME} \
		${WRKSRC}/pkg/META \
		${ALL_TARGET:S|^|${WRKSRC}/_build/src/|}
	${INSTALL_DATA_DIR} ${PREFIX}/share/doc/ocaml-${NAME}/api
	${INSTALL_DATA} \
		${WRKDIST}/{README,CHANGES}.md \
		${PREFIX}/share/doc/ocaml-${NAME}/
	${INSTALL_DATA} ${WRKDIST}/doc/* ${PREFIX}/share/doc/ocaml-${NAME}/api/


.include <bsd.port.mk>
