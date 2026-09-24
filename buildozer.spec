[app]
title = Shop Zone
package.name = shopzone
package.domain = org.test
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,html,css,js
version = 0.1

# Requirements
requirements = python3,kivy

orientation = portrait
osx.python_version = 3
osx.kivy_version = 1.9.1

fullscreen = 0
android.permissions = INTERNET

# SDK, NDK & API Settings (Ubuntu 24.04/22.04 နှင့် ကိုက်ညီအောင် ပြင်ထားသည်)
android.api = 33
android.minapi = 21
android.ndk = 25b
android.ndk_api = 21
android.accept_sdk_license = True
android.archs = arm64-v8a, armeabi-v7a

[buildozer]
log_level = 2
warn_on_root = 1
