[app]

# (str) Title of your application
title = Shop Zone

# (str) Package name
package.name = shopzone

# (str) Package domain (needed for android/ios packaging)
package.domain = org.test

# (str) Source code where the main.py live
source.dir = .

# (list) Source files to include (process only files with these extensions)
source.include_exts = py,png,jpg,kv,atlas,html,css,js

# (list) Application version
version = 0.1

# (list) Application requirements
# Note: Kivy version နဲ့ pillow စာလုံးပေါင်း အမှန်အတိုင်း သတ်မှတ်ထားပါသည်
requirements = python3,kivy==2.3.0,openssl,requests,pillow,certifi

# (str) Supported orientation (one of landscape, sensorLandscape, portrait or all)
orientation = portrait

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 0

# (list) Permissions
android.permissions = INTERNET

# (int) Target Android API
android.api = 33

# (int) Minimum API supported
android.minapi = 21

# (str) Android NDK version
android.ndk = 25b

# (int) Android NDK API level
android.ndk_api = 21

# (bool) Accept SDK license automatically
android.accept_sdk_license = True

# (list) The Android archs to build for
android.archs = arm64-v8a

# (str) python-for-android branch to use
# develop branch သည် SDL2 နှင့် FreeType C-library build error များကို ဖြေရှင်းပေးထားပါသည်
p4a.branch = develop

[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) Display warning if buildozer is run as root (0 = disable, 1 = enable)
warn_on_root = 1
