# $OpenBSD: Makefile,v 1.185 2018/01/11 19:27:02 rpe Exp $

COMMENT-main =	GIT - Tree History Storage Tool
COMMENT-svn =	GIT - subversion interoperability tools
COMMENT-x11 =	GIT - graphical tools

V =		2.15.1
DISTNAME =	git-${V}
PKGNAME-main =	${DISTNAME}
PKGNAME-svn =	git-svn-${V}
PKGNAME-x11 =	git-x11-${V}
CATEGORIES =	devel
REVISION-main =	0

HOMEPAGE =	https://git-scm.com/

MAINTAINER =	Benoit Lecocq <benoit@openbsd.org>

# GPLv2 only
PERMIT_PACKAGE_CDROM = Yes

DOC_DISTFILE =		git-manpages-${V}${EXTRACT_SUFX}
DISTFILES =		${DISTNAME}${EXTRACT_SUFX} ${DOC_DISTFILE}
EXTRACT_ONLY =		${DISTNAME}${EXTRACT_SUFX}

MASTER_SITES =		https://www.kernel.org/pub/software/scm/git/

MODULES =		x11/tk lang/python

MODPY_BUILDDEP =	No
MODPY_RUNDEP =		No
MODPY_ADJ_FILES =	contrib/hooks/multimail/git_multimail.py \
			contrib/hooks/multimail/migrate-mailhook-config \
			contrib/hooks/multimail/post-receive.example

BUILD_DEPENDS =		devel/gettext-tools \
			devel/p5-Error

MULTI_PACKAGES =	-main -svn -x11

WANTLIB-main =		c crypto curl expat iconv intl pthread ssl z

RUN_DEPENDS-main =	net/rsync \
			devel/p5-Error \
			devel/cvsps
LIB_DEPENDS-main =	devel/gettext \
			net/curl

RUN_DEPENDS-svn =	${BASE_PKGPATH} \
			devel/subversion,-perl \
			www/p5-URI \
			www/p5-libwww
LIB_DEPENDS-svn =
WANTLIB-svn =
PKG_ARCH-svn =		*

RUN_DEPENDS-x11 =	${BASE_PKGPATH},-main \
			${MODTK_RUN_DEPENDS}
LIB_DEPENDS-x11 =
WANTLIB-x11 =
PKG_ARCH-x11 =		*

MAKE_FLAGS =		V=1 \
			gitexecdir=libexec/git \
			TCLTK_PATH=${MODTK_BIN} \
			TCL_PATH=${MODTCL_BIN}
MAKE_ENV =		TEST_TAR=${LOCALBASE}/bin/gtar

CONFIGURE_STYLE =	gnu
CONFIGURE_ARGS =	--sysconfdir=${SYSCONFDIR} \
			--mandir=${PREFIX}/man \
			--with-curl=${LOCALBASE} \
			--with-iconv=${LOCALBASE} \
			--with-tcltk=${MODTK_BIN} \
			--with-python=no
CONFIGURE_ENV =		CPPFLAGS="-I${WRKSRC} -I${LOCALBASE}/include" \
			LDFLAGS="-L${LOCALBASE}/lib" \
			DIFF=diff TAR=tar

USE_GMAKE =		Yes

TEST_DEPENDS =		archivers/gtar \
			archivers/unzip \
			archivers/zip \
			devel/cvsps \
			devel/subversion,-perl

post-extract:
	@mkdir -p ${WRKSRC}/doc
	@cd ${WRKSRC}/doc && ${TAR} -xzf ${FULLDISTDIR}/${DOC_DISTFILE}
	@cd ${WRKSRC} && perl -pi -e "s|/usr/share/git|${TRUEPREFIX}/share/git|g" \
		doc/man1/git-clone.1 doc/man1/git-init.1 doc/man1/gitweb.1

post-install:
	${INSTALL_DATA} ${WRKBUILD}/libgit.a ${PREFIX}/lib
	${INSTALL_DATA_DIR} ${PREFIX}/share/emacs/site-lisp
	${INSTALL_DATA} ${WRKBUILD}/contrib/emacs/*.el \
		${PREFIX}/share/emacs/site-lisp
	cd ${WRKBUILD}/doc && \
		pax -rw . ${PREFIX}/man
	${INSTALL_DATA} ${WRKBUILD}/contrib/hooks/post-receive-email \
		${PREFIX}/share/git-core/templates/hooks/post-receive-email.sample
	${INSTALL_DATA_DIR} ${PREFIX}/share/git-core/templates/hooks/multimail
.for f in git_multimail.py migrate-mailhook-config post-receive.example
	${INSTALL_DATA} ${WRKBUILD}/contrib/hooks/multimail/$f \
		${PREFIX}/share/git-core/templates/hooks/multimail
.endfor
	${INSTALL_DATA} ${WRKBUILD}/contrib/hooks/setgitperms.perl \
		${PREFIX}/share/git-core/templates/hooks/setgitperms.perl
	chown -R ${BINOWN}:${BINGRP} ${PREFIX}/libexec/git
	cd ${WRKBUILD}/gitweb && \
		${MAKE_ENV} ${MAKE_PROGRAM} gitwebdir=${TRUEPREFIX}/share/gitweb install
	perl -pi -e "s|${WRKINST}||g" ${PREFIX}/share/gitweb/gitweb.cgi
	${INSTALL_DATA} ${WRKBUILD}/gitweb/README ${PREFIX}/share/gitweb

do-test:
	cd ${WRKSRC} && ${MAKE_ENV} GIT_TEST_OPTS="--immediate" ${MAKE_PROGRAM} \
		HOME=${WRKDIST}/t test

.include <bsd.port.mk>
