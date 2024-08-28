# views.py
import cv2
import time
from django.http import StreamingHttpResponse, JsonResponse
from django.shortcuts import render

from drone_control.control.tello_control import Drone

"""def control_feed(request):
    battery = me.get_battery()
    if me.get_battery() != battery:
        battery = me.get_battery()
    connection = me.query_wifi_signal_noise_ratio()
    if me.me.query_wifi_signal_noise_ratio() != connection:
        connection = me.query_wifi_signal_noise_ratio()
    win = init()
    while True:
        vals = getKeyboardInput()

        return render(request, 'drone/control.html',
                      context={'battery': battery,
                               'connection': connection,
                               'vals': vals,
                               'win': win
                               }
                      )
"""

drone = Drone()


def video_feed(request):
    return StreamingHttpResponse(drone.generate_frames(), content_type='multipart/x-mixed-replace; boundary=frame')


def index(request):
    return render(request, 'drone/control.html')


def control_drone(request):
    if request.method == 'POST':
        command = request.POST.get('command')

        speed = 50
        lr, fb, ud, yv = 0, 0, 0, 0

        if command == "LEFT":
            lr = -speed
        elif command == "RIGHT":
            lr = speed
        elif command == "UP":
            fb = speed
        elif command == "DOWN":
            fb = -speed
        elif command == "w":
            ud = speed
        elif command == "s":
            ud = -speed
        elif command == "a":
            yv = -speed
        elif command == "d":
            yv = speed
        elif command == "q":
            drone.land()
        elif command == "e":
            drone.takeoff()
        elif command == "g":
            drone.flip_back()
        elif command == "STOP":
            # Stop all movements
            lr, fb, ud, yv = 0, 0, 0, 0

        drone.send_rc_control(lr, fb, ud, yv)
        return JsonResponse({'status': 'success'})
    return JsonResponse({'status': 'failed'})

