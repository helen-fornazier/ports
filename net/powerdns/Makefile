# $OpenBSD: Makefile,v 1.59 2018/01/11 19:27:07 rpe Exp $

BROKEN-hppa =		undefined reference to '__sync_fetch_and_add_4'

COMMENT-main=		modular authoritative nameserver (with database support)
COMMENT-mysql=		MySQL database access module for PowerDNS
COMMENT-pgsql=		PGSQL database access module for PowerDNS
COMMENT-ldap=		LDAP module for PowerDNS

V=			4.0.4
DISTNAME=		pdns-${V}
EXTRACT_SUFX =		.tar.bz2
PKGNAME=		powerdns-${V}
PKGNAME-main=		powerdns-${V}
PKGNAME-mysql=		powerdns-mysql-${V}
PKGNAME-pgsql=		powerdns-pgsql-${V}
PKGNAME-ldap=		powerdns-ldap-${V}
CATEGORIES=		net
HOMEPAGE=		http://www.powerdns.com/
REVISION-ldap=		1
REVISION-main=		2
REVISION-mysql=		1
REVISION-pgsql=		1

MULTI_PACKAGES=		-main -mysql -pgsql -ldap

# GPLv2
PERMIT_PACKAGE_CDROM=	Yes

COMPILER =		base-clang ports-gcc

WANTLIB += m pthread ${COMPILER_LIBCXX}
#WANTLIB += ${MODGCC4_CPPWANTLIB}

WANTLIB-main += ${WANTLIB}
WANTLIB-main += boost_program_options-mt boost_serialization-mt
WANTLIB-main += bz2 c crypto gmp sqlite3 z

MASTER_SITES=		http://downloads.powerdns.com/releases/

NO_TEST=		Yes

LIB_DEPENDS-main=	${LIB_DEPENDS} \
			databases/sqlite3 \
			devel/boost \
			devel/gmp

PSEUDO_FLAVORS+=	no_mysql no_pgsql no_ldap
FLAVOR?=

BACKENDS=		gsqlite3

SYSCONFDIR=		${BASESYSCONFDIR}/pdns

CONFIGURE_STYLE=	gnu
CONFIGURE_ARGS+=	--disable-shared \
			--with-modules="bind" \
			--with-sqlite3 \
			--with-dynmodules="${BACKENDS}" \
			--without-lua \
			--disable-hardening \
			--without-protobuf

CONFIGURE_ENV+=		CPPFLAGS="-I${LOCALBASE}/include" \
			LDFLAGS="-L${LOCALBASE}/lib"
LIBTOOL_FLAGS=		--tag=disable-static

.include <bsd.port.arch.mk>

# MySQL
.if ${BUILD_PACKAGES:M-mysql}
CONFIGURE_ARGS+=	--with-mysql=${LOCALBASE}
BACKENDS+=		gmysql
.else
CONFIGURE_ARGS+=	--without-mysql
.endif
LIB_DEPENDS-mysql=	${LIB_DEPENDS} \
			databases/mariadb
RUN_DEPENDS-mysql=	${FULLPKGNAME-main}:net/powerdns
WANTLIB-mysql+=		crypto lib/mysql/mysqlclient ssl z ${WANTLIB}

# PostgreSQL
.if ${BUILD_PACKAGES:M-pgsql}
CONFIGURE_ARGS+=	--with-pgsql=${LOCALBASE} \
			--with-pgsql-includes=${LOCALBASE}/include/postgresql
BACKENDS+=		gpgsql
.else
CONFIGURE_ARGS+=	--without-pgsql
.endif
LIB_DEPENDS-pgsql=	${LIB_DEPENDS} \
			databases/postgresql,-main
RUN_DEPENDS-pgsql=	${FULLPKGNAME-main}:net/powerdns
WANTLIB-pgsql=		crypto pq>=2 ssl ${WANTLIB}

# LDAP
.if ${BUILD_PACKAGES:M-ldap}
BACKENDS+=		ldap
.else
CONFIGURE_ARGS+=	--without-ldap
.endif
LIB_DEPENDS-ldap=	${LIB_DEPENDS} \
			databases/openldap
RUN_DEPENDS-ldap=	${FULLPKGNAME-main}:net/powerdns
WANTLIB-ldap+=		${WANTLIB} crypto lber-2.4 ldap_r-2.4 sasl2 ssl

EXAMPLE_DIR=		${PREFIX}/share/examples/pdns/
post-install:
	rm -f ${PREFIX}/lib/pdns/*.la
	${INSTALL_DATA_DIR} ${EXAMPLE_DIR}
.for t in tables-mysql.sql tables-pgsql.sql tables-sqlite.sql
	${INSTALL_DATA} ${FILESDIR}/$t ${EXAMPLE_DIR}
.endfor
	${INSTALL_DATA} ${WRKSRC}/pdns/pdns.conf-dist ${EXAMPLE_DIR}
	${INSTALL_DATA} ${FILESDIR}/pdns.conf ${EXAMPLE_DIR}

.include <bsd.port.mk>
