import cv2

image = cv2.imread("image.jpg")

gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) # 이미지를 그레이 컬러로 변경

resized_image = cv2.resize(gray_image, (1000, 1000)) # 이미지 크기를 조정

cv2.imwrite("gray_image.jpg", resized_image) # 그레이 컬러로 변경된 이미지를 파일에 저장

cv2.imshow("Image", resized_image)
cv2.waitKey(0)