# $OpenBSD: Makefile,v 1.19 2018/01/05 12:33:08 sthen Exp $

COMMENT =		deduplicating backup program

MODPY_EGG_VERSION =	1.1.4
DISTNAME =		borgbackup-${MODPY_EGG_VERSION}
REVISION =		0

CATEGORIES =		sysutils

MAINTAINER =		Bjorn Ketelaars <bjorn.ketelaars@hydroxide.nl>

# BSD-3
PERMIT_PACKAGE_CDROM =	Yes

MODULES =		lang/python
MODPY_PI =		Yes
MODPY_SETUPTOOLS =	Yes
MODPY_VERSION =		${MODPY_DEFAULT_VERSION_3}

WANTLIB +=		${MODPY_WANTLIB} b2 crypto lz4 pthread zstd

LIB_DEPENDS +=		${MODPY_LIB_DEPENDS} \
			archivers/lz4 \
			archivers/zstd \
			security/libb2
BUILD_DEPENDS +=	${RUN_DEPENDS} \
			devel/py-setuptools_scm${MODPY_FLAVOR} \
			textproc/py-sphinx_guzzle_theme${MODPY_FLAVOR}
RUN_DEPENDS +=		net/py-msgpack${MODPY_FLAVOR}
TEST_DEPENDS +=		${RUN_DEPENDS} \
			devel/py-test${MODPY_FLAVOR} \
			devel/py-test-benchmark${MODPY_FLAVOR} \
			devel/py-test-xdist${MODPY_FLAVOR}

post-build:
	${MODPY_CMD} build_ext --inplace
	cd ${WRKSRC}/docs; env PYTHONPATH=${WRKSRC} \
		make man SPHINXBUILD=sphinx-build${MODPY_BIN_SUFFIX}

post-install:
	${INSTALL_MAN} ${WRKSRC}/docs/_build/man/borg.1 ${PREFIX}/man/man1/borg.1

do-test: fake
	cd ${WRKSRC}; \
		PATH=${WRKINST}/usr/local/bin:${PATH} \
		PYTHONPATH=${WRKSRC}/src \
		${MODPY_BIN} -m pytest --ignore lib*

.include <bsd.port.mk>
