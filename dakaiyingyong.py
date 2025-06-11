import os
#os.system("adb shell dumpsys activity")
os.system("adb -s 192.168.31.52:5555 shell am start -n com.tencent.mm/com.tencent.mm.ui.LauncherUI")
#os.system("adb shell am start -n com.tencent.mm/com.tencent.mm.ui.LauncherUI")
#os.system("adb shell am start -n com.android.settings/com.android.settings.Settings")