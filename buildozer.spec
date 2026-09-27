[app]
title = Shop Zone
package.name = shopzone
package.domain = org.test
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1
requirements = python3,kivy==2.3.0,kivymd==1.2.0,pillow==10.2.0,requests,pyjnius
orientation = portrait
android.permissions = INTERNET
android.api = 33
android.minapi = 21
android.ndk = 25b
android.accept_sdk_license = True
android.archs = arm64-v8a
android.release_artifact = apk

[buildozer]
log_level = 2
warn_on_root = 0
