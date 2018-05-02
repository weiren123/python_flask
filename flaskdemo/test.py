# -*- coding:utf-8 -*-
import os
import push_example
def changeImage():
    path = "D:\\workspace\\pythondemo\\images\\"
    new_path = "D:\\workspace\\pythondemo\\new_images\\"
    for file in os.listdir(path):
        if os.path.isfile(os.path.join(path, file)) == True:
            if file.find('.jpg') < 0:
                print("file")
            else:
                print(file.encode())
                new_name = file.replace(".jpg_", ".jpg")
                os.rename(os.path.join(path, file), os.path.join(new_path, new_name))
def analysisInfo():
     # currentPrice = ""
     univalent = 116
     changeUnivallent = 116
     # changePrice = ""
     # d_value = ""
     # priceType = False
     currentPrice = univalent * 3
     print("currentPrice:"+str(currentPrice))
     changePrice =changeUnivallent * 3
     print("changePrice:" + str(changePrice))
     if changeUnivallent > univalent:
         priceType = True
     else:
         priceType = False

     if priceType == True:
         d_value = abs(changePrice - currentPrice)
         print("↑d_value:" + str(d_value))
     else:
         d_value = abs(changePrice - currentPrice)
         print("↓d_value:" + str(d_value))
     if priceType == False and d_value == 0:
         print("→→→→→→→→→→→→→→")
         push_example.platfrom_msg()

#递归算法
def factorial(n):
    if n == 1:
        return 1  # 递归结束
    return n * factorial(n - 1)
if __name__ == '__main__':
    # changeImage()
    analysisInfo()