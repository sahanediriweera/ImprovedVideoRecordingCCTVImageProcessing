import argparse
import cv2
from datetime import datetime
import os
from PixelImageDifference import ImagePixelDifference
from HistogramImageDifference import ImageHistogramDifference
from SafetyDetection import fireDetection,smokeDetection


def get_Video_Capture_and_Write(outputname):
    outputname = getFileName() if outputname == "output" else outputname
    fourcc = cv2.VideoWriter_fourcc(*'XVID') 
    video_writer = cv2.VideoWriter("output.avi", fourcc, 20.0, (640, 480))
    cap = cv2.VideoCapture(0)
    return cap,video_writer


def getFileName():
    now = datetime.now()
    dt_value = now.strftime("%d/%m/%Y %H:%M%S")
    return dt_value

def process_video(algorithm,outputname,threshold,timerlevel,reference_image,video_link):
    if(algorithm == "historgram"):
        IDif = ImageHistogramDifference(reference_image,threshold=float(threshold[0]),timerlevel=timerlevel)
    else:
        IDif = ImagePixelDifference(reference_image,threshold=float(threshold[0]),timerlevel=timerlevel)
    fourcc = cv2.VideoWriter_fourcc(*'XVID')  # Choose the codec (XVID for .avi format)
    video_writer = cv2.VideoWriter("{}.avi".format(outputname), fourcc, 20.0, (640, 480))  # Create the VideoWriter object
    cap = cv2.VideoCapture(video_link)
    frame_count = 0
    the_actual_frame_count = 0

    try:
        while cap.isOpened():
        
            ret, frame = cap.read()
            cv2.imshow('frame', frame)
            print(f"The actual frame count {the_actual_frame_count} the current frame count {frame_count}")
            if IDif.difference(frame=frame):
                video_writer.write(frame)
                frame_count +=1
            the_actual_frame_count+=1
            if cv2.waitKey(10) & 0xFF == ord('q'):
                break
        cap.release()
        video_writer.release()
        cv2.destroyAllWindows()
    except Exception as e:
        print()

def run(vsource = 0,outputname = "output",threshold = 1000,timerlevel = 60,reference_image = "",video_link="",algorithm="pixel"):
    threshold = float(threshold[0])
    timerlevel = int(timerlevel[0])
    if(video_link == "" ):
        if(algorithm == "historgram"):
            IDif = ImageHistogramDifference(reference_image,threshold=threshold,timerlevel=timerlevel)
        else:
            IDif = ImagePixelDifference(reference_image,threshold=threshold,timerlevel=timerlevel)
        fourcc = cv2.VideoWriter_fourcc(*'XVID')  # Choose the codec (XVID for .avi format)
        video_writer = cv2.VideoWriter("{}.avi".format(outputname), fourcc, 20.0, (640, 480))  # Create the VideoWriter object
        cap = cv2.VideoCapture(vsource)
        frame_count = 0
        the_actual_frame_count = 0
        try:
            while cap.isOpened():
                ret, frame = cap.read()
                cv2.imshow('frame', frame)
                print(f"The actual frame count {the_actual_frame_count} the current frame count {frame_count}")
                if IDif.difference(frame=frame):
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
    else:
        process_video(algorithm,outputname,threshold,timerlevel,reference_image,video_link)

def parse_opt():
    parser = argparse.ArgumentParser()
    parser.add_argument("--vsource",nargs= '+',type= int,default=0,help= "Enter the Video camara value")
    parser.add_argument("--outputname",default= "output",help= "Enter the name of the file name ")
    parser.add_argument("--threshold",nargs= '+',type= float,default=1000.0,help= "Enter the threshold value")
    parser.add_argument("--timerlevel",nargs= '+',type=int,default=60,help= "Enter the timer level to compare")
    parser.add_argument("--reference_image",default="",help="Enter the address of the reference image")
    parser.add_argument("--video_link",default="",help="Enter Video Addrress")
    parser.add_argument("--algorithm",default="pixel",help="Enter suitable algorithm")
    opt = parser.parse_args()
    return opt

def main(opt):
    run(**(vars(opt)))


if __name__ == "__main__":
    opt = parse_opt()
    main(opt)