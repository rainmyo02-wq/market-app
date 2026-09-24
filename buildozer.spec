[app]
title = Shop Zone
package.name = shopzone
package.domain = org.test
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,html,css,js
version = 0.1
requirements = python3,kivy

orientation = portrait
osx.python_version = 3
osx.kivy_version = 1.9.1

fullscreen = 0
android.permissions = INTERNET

# SDK & License သတ်မှတ်ချက်များ (License Error မတက်စေရန် ပြင်ထားသည်)
android.api = 31
android.minapi = 21
android.ndk = 25b
android.accept_sdk_license = True

[buildozer]
log_level = 2
warn_on_root = 1
