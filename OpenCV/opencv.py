import cv2

cap = cv2.VideoCapture(0)

ret, frame = cap.read()

if ret:

    cv2.imshow("GeeksForGeeks", frame)
    cv2.imwrite('captured_image.jpg', frame)

    cv2.waitKey(0)

    cv2.destroyAllWindows()