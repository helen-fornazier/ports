--- build_packages.sh.orig	2017-05-14 18:25:32 UTC
+++ build_packages.sh
@@ -49,9 +49,9 @@ function build_distro() {
     --maintainer 'gc-team@google.com' \
     --name "${name}" \
     --no-python-fix-name \
-    --python-install-bin '/usr/bin' \
+    --python-install-bin '%%PREFIX%%/bin' \
     --python-install-lib "${py_path}" \
-    --python-install-data "/usr/share/doc/${name}" \
+    --python-install-data "%%PREFIX%%/share/doc/${name}" \
     --rpm-dist "${distro}" \
     setup.py
 }
@@ -83,6 +83,9 @@ fi
 
 for build in "${BUILD[@]}"; do
   case "$build" in
+    freebsd) # FreeBSD
+      build_distro 'freebsd' 'dir' '%%PREFIX%%/lib/python2.7/site-packages'
+      ;;
     el6) # RHEL/CentOS 6
       build_distro 'el6' 'rpm' '/usr/lib/python2.6/site-packages'
       ;;
