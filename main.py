import cv2
from tkinter import filedialog
from PIL import Image
from datetime import datetime

# ask the user to upload the file
file = filedialog.askopenfilename()
print(file)

# get only file name
file_name = file[file.rindex("/")+1:file.rindex(".")]

# now take the image from the file_path and open it with cv2
# it will now be saved as a numpy array.

a = cv2.imread(file)

# denoisfy the image
# a = cv2.fastNlMeansDenoisingColored(a, None, 10, 10, 7, 21)
# print("Deonisfying")

# loop on each pixel value of image on all three channels.
op = 1
total = a.shape
for i in total:
    op *= i

current = 0
for i, i_ in enumerate(a):
    for j, j_ in enumerate(i_):
        for k, k_ in enumerate(j_):
            current += 1
            tmp = a[i][j][k]
            if 2 <= tmp <= 5:
                a[i][j][k] = 255-tmp
            print("{} % complete".format(current/op*100))

print("Save file in which directory?")
save_dir = filedialog.askdirectory()
img = Image.fromarray(a)

# save in save_dir as img.jpeg
img.save(save_dir + "/" + file_name + "_img.jpeg")
