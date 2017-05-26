--- google_compute_engine/boto/compute_auth.py.orig	2017-05-14 18:25:32 UTC
+++ google_compute_engine/boto/compute_auth.py
@@ -29,7 +29,7 @@
 class ComputeAuth(auth_handler.AuthHandler):
   """Google Compute service account auth handler.
 
-  The boto library reads the system config file (/etc/boto.cfg) and looks
+  The boto library reads the system config file (%%PREFIX%%/etc/boto.cfg) and looks
   at a config value called 'plugin_directory'. It then loads the Python
   files and find classes derived from boto.auth_handler.AuthHandler.
   """
