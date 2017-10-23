# import the necessary packages
from collections import deque
import numpy as np
import argparse
import imutils
import cv2

def main():

    cv2.namedWindow("h264-stream", cv2.WINDOW_NORMAL)
    cv2.resizeWindow("h264-stream", 1280, 720)
    video = cv2.VideoCapture('tcp://192.168.2.5:9092')
    while True:
        ret, frame = video.read()
        if ret == True:
            cv2.imshow("h264-stream", frame)
            cv2.waitKey(1)
        else:
            break
    video.release()
    cv2.destroyAllWindows()


if __name__== "__main__":
    main()
