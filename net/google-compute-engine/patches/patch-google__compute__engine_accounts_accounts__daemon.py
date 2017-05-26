--- google_compute_engine/accounts/accounts_daemon.py.orig	2017-05-14 18:25:32 UTC
+++ google_compute_engine/accounts/accounts_daemon.py
@@ -27,7 +27,7 @@
 from google_compute_engine import metadata_watcher
 from google_compute_engine.accounts import accounts_utils
 
-LOCKFILE = '/var/lock/google_accounts.lock'
+LOCKFILE = '/var/spool/lock/google_accounts.lock'
 
 
 class AccountsDaemon(object):
