import time, os
import io
import time
import picamera

os.putenv('SDL_VIDEODRIVER', 'fbcon')
os.putenv('SDL_FBDEV'      , '/dev/fb1')
os.putenv('SDL_MOUSEDRV'   , 'TSLIB')
os.putenv('SDL_MOUSEDEV'   , '/dev/input/touchscreen')
os.putenv('SDL_AUDIODRIVER'   , 'alsa')
# Create an in-memory stream
#my_stream = io.BytesIO()
#with picamera.PiCamera() as camera:
camera = picamera.PiCamera()
camera.start_preview()
    # Camera warm-up time
time.sleep(10)
camera.stop_preview()
camera.capture(my_stream, 'jpeg')
