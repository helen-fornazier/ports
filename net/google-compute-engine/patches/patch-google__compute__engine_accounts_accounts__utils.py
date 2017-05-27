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
@@ -126,7 +126,7 @@
     #
     # To solve the issue, make the password '*' which is also recognized
     # as locked but does not prevent SSH login.
-    command = ['useradd', '-m', '-s', '/bin/bash', '-p', '*', user]
+    command = ['useradd', '-m', user]
     try:
       subprocess.check_call(command)
     except subprocess.CalledProcessError as e:
