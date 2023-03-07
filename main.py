import os
os.system("clear")
try:
    from PIL import Image, ImageFilter
    print("["+"\x1b[32;1m"+"✔︎"+"\x1b[0m"+"] Successfully Imported PIL import")
except ImportError:
    os.system("python -m pip install --upgrade pip")
    os.system("pip3 install Pillow")
    print("["+"\x1b[32;1m"+"+"+"\x1b[0m"+"] Installed PIL import")
filename = input("Enter File Directory (Ex. C:\Documents\photos\sample.pdf / /Users/sh1d0re/Documents/photos/sample/pdf):\n>>> ")
img = Image.open(filename)
w, h, colors, resulttxt, num, prebrightness, resolution, a, b = img.size[0], img.size[1], [], "", 0, 0, int(input("Enter Resolution (Around 160 is reccomended):\n>>> ")), 0, 0
os.system("clear")
for c in range(resolution):
    for d in range(resolution):
        a, b, prebrightness = str(int(w/resolution)*d), str(int(h/resolution)*c), prebrightness + int(img.getpixel((int(a),int(b)))[0])+int(img.getpixel((int(a),int(b)))[1])+int(img.getpixel((int(a),int(b)))[2])/3
        if prebrightness//3 <= 5: resulttxt+=" "
        elif prebrightness//3 <= 20: resulttxt+="."
        elif prebrightness//3 <= 40: resulttxt+=":"
        elif prebrightness//3 <= 60: resulttxt+=";"
        elif prebrightness//3 <= 80: resulttxt+="^"
        elif prebrightness//3 <= 100: resulttxt+="-"
        elif prebrightness//3 <= 120: resulttxt+="~"
        elif prebrightness//3 <= 140: resulttxt+=">"
        elif prebrightness//3 <= 160: resulttxt+="+"
        elif prebrightness//3 <= 180: resulttxt+="*"
        elif prebrightness//3 <= 200: resulttxt+="%"
        elif prebrightness//3 <= 220: resulttxt+="¥"
        elif prebrightness//3 <= 240: resulttxt+="$"
        elif prebrightness//3 <= 245: resulttxt+="@"
        elif prebrightness//3 <= 255: resulttxt+="#"
        resulttxt+="  "
        prebrightness = 0
    resulttxt+="\n"   
print(resulttxt+"\n\n=========================\nPRINTED ASCII-ART\n=========================")
