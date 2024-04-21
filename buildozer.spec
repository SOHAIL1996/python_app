[app]
title = JourneyPrayer
package.name = com.sorox.journeyprayer
package.domain = com.sorox
source.dir = .
source.include_exts = py,mp3
version = 0.1
requirements = python3,pygame

[buildozer]
# Set to "android" for Android builds
target = android

# Permissions
android.permissions = 

# Presplash
presplash.filename = %(source.dir)s/icon/elements.png
