import cv2

class Camera:
    def __init__(self):
        self.camera = cv2.VideoCapture(0)

    def frames(self):
        if not self.camera.isOpened():
            raise RuntimeError('Could not start camera.')

        while True:
            # read current frame
            _, img = self.camera.read()
            print()

            # encode as a jpeg image and return it
            yield cv2.imencode('.jpg', img)[1].tobytes()