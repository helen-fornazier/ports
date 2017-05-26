--- google_compute_engine/metadata_scripts/script_executor.py.orig	2017-05-14 18:25:32 UTC
+++ google_compute_engine/metadata_scripts/script_executor.py
@@ -50,7 +50,7 @@
       metadata_script: string, the file location of an executable script.
     """
     process = subprocess.Popen(
-        metadata_script, shell=True, executable='/bin/bash',
+        metadata_script, shell=True, executable='%%PREFIX%%/bin/bash',
         stderr=subprocess.STDOUT, stdout=subprocess.PIPE)
     while True:
       for line in iter(process.stdout.readline, b''):
