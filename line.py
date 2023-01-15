import cv2
import numpy as np

# Load the image and convert it to grayscale
image = cv2.imread('image.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Find the edges in the image using Canny edge detection
edged = cv2.Canny(gray, 50, 100)

# Find the contours in the edged image
contours, _ = cv2.findContours(edged, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

# Draw the contours on the image in white
cv2.drawContours(image, contours, -1, (255, 255, 255), 3)  

# Show the image
cv2.imshow("Contours", image)
cv2.waitKey(0)
cv2.destroyAllWindows()