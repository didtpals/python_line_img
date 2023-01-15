import cv2

image = cv2.imread("image.jpg")  # imred 옵션을 사용해서 이미지파일을 읽음

cv2.imshow("Image", image) # imshow 옵션를 사용해서 이미지를 표시해줌

cv2.waitKey(0) # wartkey 옵션을 사용해서 m/s 단위를 기준으로 입력한 m/s 동안 또는 X키나 누를 때까지 창을 표시할 수 있음
               # 인수에 0을 입력하면 X키를 누를 때까지 표시