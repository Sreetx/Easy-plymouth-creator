import glob
import os, re
name = "chara"
image = "/home/programmer/chara"
png_files = glob.glob(os.path.join(image, '*.png'))
tota = len(png_files)
print(tota)
