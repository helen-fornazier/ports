# $OpenBSD: Makefile,v 1.40 2017/11/26 18:59:32 landry Exp $

COMMENT=	Xfce4 disk performance panel plugin

XFCE_VERSION=	2.6.1
XFCE_PLUGIN=	diskperf
REVISION=	1

# BSD
PERMIT_PACKAGE_CDROM=	Yes

MODULES=	x11/xfce4
MODXFCE_WANTLIB =	xfce4panel-2.0

WANTLIB += ICE SM X11 X11-xcb Xcomposite Xcursor Xdamage
WANTLIB += Xext Xfixes Xi Xinerama Xrandr Xrender Xtst
WANTLIB += atk-1.0 cairo expat ffi fontconfig freetype
WANTLIB += gdk_pixbuf-2.0 gio-2.0 glib-2.0 gmodule-2.0 gobject-2.0
WANTLIB += gthread-2.0 m pango-1.0 pangocairo-1.0 iconv intl
WANTLIB += pangoft2-1.0 pcre pixman-1 png
WANTLIB += startup-notification-1 xcb xcb-util xcb-render xcb-shm
WANTLIB += xfce4util z xfce4ui-2 harfbuzz pthread graphite2
WANTLIB += atk-bridge-2.0 atspi cairo-gobject dbus-1 epoxy gdk-3 gtk-3


.include <bsd.port.mk>
