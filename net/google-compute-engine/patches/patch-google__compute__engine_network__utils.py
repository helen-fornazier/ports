--- /tmp/KWpq5X_network_utils.py	2017-05-19 08:44:58.717188081 -0300
+++ google_compute_engine/network_utils.py	2017-05-19 08:44:55.457204773 -0300
@@ -17,6 +17,7 @@
 
 import logging
 import os
+import netifaces
 
 
 class NetworkUtils(object):
@@ -38,14 +39,12 @@
       dict, string MAC addresses mapped to the string network interface name.
     """
     interfaces = {}
-    for interface in os.listdir('/sys/class/net'):
-      try:
-        mac_address = open(
-            '/sys/class/net/%s/address' % interface).read().strip()
-      except (IOError, OSError) as e:
-        message = 'Unable to determine MAC address for %s. %s.'
-        self.logger.warning(message, interface, str(e))
-      else:
+    for interface in netifaces.interfaces():
+        mac_address = netifaces.ifaddresses(interface)[netifaces.AF_LINK][0]['addr']
+        if  mac_address == interface:
+            message = 'Unable to determine MAC address for %s.'
+            self.logger.warning(message, interface)
+            continue
         interfaces[mac_address] = interface
     return interfaces
 
