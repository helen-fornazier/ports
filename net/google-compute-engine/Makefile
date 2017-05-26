# $OpenBSD: Makefile,v 1.76 2017/02/25 16:04:20 danj Exp $

COMMENT =	Google daemon for use with Google Cloud Compute Engine

DISTNAME =	google-compute-engine-2.3.6

GH_ACCOUNT =	GoogleCloudPlatform
GH_PROJECT =	compute-image-packages
GH_TAGNAME =	20170426

CATEGORIES =	net

HOMEPAGE =	https://github.com/GoogleCloudPlatform/compute-image-packages

MAINTAINER =	Helen Koike <helen.koike@collabora.com>

# Apache 2.0
PERMIT_PACKAGE_CDROM =	Yes

MODULES =		lang/python

MODPY_SETUPTOOLS =	Yes

MODPY_ADJ_FILES =	scripts/optimize_local_ssd \
		scripts/set_multiqueue \
		google_compute_engine/network_setup/network_setup.py \
		google_compute_engine/network_setup/__init__.py \
		google_compute_engine/metadata_scripts/script_retriever.py \
		google_compute_engine/metadata_scripts/__init__.py \
		google_compute_engine/metadata_scripts/script_executor.py \
		google_compute_engine/metadata_scripts/script_manager.py \
		google_compute_engine/ip_forwarding/__init__.py \
		google_compute_engine/ip_forwarding/ip_forwarding_utils.py \
		google_compute_engine/ip_forwarding/ip_forwarding_daemon.py \
		google_compute_engine/network_utils.py \
		google_compute_engine/clock_skew/clock_skew_daemon.py \
		google_compute_engine/clock_skew/__init__.py \
		google_compute_engine/__init__.py \
		google_compute_engine/metadata_watcher.py \
		google_compute_engine/instance_setup/instance_config.py \
		google_compute_engine/instance_setup/__init__.py \
		google_compute_engine/instance_setup/instance_setup.py \
		google_compute_engine/test_compat.py \
		google_compute_engine/config_manager.py \
		google_compute_engine/file_utils.py \
		google_compute_engine/accounts/accounts_daemon.py \
		google_compute_engine/accounts/__init__.py \
		google_compute_engine/accounts/accounts_utils.py \
		google_compute_engine/logger.py \
		google_compute_engine/boto/__init__.py \
		google_compute_engine/boto/compute_auth.py \
		google_compute_engine/boto/boto_config.py \
		google_compute_engine/compat.py

RUN_DEPENDS =	shells/bash \
		security/sudo \
		net/ntp \
		net/py-boto \
		net/py-netifaces \
		net/py-netaddr

pre-configure:
	@sed -i -e 's|%%PREFIX%%|${PREFIX}|g' \
		${WRKSRC}/build_packages.sh \
		${WRKSRC}/google_compute_engine/accounts/accounts_utils.py \
		${WRKSRC}/google_compute_engine/boto/boto_config.py \
		${WRKSRC}/google_compute_engine/boto/compute_auth.py \
		${WRKSRC}/google_compute_engine/config_manager.py \
		${WRKSRC}/google_compute_engine/instance_setup/instance_config.py \
		${WRKSRC}/google_compute_engine/metadata_scripts/script_executor.py \
		${WRKSRC}/google_compute_engine/network_setup/network_setup.py

.include <bsd.port.mk>
