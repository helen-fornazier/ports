--- google_compute_engine/accounts/accounts_utils.py.orig	2017-05-14 18:25:32 UTC
+++ google_compute_engine/accounts/accounts_utils.py
@@ -43,7 +43,10 @@
     """
     self.logger = logger
     self.google_sudoers_group = 'google-sudoers'
-    self.google_sudoers_file = '/etc/sudoers.d/google_sudoers'
+    if os.path.exists('/etc/sudoers.d'):
+      self.google_sudoers_file = '/etc/sudoers.d/google_sudoers'
+    else:
+      self.google_sudoers_file = '/etc/sudoers'
     self.google_users_dir = '/var/lib/google'
     self.google_users_file = os.path.join(self.google_users_dir, 'google_users')
 
@@ -75,17 +78,23 @@
       except subprocess.CalledProcessError as e:
         self.logger.warning('Could not create the sudoers group. %s.', str(e))
 
-    if not os.path.exists(self.google_sudoers_file):
-      try:
-        with open(self.google_sudoers_file, 'w') as group:
-          message = '%{0} ALL=(ALL:ALL) NOPASSWD:ALL'.format(
-              self.google_sudoers_group)
-          group.write(message)
-      except IOError as e:
-        self.logger.error(
-            'Could not write sudoers file. %s. %s',
-            self.google_sudoers_file, str(e))
-        return
+    try:
+      with open(self.google_sudoers_file, 'a+') as group:
+        """Check if the group is already in the sudoers file"""
+        found = False
+        message = '%{0} ALL=(ALL:ALL) NOPASSWD:ALL'.format(
+            self.google_sudoers_group)
+        for line in group:
+          if message in line:
+            found = True
+            break
+        if not found:
+          group.write('\n' + message)
+    except IOError as e:
+      self.logger.error(
+          'Could not write sudoers file. %s. %s',
+          self.google_sudoers_file, str(e))
+      return
 
     file_utils.SetPermissions(
         self.google_sudoers_file, mode=0o440, uid=0, gid=0)
@@ -126,7 +135,7 @@
     #
     # To solve the issue, make the password '*' which is also recognized
     # as locked but does not prevent SSH login.
-    command = ['useradd', '-m', '-s', '/bin/bash', '-p', '*', user]
+    command = ['useradd', '-m', user]
     try:
       subprocess.check_call(command)
     except subprocess.CalledProcessError as e:
