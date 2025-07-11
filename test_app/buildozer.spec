[app]
title = Tripeaks
package.name = Tripeakssolitaire 
package.domain = org.wasey
source.dir = .
source.include_exts = py,kv,png,jpg,jpeg,ttf,atlas
source.include_patterns = img/*.png, img/*.jpg, img/*.jpeg
version = 0.1
requirements = python,kivy,https://github.com/kivymd/KivyMD/archive/master.zip,materialyoucolor,exceptiongroup,asyncgui,asynckivy,android
orientation = portrait
fullscreen = 0
#android.permissions = INTERNET,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE
android.api = 33
android.minapi = 21
android.ndk_api = 21
android.archs = arm64-v8a, armeabi-v7a
android.allow_backup = True
# Optional UI polish
icon.filename = %(source.dir)s/img/icon.jpg
#presplash.filename = %(source.dir)s/img/presplash.png

[buildozer]
log_level = 2
warn_on_root = 1
