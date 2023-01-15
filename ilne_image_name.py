import cv2
import numpy as np

# Load the image and convert it to grayscale
image = cv2.imread('image.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

cv2.imwrite("ilne_image_name.jpg", gray)

# Detect edges using the Canny algorithm
edges = cv2.Canny(gray, 50, 100)

# Display the edges image using imshow
cv2.imshow('Edges', edges)
cv2.waitKey(0)
cv2.destroyAllWindows()

