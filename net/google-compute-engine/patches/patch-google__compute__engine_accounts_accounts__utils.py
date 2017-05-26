--- google_compute_engine/accounts/accounts_utils.py.orig	2017-05-14 18:25:32 UTC
+++ google_compute_engine/accounts/accounts_utils.py
@@ -43,8 +43,8 @@
     """
     self.logger = logger
     self.google_sudoers_group = 'google-sudoers'
-    self.google_sudoers_file = '/etc/sudoers.d/google_sudoers'
-    self.google_users_dir = '/var/lib/google'
+    self.google_sudoers_file = '%%PREFIX%%/etc/sudoers.d/google_sudoers'
+    self.google_users_dir = '%%PREFIX%%/var/lib/google'
     self.google_users_file = os.path.join(self.google_users_dir, 'google_users')
 
     self._CreateSudoersGroup()
@@ -71,7 +71,7 @@
     """Create a Linux group for Google added sudo user accounts."""
     if not self._GetGroup(self.google_sudoers_group):
       try:
-        subprocess.check_call(['groupadd', self.google_sudoers_group])
+        subprocess.check_call(['pw', 'groupadd', self.google_sudoers_group])
       except subprocess.CalledProcessError as e:
         self.logger.warning('Could not create the sudoers group. %s.', str(e))
 
@@ -126,7 +126,7 @@
     #
     # To solve the issue, make the password '*' which is also recognized
     # as locked but does not prevent SSH login.
-    command = ['useradd', '-m', '-s', '/bin/bash', '-p', '*', user]
+    command = ['pw', 'useradd', user, '-m']
     try:
       subprocess.check_call(command)
     except subprocess.CalledProcessError as e:
@@ -148,7 +148,7 @@
     """
     groups = ','.join(groups)
     self.logger.debug('Updating user %s with groups %s.', user, groups)
-    command = ['usermod', '-G', groups, user]
+    command = ['pw', 'usermod', user, '-G', groups]
     try:
       subprocess.check_call(command)
     except subprocess.CalledProcessError as e:
@@ -317,7 +317,7 @@
     """
     self.logger.info('Removing user %s.', user)
     if self.remove:
-      command = ['userdel', '-r', user]
+      command = ['pw', 'userdel', user, '-r']
       try:
         subprocess.check_call(command)
       except subprocess.CalledProcessError as e:
