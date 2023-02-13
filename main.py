import argparse
import cv2
import time
from datetime import datetime
import os


def getFileName():
    now = datetime.now()
    dt_value = now.strftime("%d/%m/%Y %H:%M%S")
    return dt_value


def run(vsource = 0,outputname = "output",threshold = 1000):

    cap = cv2.VideoCapture(vsource)
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    fps = int(cap.get(cv2.CAP_PROP_FPS))
    fourcc = cv2.VideoWriter_fourcc('P','I','M','1')
    outputname = getFileName() if outputname == "output" else outputname
    video_writer = cv2.VideoWriter(os.path.join("Recordings","{}.avi".format(outputname)),fourcc,fps,(width,height))


    while cap.isOpened():
        try:
            ret, frame = cap.read()
            if(True):
                video_writer.write(frame)
            if((True) OR (True)):
                print(True)
                /**/

            if cv2.waitKey(10) & 0xFF == ord('q'):
                break
        except e:
            break




def parse_opt():
    parser = argparse.ArgumentParser()
    parser.add_argument("--vsource",nargs= '+',type= int,help= "Enter the Video camara value")
    parser.add_argument("--outputname",default= "output",help= "Enter the name of the file name ")
    parser.add_argument("--threshold",nargs= '+',type= int,help= "Enter the threshold value")
    opt = parser.parse_args()
    return opt

def main(opt):
    run(**(vars(opt)))


if __name__ == "__main__":
    opt = parse_opt()
    main(opt)