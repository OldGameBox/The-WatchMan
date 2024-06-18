import cv2

camera = cv2.VideoCapture(0)


def start_camera():
    while True:
        # Capture the video frame
        # by frame
        ret, frame = camera.read()

        # Display the resulting frame
        cv2.imshow('frame', frame)

        # the 'q' button is set as the
        # quitting button you may use any
        # desired button of your choice
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # After the loop release the cap object
    camera.release()
    # Destroy all the windows
    cv2.destroyAllWindows()


def get_image_from_camera():
    ret, frame = camera.read()

    if ret:
        cv2.imshow("GeeksForGeeks", frame)
        cv2.imwrite('captured_image.jpg', frame)

        cv2.waitKey(0)

        cv2.destroyAllWindows()


if __name__ == "__main__":
    pass
