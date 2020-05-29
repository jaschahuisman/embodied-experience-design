import cv2

cap = cv2.VideoCapture(0)
cv2.namedWindow("Test")

img_counter = 0

while True:
    ret, frame = cap.read()

    # Error handling
    if not ret:
        print("failed to grab frame")
        break

    # Show the webcam frame
    cv2.imshow("test", frame)

    # Waitkey
    k = cv2.waitKey(1)

    # Escape – Exit
    if k % 256 == 27:
        print("Escape hit, closing...")
        break
    elif k % 256 == 32:
        img_name = "opencv_frame{}.png".format(img_counter)
        cv2.imwrite(img_name, frame)
        print("{} written!".format(img_name))
        img_counter += 1

cap.release()
cv2.destroyAllWindows()
