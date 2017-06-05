--- google_compute_engine/instance_setup/instance_setup.py.orig	2017-05-14 18:25:32 UTC
+++ google_compute_engine/instance_setup/instance_setup.py
@@ -119,16 +119,16 @@
     """Initialize the SSH daemon."""
     # Exit as early as possible.
     # Instance setup systemd scripts block sshd from starting.
-    if os.path.exists('/bin/systemctl'):
+    if os.path.exists('%%PREFIX%%/bin/systemctl'):
       return
-    elif (os.path.exists('/etc/init.d/ssh') or
-          os.path.exists('/etc/init/ssh.conf')):
-      subprocess.call(['service', 'ssh', 'start'])
-      subprocess.call(['service', 'ssh', 'reload'])
-    elif (os.path.exists('/etc/init.d/sshd') or
-          os.path.exists('/etc/init/sshd.conf')):
-      subprocess.call(['service', 'sshd', 'start'])
-      subprocess.call(['service', 'sshd', 'reload'])
+    elif (os.path.exists('/etc/rc.d/ssh') or
+          os.path.exists('/etc/rc/ssh.conf')):
+      subprocess.call(['/etc/rc.d/ssh', 'start'])
+      subprocess.call(['/etc/rc.d/ssh', 'reload'])
+    elif (os.path.exists('/etc/rc.d/sshd') or
+          os.path.exists('/etc/rc/sshd.conf')):
+      subprocess.call(['/etc/rc.d/sshd', 'start'])
+      subprocess.call(['/etc/rc.d/sshd', 'reload'])
 
   def _SetSshHostKeys(self):
     """Regenerates SSH host keys when the VM is restarted with a new IP address.
