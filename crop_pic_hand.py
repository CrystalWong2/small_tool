

# -*- coding:utf-8 -*-

import cv2
import numpy as np
import os
import sys

def file_exist(full_filename):
    
    if os.path.exists(full_filename):
        pass
    else:
        print("图片不存在")
        sys.exit(0)

class UseCv:
    def __init__(self):
        self.path = 'H:\\test_similarity\\test_data\\2.png'
    

    def cut(self):
        img = cv2.imread(self.path, flags=cv2.IMREAD_COLOR)
        file_exist(self.path)
        bbox = cv2.selectROI(img, False)

        #bbox[x_min,y_min,w,h]
        print(str(bbox[0]) + " " +str(bbox[1]) + " "+str(bbox[2]) + " "+str(bbox[3]) + " ")
        bbox_int = np.zeros((2,),dtype=np.int)


        if bbox[3] % 8 != 0:
            
            h = (bbox[3] // 8 + 1) * 8

            bbox_int[1] = (bbox[1]-( h -bbox[3])// 2)


        if bbox[2] % 8 != 0:
            w = (bbox[2] // 8 + 1) * 8
            bbox_int[0] = (bbox[0]-( w -bbox[2])// 2)
     

        cut = img[bbox_int[1]:bbox_int[1]+h, bbox_int[0]:bbox_int[0]+w]
        cv2.imwrite('20.bmp', cut)


if __name__ == '__main__':
    UseCv().cut()
