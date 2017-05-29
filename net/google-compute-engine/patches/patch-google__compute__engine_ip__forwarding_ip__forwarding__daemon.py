--- /tmp/cME1JV_ip_forwarding_daemon.py	2017-05-29 18:03:51.684092653 -0300
+++ google_compute_engine/ip_forwarding/ip_forwarding_daemon.py	2017-05-29 18:01:32.836823451 -0300
@@ -38,7 +38,7 @@
 
 from google_compute_engine.ip_forwarding import ip_forwarding_utils
 
-LOCKFILE = '/var/lock/google_ip_forwarding.lock'
+LOCKFILE = '/var/spool/lock/google_ip_forwarding.lock'
 
 
 class IpForwardingDaemon(object):
@@ -130,17 +130,17 @@
     Args:
       result: dict, the metadata response with the new network interfaces.
     """
+    ip_addresses = []
     for network_interface in result:
       mac_address = network_interface.get('mac')
       interface = self.network_utils.GetNetworkInterface(mac_address)
-      ip_addresses = []
       if interface:
         ip_addresses.extend(network_interface.get('forwardedIps', []))
         ip_addresses.extend(network_interface.get('ipAliases', []))
-        self._HandleForwardedIps(ip_addresses, interface)
       else:
         message = 'Network interface not found for MAC address: %s.'
         self.logger.warning(message, mac_address)
+    self._HandleForwardedIps(ip_addresses, 'lo' + self.ip_forwarding_utils.proto_id)
 
 
 def main():
