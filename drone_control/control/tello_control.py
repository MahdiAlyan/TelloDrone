from flask import Flask, Response
from djitellopy import tello
import cv2


class Drone(tello.Tello):
    super(tello.Tello)

    def __init__(self):
        super().__init__()
        self.me = tello.Tello()
        self.me.connect()
        self.me.streamon()

        self.x, self.y, self.z = 0, 0, 0  # Initial position
        self.speed = 0.5  # Adjust speed as necessary

    def generate_frames(self):
        while True:
            img = self.me.get_frame_read().frame
            img = cv2.resize(img, (640, 480))
            img = cv2.cvtColor(img, cv2.COLOR_RGB2BGRA)
            _, buffer = cv2.imencode('.jpg', img)

            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')


# Flask app for video streaming
app = Flask(__name__)
drone = Drone()


@app.route('/video_feed')
def video_feed():
    return Response(drone.generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000)
