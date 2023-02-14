import time
import cv2

class ImageDifference():

    def getDifference(self,image1,image2):
        image_difference = cv2.absdiff(image1,image2)
        difference = cv2.sumElems(image_difference)[0]
        return difference


    def __init__(self,reference_image,threshold,timerlevel):
        self.reference_image = reference_image
        self.threshold = threshold
        self.timerlevel = timerlevel
        self.last_time = time.now()

    def difference(self,frame):
        image1 = cv2.cvtColor(self.reference_image,cv2.COLOR_BGR2GRAY)
        image2 = cv2.cvtColor(self.reference_image,cv2.COLOR_BGR2GRAY)
        diff = self.getDifference(image1,image2)
        if(diff>self.threshold):
            return True
        else:
            return False
    
    def getTimeDifference(self):
        now_time = time.time()
        time_diff = now_time - self.last_time
        if(time_diff>self.timerlevel):
            return True
        else:
            return False
        
    def set_last_time(self):
        self.last_time = time.now()