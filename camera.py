import cv2

class VideoCamera(object):
    def __init__(self):
        # self.video = cv2.VideoCapture(0)
        # self.video = cv2.VideoCapture("Jack_Reacher.mkv")
        self.video = cv2.VideoCapture("school.mp4")

    def __del__(self):
        self.video.release()

    def get_frame(self):
        success, image = self.video.read()


        # image = cv2.flip(image, 1)
        ret, jpeg = cv2.imencode('.png', image)
        return jpeg.tobytes()