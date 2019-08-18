from time import sleep

import cv2
import numpy as np
import pickle

from RealSenseCamera import RealSenseCamera

file = open('real_record.pkl', 'rb')
frames = pickle.load(file)
file.close()

for frame in frames:
    color_image = frame['color_image']
    depth_image = frame['depth_image']
    cv2.imshow('color', color_image)
    print(' depth at pixel (250,375) : ', depth_image[250][375] / 1000)
    cv2.waitKey(1)
    sleep(0.03)


