
import time, datetime
import atexit, io, os, picamera, yuv2rgb, picamera, pygame
from gui_button import *
import custom_events


def init_camera():
    global camera, sizeMode, sizeData,yuv, rgb
    s = os.getenv("SUDO_UID")
    uid = int(s) if s else os.getuid()
    s = os.getenv("SUDO_GID")
    gid = int(s) if s else os.getgid()
#variables used:
    sizeData = [ # Camera parameters for different size settings
     # Full res      Viewfinder  Crop window
    [(1280, 720), (320, 240), (0.0   , 0.0   , 1.0   , 1.0   )], # Large
    [(640, 480), (320, 240), (0.1296, 0.2222, 0.7408, 0.5556)], # Med
    [(480, 360), (320, 240), (0.2222, 0.2222, 0.5556, 0.5556)]] # Small
    # Buffers for viewfinder data
    rgb = bytearray(320 * 240 * 3)
    yuv = bytearray(320 * 240 * 3 / 2)
    sizeMode = 1
    camera            = picamera.PiCamera()
#    atexit.register(camera.close)
    camera.resolution = sizeData[sizeMode][1]
    config.recording = False
#    path = "/home/pi/recorded_videos"
    calculate_count()
    print camera.resolution


def deinit_camera():
    global camera
    camera.close()

#to find the count of the file to be written next for the first time wh$
def calculate_count():
    # max_count = to keep a measure of the total no of files
    # count = determines the number of the file on which we are current$
#    global path
    files = os.listdir(config.path)
    if files == []:
        config.count = 0
    else:
        files = sorted(files)
        last_file = files[-1]
#        index = -1
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
        config.count = int(last_file[start_index:end_index])
        config.count = (config.count + 1)%1000
        config.max_count = config.count

def preview(screen):
    global sizeMode, camera, yuv, rgb, sizeData
    if config.recording:
        img = pygame.image.load('/home/pi/touch-flux/icons/gear.png')
        screen.blit(img,
           ((320 - img.get_width() ) / 2,
           (240 - img.get_height()) / 2))
        return None
    stream = io.BytesIO() # Capture into in-memory stream
    camera.capture(stream, use_video_port=True, format='raw')
    stream.seek(0)
    stream.readinto(yuv)  # stream -> YUV buffer
    stream.close()
    yuv2rgb.convert(yuv, rgb, sizeData[sizeMode][1][0],
      sizeData[sizeMode][1][1])
    img = pygame.image.frombuffer(rgb[0:
      (sizeData[sizeMode][1][0] * sizeData[sizeMode][1][1] * 3)],
      sizeData[sizeMode][1], 'RGB')
#    img = pygame.transform.scale(img, (320,240))
    screen.blit(img,
      ((320 - img.get_width() ) / 2,
       (240 - img.get_height()) / 2))

def increment_count():
    config.count = (config.count + 1)%1000

def record():
    global camera, start_time, sizeData
    if not config.recording:
#        camera.resolution = size_Data[sizeMode][0]
        camera.resolution = sizeData[config.mode][0]
        print camera.resolution
#        config.camera_preview = False   # to turn off the preview
        date = time.strftime("%d-%m-%Y")
        full_path = config.path + "/video" + "%03d"%config.count + "_" + date
        print full_path
        camera.start_recording(full_path, 'h264')
        config.recording = True
        if config.count > config.max_count:
            config.max_count = config.count
        increment_count()
        start_time = datetime.datetime.now()
    else:
        camera.stop_recording()
        config.recording = False
        camera.resolution = sizeData[config.mode][1]
 #       config.camera_preview = True   #to turn on the preview

def navigation(n):
#    global path
    if config.camera_preview:
        config.camera_preview = False
    config.count = (config.count + n) % config.max_count


