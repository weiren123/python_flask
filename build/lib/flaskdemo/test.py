# -*- coding:utf-8 -*-
import os
path = "D:\\workspace\\pythondemo\\images\\"
new_path = "D:\\workspace\\pythondemo\\new_images\\"
for file in os.listdir(path):
    if os.path.isfile(os.path.join(path, file)) == True:
        if file.find('.jpg') < 0:
            print("file")
        else:
            print(file.encode())
            new_name =file.replace(".jpg_",".jpg")
            os.rename(os.path.join(path, file), os.path.join(new_path, new_name))