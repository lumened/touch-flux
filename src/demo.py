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
path="/home/pi/videos"
files = os.listdir(path)
files = sorted(files)
last_file = files[-1]
#    index = -1
i = 0
while i < len(last_file):
    if last_file[i].isdigit():
        break
    i = i+1;
start_index = i
while i < len(last_file):
    if not last_file[i].isdigit():
        break
    i = i+1
end_index = i
print files
print last_file
print start_index
print end_index
#end_index = end_index-1
print int(last_file[start_index:end_index])
