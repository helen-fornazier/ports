# $OpenBSD: Makefile,v 1.110 2017/11/12 22:01:46 naddy Exp $

COMMENT-main=		mail and news client
COMMENT-bogofilter=	bogofilter plugin
COMMENT-spamassassin=	spamassassin plugin
COMMENT-pdfviewer=	pdfviewer plugin
COMMENT-gdata=		gdata plugin

V=			3.15.0
DISTNAME=		claws-mail-${V}
PKGNAME-main=		${DISTNAME}
PKGNAME-bogofilter=	claws-mail-bogofilter-${V}
PKGNAME-spamassassin=	claws-mail-spamassassin-${V}
PKGNAME-pdfviewer=	claws-mail-pdfviewer-${V}
PKGNAME-gdata=		claws-mail-gdata-${V}

REVISION=		1
REVISION-gdata=		2
REVISION-main=		3

CATEGORIES=		mail news

HOMEPAGE=		http://www.claws-mail.org/
MAINTAINER=		Daniel Jakots <obsd@chown.me>

# GPLv3+
PERMIT_PACKAGE_CDROM=	Yes

MASTER_SITES=		http://www.claws-mail.org/releases/

DIST_SUBDIR=		claws

MULTI_PACKAGES=		-main -bogofilter -spamassassin -pdfviewer -gdata
FLAVORS=		jpilot ldap
FLAVOR?=

FLAVOR_STRING=		${FLAVOR_EXT:S/-/,/g}
SUBST_VARS=		FLAVOR_STRING

RUN_DEPENDS-bogofilter=	${BUILD_PKGPATH} \
			mail/bogofilter
RUN_DEPENDS-spamassassin=${BUILD_PKGPATH} \
			mail/p5-Mail-SpamAssassin

WANTLIB += X11 Xcomposite Xcursor Xdamage Xext Xfixes Xi Xinerama
WANTLIB += Xrandr Xrender atk-1.0 cairo crypto curl etpan execinfo
WANTLIB += expat ffi fontconfig freetype gdk-x11-2.0 gdk_pixbuf-2.0
WANTLIB += gio-2.0 glib-2.0 gmodule-2.0 gobject-2.0 graphite2
WANTLIB += gthread-2.0 gtk-x11-2.0 harfbuzz iconv intl m nghttp2 pango-1.0
WANTLIB += pangocairo-1.0 pangoft2-1.0 pcre pixman-1 png pthread
WANTLIB += sasl2 ssl xcb xcb-render xcb-shm z

WANTLIB-main =  ${WANTLIB}
WANTLIB-main += ICE SM X11-xcb archive assuan bz2 c canberra canberra-gtk
WANTLIB-main += croco-0.6 db dbus-1 dbus-glib-1 enchant gmp gnutls gpg-error
WANTLIB-main += gpgme hogweed ical icalss icalvcal icudata icui18n icuuc idn2
WANTLIB-main += ltdl lz4 lzma nettle notify ogg p11-kit perl rsvg-2
WANTLIB-main += startup-notification-1 ${COMPILER_LIBCXX} tasn1 unistring vorbis
WANTLIB-main += vorbisfile xcb-util xml2

WANTLIB-gdata = ${WANTLIB}
WANTLIB-gdata += gck-1 gcr-base-3 gcrypt gdata goa-1.0 gpg-error json-glib-1.0
WANTLIB-gdata += lzma nspr4 nss3 oauth p11-kit plc4 plds4 smime3 nssutil3
WANTLIB-gdata += soup-2.4 sqlite3 ssl3 xml2

WANTLIB-pdfviewer =  ${WANTLIB}
WANTLIB-pdfviewer += jpeg lcms2 openjp2 poppler poppler-glib tiff

LIB_DEPENDS=		devel/libexecinfo \
			mail/libetpan \
			security/cyrus-sasl2 \
			x11/gtk+2

RUN_DEPENDS-main=	${RUN_DEPENDS} \
			devel/desktop-file-utils \
			x11/gtk+3,-guic

LIB_DEPENDS-main=	${LIB_DEPENDS} \
			archivers/libarchive \
			archivers/xz \
			devel/startup-notification \
			textproc/enchant \
			audio/libcanberra,-gtk \
			devel/libnotify \
			security/gnutls>=2.2 \
			security/gpgme \
			textproc/libical \
			x11/dbus-glib

