import argparse
import cv2
import time
from datetime import datetime
import os


def getFileName():
    now = datetime.now()
    dt_value = now.strftime("%d/%m/%Y %H:%M%S")
    return dt_value


def run(vsource = 0,outputname = "output"):

    cap = cv2.VideoCapture(vsource)
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    fps = int(cap.get(cv2.CAP_PROP_FPS))
    fourcc = cv2.VideoWriter_fourcc('P','I','M','1')
    outputname = getFileName() if outputname == "output" else outputname
    video_writer = cv2.VideoWriter(os.path.join("Recordings","{}.avi".format(outputname)),fourcc,fps,(width,height))
    

    while cap.isOpened():
        ret, frame = cap.read()





def parse_opt():
    parser = argparse.ArgumentParser()
    parser.add_argument("--vsource",nargs= '+',type= int,help= "Enter the Video camara value")
    parser.add_argument("--outputname",default= "output",help= "Enter the name of the file name ")
    opt = parser.parse_args()
    return opt

def main(opt):
    run(**(vars(opt)))


if __name__ == "__main__":
    opt = parse_opt()
    main(opt)