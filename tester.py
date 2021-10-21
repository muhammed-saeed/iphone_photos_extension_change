import os
file_name =""

# for file in os.listdir():
#     # Check whether file is in text format or not

#     if file.endswith(('.png', '.jpg', '.jpeg')):
#         file_path = f"{path}\{file}"
#         # renamee is the file getting renamed, pre is the part of file name before extension and ext is current extension
# #         pre, ext = os.path.splitext(renamee)
# #         os.rename(renamee, pre + new_extension)
# #         # call read text file function
# #         read_text_file(file_path)
#         print(file_path)


import glob
# All files ending with .txt

print(glob.glob("/media/muhammed/New Volume/00/*.jpg")) 
print(glob.glob("/media/muhammed/New Volume/00/*.png"))
print(glob.glob("/media/muhammed/New Volume/00/*.jpeg"))
print(glob.glob("/home/muhammed/Desktop/fatimas_files/*.jpg"))
print(glob.glob("/home/muhammed/Desktop/fatimas_files/*.jpeg"))
# All files ending with .txt with depth of 2 folder
#print(glob.glob("/home/adam/*/*.txt")) 
from os import listdir
from os.path import isfile, join
mypath="/home/muhammed/Desktop/fatimas_files/"
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
# m.lower().endswith(('.png', '.jpg', '.jpeg'))
print(onlyfiles)