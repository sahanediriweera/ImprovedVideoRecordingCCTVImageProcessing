import time
import cv2
from Difference import Difference

class ImageHistogramDifference(Difference):

    def capture_image(self):
        cap = cv2.VideoCapture(0)
        ret,frame = cap.read()
        cap.release()
        return frame

    def getCorrect_Reference_Image(self,reference_image):
        if(reference_image == ""):
            image = self.capture_image()
            return image
        else:
            return cv2.imread(reference_image)

    def getDifference(self,image1,image2):
        image_difference = cv2.absdiff(image1,image2)
        difference = cv2.sumElems(image_difference)[0]
        return difference

    def changeFrame(self,frame):
        self.reference_image = frame

    def __init__(self,reference_image,threshold,timerlevel):
        self.reference_image = self.getCorrect_Reference_Image(reference_image=reference_image)
        self.threshold = threshold
        self.timerlevel = timerlevel
        self.last_time = time.time()

    def pixel_difference(self,frame):
        image1 = cv2.cvtColor(self.reference_image,cv2.COLOR_BGR2GRAY)
        image2 = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        diff = self.getDifference(image1,image2)
        print(f"got difference {diff}, {self.threshold}")
        if(diff>self.threshold):
            if(self.getTimeDifference()):
                self.changeFrame(frame=frame)
            return True
        else:
            return False
    
    def getTimeDifference(self):
        now_time = time.time()
        time_diff = now_time - self.last_time
        if(time_diff>self.timerlevel):
            self.set_last_time()
            return True
        else:
            return False
        
    def set_last_time(self):
        self.last_time = time.time()

    # def ssi(self,frame):
    #     image1 = cv2.cvtColor(self.reference_image,cv2.COLOR_BGR2GRAY)
    #     image2 = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    #     diff = compare_ssim(image1,image2, multichannel=True)
    #     print(f"got difference {diff}, {self.threshold}")
    #     if(diff>self.threshold):
    #         if(self.getTimeDifference()):
    #             self.changeFrame(frame=frame)
    #         return True
    #     else:
    #         return False
        
    def difference(self,frame):
        image1 = cv2.cvtColor(self.reference_image,cv2.COLOR_BGR2GRAY)
        image2 = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        hist1 = cv2.calcHist([image1], [0], None, [256], [0, 256])
        hist2 = cv2.calcHist([image2], [0], None, [256], [0, 256])
        diff = cv2.compareHist(hist1, hist2, cv2.HISTCMP_BHATTACHARYYA)
        print(f"got difference {diff}, {self.threshold}")
        if(diff>self.threshold):
            if(self.getTimeDifference()):
                self.changeFrame(frame=frame)
            return True
        else:
            return False
        