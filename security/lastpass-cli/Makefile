# $OpenBSD: Makefile,v 1.13 2017/11/11 13:30:44 sthen Exp $

COMMENT =	LastPass command line interface tool

GH_ACCOUNT =	lastpass
GH_PROJECT =	lastpass-cli
GH_TAGNAME =	v1.2.2
CATEGORIES =	security

MAINTAINER =	Bjorn Ketelaars <bjorn.ketelaars@hydroxide.nl>

# GPLv2
PERMIT_PACKAGE_CDROM =	Yes

WANTLIB =	c curl crypto kvm ssl xml2

MODULES =	devel/cmake

BUILD_DEPENDS=	textproc/asciidoc
LIB_DEPENDS =	net/curl \
		textproc/libxml
TEST_DEPENDS=	${BUILD_DEPENDS} \
		shells/bash

ALL_TARGET =	all doc-man

do-install:
	${INSTALL_PROGRAM} ${WRKBUILD}/lpass ${PREFIX}/bin
	${INSTALL_MAN} ${WRKBUILD}/lpass.1 ${PREFIX}/man/man1

do-test:
	cd ${WRKSRC}/test && sed -i 's,#!/bin/bash,#!${LOCALBASE}/bin/bash,' *
	cd ${WRKSRC} && make test

.include <bsd.port.mk>
