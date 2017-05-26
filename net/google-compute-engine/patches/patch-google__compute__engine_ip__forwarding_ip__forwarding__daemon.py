--- google_compute_engine/ip_forwarding/ip_forwarding_daemon.py.orig	2017-05-14 18:25:32 UTC
+++ google_compute_engine/ip_forwarding/ip_forwarding_daemon.py
@@ -38,7 +38,7 @@
 
 from google_compute_engine.ip_forwarding import ip_forwarding_utils
 
-LOCKFILE = '/var/lock/google_ip_forwarding.lock'
+LOCKFILE = '/var/spool/lock/google_ip_forwarding.lock'
 
 
 class IpForwardingDaemon(object):
