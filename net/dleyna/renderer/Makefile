# $OpenBSD: Makefile,v 1.4 2017/10/09 17:45:27 ajacoutot Exp $

COMMENT=		service for interacting with DMRs

GH_PROJECT=		dleyna-renderer

SHARED_LIBS +=	dleyna-renderer-1.0       0.0 # 1.3

RUN_DEPENDS=		net/dleyna/connector-dbus

LIB_DEPENDS=		net/dleyna/core \
			net/gupnp/av \
			net/gupnp/dlna

FAKE_FLAGS=		sysconfdir=${PREFIX}/share/examples/dleyna-renderer

WANTLIB += c dleyna-core-1.0 ffi gio-2.0 glib-2.0 gmodule-2.0
WANTLIB += gobject-2.0 gssdp-1.0 gupnp-1.0 gupnp-av-1.0 gupnp-dlna-2.0
WANTLIB += iconv intl lzma m pcre pthread soup-2.4 sqlite3 xml2
WANTLIB += z

.include <bsd.port.mk>
