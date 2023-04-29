import argparse
import cv2
from datetime import datetime
import os
from ImageDifference import ImageDifference
from SafetyDetection import fireDetection,smokeDetection


def get_Video_Capture_and_Write(outputname):
    outputname = getFileName() if outputname == "output" else outputname
    fourcc = cv2.VideoWriter_fourcc(*'XVID')  # Choose the codec (XVID for .avi format)
    video_writer = cv2.VideoWriter("output.avi", fourcc, 20.0, (640, 480))  # Create the VideoWriter object
    cap = cv2.VideoCapture(0)
    return cap,video_writer


def getFileName():
    now = datetime.now()
    dt_value = now.strftime("%d/%m/%Y %H:%M%S")
    return dt_value


def run(vsource = 0,outputname = "output",threshold = 1000,timerlevel = 60,reference_image = ""):
    IDif = ImageDifference(reference_image,threshold=float(threshold[0]),timerlevel=timerlevel)
    fourcc = cv2.VideoWriter_fourcc(*'XVID')  # Choose the codec (XVID for .avi format)
    video_writer = cv2.VideoWriter("output.avi", fourcc, 20.0, (640, 480))  # Create the VideoWriter object
    cap = cv2.VideoCapture(vsource)
    frame_count = 0
    the_actual_frame_count = 0
    try:
        while cap.isOpened():
        
            ret, frame = cap.read()
            cv2.imshow('frame', frame)
            print(f"The actual frame count {the_actual_frame_count} the current frame count {frame_count}")
            if IDif.difference(frame):
                video_writer.write(frame)
                frame_count +=1
            the_actual_frame_count+=1
            if cv2.waitKey(10) & 0xFF == ord('q'):
                break
        cap.release()
        video_writer.release()
        cv2.destroyAllWindows()
    except Exception as e:
        print(e)

def parse_opt():
    parser = argparse.ArgumentParser()
    parser.add_argument("--vsource",nargs= '+',type= int,default=0,help= "Enter the Video camara value")
    parser.add_argument("--outputname",default= "output",help= "Enter the name of the file name ")
    parser.add_argument("--threshold",nargs= '+',type= float,default=1000,help= "Enter the threshold value")
    parser.add_argument("--timerlevel",nargs= '+',type=int,default=60,help= "Enter the timer level to compare")
    parser.add_argument("--reference_image",default="",help="Enter the address of the reference image")
    opt = parser.parse_args()
    return opt

def main(opt):
    run(**(vars(opt)))


if __name__ == "__main__":
    opt = parse_opt()
    main(opt)