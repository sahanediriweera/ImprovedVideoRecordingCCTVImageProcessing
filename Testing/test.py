import os
import cv2

import cv2

# Load the two images
img1 = cv2.imread("1.jpg")
img2 = cv2.imread("2.jpg")

# Convert images to grayscale
gray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

# Calculate the absolute difference between the two images
diff = cv2.absdiff(gray1, gray2)
print
# Compute the sum of the difference image
diff_sum = cv2.sumElems(diff)[0]
print(diff_sum)
# Define a threshold value
threshold = 1000

# Determine if there is a difference between the two images
is_different = diff_sum > threshold

print(is_different)

# Show the difference image
cv2.imshow("Difference", diff)
cv2.waitKey(0)
cv2.destroyAllWindows()