--- /tmp/KWpq5X_network_utils.py	2017-05-19 08:44:58.717188081 -0300
+++ google_compute_engine/network_utils.py	2017-05-19 08:44:55.457204773 -0300
@@ -17,6 +17,7 @@
 
 import logging
 import os
+import subprocess
 
 
 class NetworkUtils(object):
@@ -37,16 +38,20 @@
     Returns:
       dict, string MAC addresses mapped to the string network interface name.
     """
+
     interfaces = {}
-    for interface in os.listdir('/sys/class/net'):
+    try:
+      interfaces_list = subprocess.check_output('ifconfig -l', shell=True)
+    except subprocess.CalledProcessError:
+        return interfaces
+    for interface in interfaces_list.split():
       try:
-        mac_address = open(
-            '/sys/class/net/%s/address' % interface).read().strip()
-      except (IOError, OSError) as e:
-        message = 'Unable to determine MAC address for %s. %s.'
-        self.logger.warning(message, interface, str(e))
+        mac_address = subprocess.check_output('ifconfig ' + interface + ' | grep -o -E "([[:xdigit:]]{1,2}:){5}[[:xdigit:]]{1,2}"', shell=True)
+      except subprocess.CalledProcessError:
+        message = 'Unable to determine MAC address for %s.'
+        self.logger.warning(message, interface)
       else:
-        interfaces[mac_address] = interface
+        interfaces[mac_address[:-1]] = interface
     return interfaces
 
   def GetNetworkInterface(self, mac_address):
