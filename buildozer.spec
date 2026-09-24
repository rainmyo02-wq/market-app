[app]
title = Shop Zone
package.name = shopzone
package.domain = org.test
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,html,css,js
version = 0.1

# Requirements (Python3.11 သို့မဟုတ် Kivy သာ သတ်မှတ်မည်)
requirements = python3,kivy

orientation = portrait
fullscreen = 0
android.permissions = INTERNET

# SDK, NDK & API Settings
android.api = 33
android.minapi = 21
android.ndk = 25b
android.accept_sdk_license = True
android.archs = arm64-v8a

[buildozer]
log_level = 2
warn_on_root = 1
