# $OpenBSD: Makefile,v 1.30 2018/01/11 19:27:07 rpe Exp $

COMMENT =	highly reliable Enterprise Messaging System

V =		3.5.6
REVISION =	1
DISTNAME =	rabbitmq-server-$V
PKGNAME =	rabbitmq-$V
CATEGORIES =	net

HOMEPAGE =	http://www.rabbitmq.com/

MAINTAINER =	Sebastian Reitenbach <sebastia@openbsd.org>

# MPL
PERMIT_PACKAGE_CDROM = Yes

MASTER_SITES =	http://www.rabbitmq.com/releases/rabbitmq-server/v${V}/

MODULES =	lang/erlang \
		lang/python
MODERL_VERSION = 18
MODPY_RUNDEP =	No

USE_GMAKE =	Yes
CONFIGURE_STYLE = none

BUILD_DEPENDS =	archivers/unzip \
		archivers/zip \
		textproc/docbook \
		textproc/docbook-xsl \
		textproc/libxslt \
		textproc/xmlto

MAKE_ENV =	PYTHON=${MODPY_BIN} VERSION=${V}

RABBITUSER =	_rabbitmq

SUBST_VARS +=	RABBITUSER V

MODPY_ADJ_FILES +=	plugins-src/rabbitmq-amqp1.0/codegen.py
MODPY_ADJ_FILES +=	plugins-src/rabbitmq-management/bin/rabbitmqadmin

NO_TEST =	Yes

pre-build:
	${SUBST_CMD} ${WRKSRC}/scripts/rabbitmqctl \
		${WRKSRC}/scripts/rabbitmq-defaults

post-install:
	${INSTALL_DATA_DIR} ${PREFIX}/share/doc/rabbitmq
	@for file in INSTALL LICENSE*; do \
		mv ${PREFIX}/lib/rabbitmq/$$file \
			${PREFIX}/share/doc/rabbitmq; \
	done
	${INSTALL_DATA_DIR} ${PREFIX}/share/examples/rabbitmq
	${SUBST_CMD} -m 0644 -c ${FILESDIR}/rabbitmq.conf \
		${PREFIX}/share/examples/rabbitmq/rabbitmq-env.conf

.include <bsd.port.mk>
