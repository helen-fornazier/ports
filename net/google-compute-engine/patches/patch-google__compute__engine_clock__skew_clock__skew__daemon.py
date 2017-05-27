--- google_compute_engine/clock_skew/clock_skew_daemon.py.orig	2017-05-14 18:25:32 UTC
+++ google_compute_engine/clock_skew/clock_skew_daemon.py
@@ -24,7 +24,7 @@
 from google_compute_engine import logger
 from google_compute_engine import metadata_watcher
 
-LOCKFILE = '/var/lock/google_clock_skew.lock'
+LOCKFILE = '/var/spool/lock/google_clock_skew.lock'
 
 
 class ClockSkewDaemon(object):
@@ -58,9 +58,12 @@
       response: string, the metadata response with the new drift token value.
     """
     self.logger.info('Clock drift token has changed: %s.', response)
-    command = ['/sbin/hwclock', '--hctosys']
+
+    ntpd_inactive = subprocess.call(['/etc/rc.d/ntpd', 'status'])
     try:
-      subprocess.check_call(command)
+      if not ntpd_inactive: subprocess.check_call(['/etc/rc.d/ntpd', 'stop'])
+      subprocess.check_call('ntpdate `awk \'$1=="server" {print $2}\' /etc/ntp.conf`', shell=True)
+      if not ntpd_inactive: subprocess.check_call(['/etc/rc.d/ntpd', 'start'])
     except subprocess.CalledProcessError:
       self.logger.warning('Failed to sync system time with hardware clock.')
     else:
