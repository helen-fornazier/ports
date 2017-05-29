--- /tmp/2QYr0S_setup.py	2017-05-29 18:03:51.636092903 -0300
+++ setup.py	2017-05-29 17:58:00.489973307 -0300
@@ -30,7 +30,6 @@
     long_description='Google Compute Engine guest environment.',
     name='google-compute-engine',
     packages=setuptools.find_packages(),
-    scripts=glob.glob('scripts/*'),
     url='https://github.com/GoogleCloudPlatform/compute-image-packages',
     version='2.3.6',
     # Entry points create scripts in /usr/bin that call a function.