LIB_DEPENDS-pdfviewer=	${LIB_DEPENDS} \
			print/poppler

LIB_DEPENDS-gdata=	${LIB_DEPENDS} \
			devel/libgdata

#geolocation looks for champlain <= 0.10
#python tries to dlopen libpython2.7.so
CONFIGURE_ARGS+=	--disable-acpi_notifier-plugin \
			--disable-compface \
			--disable-fancy-plugin \
			--disable-geolocation-plugin \
			--disable-python-plugin \
			--enable-new-addrbook

USE_GMAKE=		Yes
LIBTOOL_FLAGS=		--tag=disable-static
CONFIGURE_STYLE=	autoconf

AUTOCONF_VERSION=	2.69
CONFIGURE_ENV+=		CPPFLAGS="-I${X11BASE}/include" \
			LDFLAGS="-L${X11BASE}/lib"

.if ${FLAVOR:Mjpilot}
LIB_DEPENDS-main+=	comms/pilot-link
WANTLIB-main +=		pisock
RUN_DEPENDS-main+=	comms/jpilot
.else
CONFIGURE_ARGS+=	--disable-jpilot
.endif

.if ${FLAVOR:Mldap}
WANTLIB-main+=		lber-2.4 ldap-2.4
LIB_DEPENDS-main+=	databases/openldap
.else
CONFIGURE_ARGS+=	--disable-ldap
.endif

TOOLS=		OOo2claws-mail.pl \
		acroread2claws-mail.pl \
		calypso_convert.pl \
		claws-mail-compose-insert-files.pl \
		convert_mbox.pl \
		csv2addressbook.pl \
		eud2gc.py \
		filter_conv.pl filter_conv_new.pl \
		fix_date.sh \
		gif2xface.pl \
		google_msgid.pl google_search.pl \
		kmail-mailbox2claws-mail.pl \
		kmail2claws-mail.pl kmail2claws-mail_v2.pl \
		mairix.sh \
		mew2claws-mail.pl \
		multiwebsearch.conf multiwebsearch.pl \
		nautilus2claws-mail.sh \
		outlook2claws-mail.pl \
		popfile-link.sh \
		tb2claws-mail tbird2claws.py \
		textviewer.pl textviewer.sh \
		thunderbird-filters-convertor.pl \
		uudec uuooffice \
		vcard2xml.py \
		README \
		kdeservicemenu/claws-mail-attach-files.desktop.kde4template \
		kdeservicemenu/claws-mail-attach-files.desktop.template \
		kdeservicemenu/claws-mail-kdeservicemenu.pl \
		kdeservicemenu/install.sh \
		kdeservicemenu/README

post-install:
	${INSTALL_DATA_DIR} ${PREFIX}/share/icons/hicolor/48x48/apps
	${INSTALL_DATA} ${WRKSRC}/claws-mail.png ${PREFIX}/share/icons/hicolor/48x48/apps/claws-mail.png
	${INSTALL_DATA_DIR} ${PREFIX}/share/icons/hicolor/64x64/apps
	${INSTALL_DATA} ${WRKSRC}/claws-mail-64x64.png ${PREFIX}/share/icons/hicolor/64x64/apps/claws-mail.png
	${INSTALL_DATA_DIR} ${PREFIX}/share/icons/hicolor/128x128/apps
	${INSTALL_DATA} ${WRKSRC}/claws-mail-128x128.png ${PREFIX}/share/icons/hicolor/128x128/apps/claws-mail.png
	${INSTALL_DATA_DIR} ${PREFIX}/share/applications/
	${INSTALL_DATA} ${WRKSRC}/claws-mail.desktop ${PREFIX}/share/applications/claws-mail.desktop
	${INSTALL_DATA_DIR} ${PREFIX}/share/claws-mail/tools/kdeservicemenu
.for i in ${TOOLS}
	${INSTALL_DATA} ${WRKSRC}/tools/${i} \
	${PREFIX}/share/claws-mail/tools/${i}
.endfor

.include <bsd.port.mk>
