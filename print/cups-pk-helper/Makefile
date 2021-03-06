# $OpenBSD: Makefile,v 1.16 2017/11/21 00:13:03 naddy Exp $

COMMENT=	fine-grained privileges PolicyKit helper for CUPS

DISTNAME=	cups-pk-helper-0.2.6
EXTRACT_SUFX=	.tar.xz
REVISION=	0

CATEGORIES=	print sysutils

MAINTAINER=	Antoine Jacoutot <ajacoutot@openbsd.org>

HOMEPAGE=	http://www.freedesktop.org/wiki/Software/cups-pk-helper

# GPLv2
PERMIT_PACKAGE_CDROM=	Yes

WANTLIB =  c cups gio-2.0 glib-2.0 gobject-2.0 iconv intl
WANTLIB += polkit-gobject-1 pthread

MASTER_SITES=	http://www.freedesktop.org/software/cups-pk-helper/releases/

MODULES=	textproc/intltool

LIB_DEPENDS=	sysutils/polkit \
		print/cups,-libs

# polkit(8) almost always needs to know the "active" session
RUN_DEPENDS +=	sysutils/consolekit

# /usr/local/share/dbus-1/system-services/
RUN_DEPENDS +=	x11/dbus,-suid

USE_GMAKE=	Yes

CONFIGURE_STYLE=gnu
CONFIGURE_ENV=	CPPFLAGS="-I${LOCALBASE}/include" \
		LDFLAGS="-L${LOCALBASE}/lib"

FAKE_FLAGS=	sysconfdir=${PREFIX}/share/examples/cups-pk-helper

.include <bsd.port.mk>
