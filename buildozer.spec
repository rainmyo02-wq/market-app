[app]

title = Shop Zone
package.name = shopzone
package.domain = org.test
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,html,css,js
version = 0.1

requirements = python3,kivy,openssl,requests,pillow,certifi

orientation = portrait
fullscreen = 0
android.permissions = INTERNET

# SDK, NDK & API Settings (API 33 သို့ ပြောင်းထားပါသည်)
android.api = 33
android.minapi = 21
android.ndk = 25b
android.accept_sdk_license = True
android.archs = arm64-v8a

# python-for-android ၏ အသစ်ဆုံး develop branch ကို သုံးရန်
p4a.branch = develop

[buildozer]

log_level = 2
warn_on_root = 1
