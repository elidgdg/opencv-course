import os
import cv2 as cv
import numpy as np

people = []
for i in os.listdir('/home/elijah/repos/opencv-course/Resources/Faces/train'):
    people.append(i)

DIR = '/home/elijah/repos/opencv-course/Resources/Faces/train'

def create_train():
    