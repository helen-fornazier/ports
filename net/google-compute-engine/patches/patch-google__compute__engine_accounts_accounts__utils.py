--- google_compute_engine/accounts/accounts_utils.py.orig	2017-05-14 18:25:32 UTC
+++ google_compute_engine/accounts/accounts_utils.py
@@ -126,7 +126,7 @@
     #
     # To solve the issue, make the password '*' which is also recognized
     # as locked but does not prevent SSH login.
-    command = ['useradd', '-m', '-s', '/bin/bash', '-p', '*', user]
+    command = ['useradd', '-m', user]
     try:
       subprocess.check_call(command)
     except subprocess.CalledProcessError as e:
