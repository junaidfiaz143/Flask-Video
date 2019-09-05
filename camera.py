import cv2

class VideoCamera(object):
    def __init__(self):
        self.video = cv2.VideoCapture(0)
        # self.video = cv2.VideoCapture("Jack_Reacher.mkv")

    def __del__(self):
        self.video.release()

    def get_frame(self):
        success, image = self.video.read()
        # We are using Motion JPEG, but OpenCV defaults to capture raw images,
        # so we must encode it into JPEG or PNG in order to correctly display the
        # video stream.

        # image = cv2.flip(image, 1)
        ret, jpeg = cv2.imencode('.png', image)
        return jpeg.tobytes()