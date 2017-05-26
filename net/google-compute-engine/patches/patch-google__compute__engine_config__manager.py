--- google_compute_engine/config_manager.py.orig	2017-05-14 18:25:32 UTC
+++ google_compute_engine/config_manager.py
@@ -21,7 +21,7 @@
 from google_compute_engine import file_utils
 from google_compute_engine.compat import parser
 
-CONFIG = '/etc/default/instance_configs.cfg'
+CONFIG = '%%PREFIX%%/etc/instance_configs.cfg'
 
 
 class ConfigManager(object):
@@ -101,7 +101,7 @@
     """
     config_file = config_file or self.config_file
     config_name = os.path.splitext(os.path.basename(config_file))[0]
-    config_lock = '/var/lock/google_%s.lock' % config_name
+    config_lock = '/var/spool/lock/google_%s.lock' % config_name
     with file_utils.LockFile(config_lock):
       with open(config_file, 'w') as config_fp:
         if self.config_header:
