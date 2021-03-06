# $OpenBSD: Makefile,v 1.26 2017/11/13 06:57:36 steven Exp $

COMMENT=	library of Fortran linear algebra subroutines

VERSION=	3.7.1
DISTNAME=	lapack-${VERSION}

SHARED_LIBS=	lapack 6.0

CATEGORIES=	math
DISTFILES=	${DISTNAME}.tgz manpages.tgz:0

HOMEPAGE=	http://www.netlib.org/lapack/

MAINTAINER=	Steven Mestdagh <steven@openbsd.org>

# BSD
PERMIT_PACKAGE_CDROM=	Yes

MASTER_SITES=	http://www.netlib.org/lapack/ \
		http://www.netlib.no/netlib/lapack/
MASTER_SITES0=	http://www.netlib.org/lapack/
EXTRACT_SUFX=	.tgz
DIST_SUBDIR=	${DISTNAME}

LIB_DEPENDS =	math/blas
WANTLIB =	blas>=1

MODULES=	fortran
MODFORTRAN_COMPILER = gfortran
BUILD_DEPENDS=	${MODFORTRAN_BUILD_DEPENDS}

MAKE_ENV=	SHLIB_MAJOR=${LIBlapack_VERSION:R} \
		SHLIB_MINOR=${LIBlapack_VERSION:E} \
		TIMER=EXT_ETIME \
		FC="${MODFORTRAN_COMPILER} -cpp"
FAKE_FLAGS=	LIBDIR=${LOCALBASE}/lib DEBUGLIBS=no
USE_GROFF =	Yes

TEST_DEPENDS=	devel/gmake
TEST_FLAGS=	PLAT= OPTS= FORTRAN=${MODFORTRAN_COMPILER} \
		LOADER=${MODFORTRAN_COMPILER} \
		LAPACKLIB=SRC/liblapack.a \
		BLASLIB="${LOCALBASE}/lib/libblas.a ${LOCALBASE}/lib/libgfortran.a"

MAKE_FILE=	${FILESDIR}/Makefile
WRKSRC=		${WRKDIST}/SRC

MANSRC=		${WRKDIR}/man/man3

# avoid 'unknown manpage type' errors and move manpages to section 3
pre-configure:
	@cp ${WRKDIST}/make.inc.example ${WRKDIST}/make.inc
	@cd ${WRKSRC} && for f in *.F ; do mv $$f $${f%.F}.f ; done

post-build:
	@cd ${MANSRC} && for m in *.f.3 ; do perl -pi \
		-e 'if ($$. == 1) {s/(\.TH\s+)"([^"]+)\.f"\s+3\s+("[^"]+")/\1 \2 3f \3 "LAPACK Version ${VERSION}" "LAPACK Version ${VERSION}"/}' \
		-e 'if ($$. == 5) {s/^(\w+)\.f \\-/\1/}' $$m ; done
	@cd ${MANSRC} && \
		for m in SRC_*.f.3; do mv $$m $${m#SRC_}; done && \
		for m in *.f.3; do mv $$m $${m%\.f\.3}.3f; done

post-install:
	@cd ${MANSRC} && for m in `${MAKE} -f ${MAKE_FILE} printsrc | \
		perl -p -e 's/\s/\n/g' | \
		grep -v TIME | \
		grep -v ssytrd_sb2st.f | \
		grep -v dsytrd_sb2st.f | \
		grep -v chetrd_hb2st.f | \
		grep -v zhetrd_hb2st.f | \
		grep -v iparam2stage.f | \
		grep -v lsame.f | \
	 	grep -v xerbla.f | \
		grep -v xerbla_array.f` ; do \
		${INSTALL_MAN} `basename $${m%.f}.3f` ${PREFIX}/man/man3f ; done
	@${INSTALL_MAN} ${MANSRC}/*TIME*.3f ${PREFIX}/man/man3f

do-test:
	cd ${WRKDIST}/TESTING/MATGEN && gmake ${ALL_TEST_FLAGS}
	cd ${WRKDIST}/TESTING && gmake ${ALL_TEST_FLAGS}

.include <bsd.port.mk>
