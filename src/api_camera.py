
import time, datetime
import atexit, io, os, picamera, yuv2rgb, picamera, pygame
from gui_button import *
import custom_events
DEBUG = True

def init_camera():
    global camera, sizeMode, sizeData,yuv1, rgb1, yuv2, rgb2, stream
    s = os.getenv("SUDO_UID")
    uid = int(s) if s else os.getuid()
    s = os.getenv("SUDO_GID")
    gid = int(s) if s else os.getgid()
#variables used:
    sizeData = [ # Camera parameters for different size settings
     # Full res      Viewfinder  Crop window
    [(1280, 720), (320, 240)],#, (0.0   , 0.0   , 1.0   , 1.0   )], # Large
    [(640, 480), (320, 240)],#, (0.1296, 0.2222, 0.7408, 0.5556)], # Med
    [(320, 240), (320, 240)]]#, (0.2222, 0.2222, 0.5556, 0.5556)]] # Small
    # Buffers for viewfinder data
#    sizeMode = 1
    camera            = picamera.PiCamera()
#    atexit.register(camera.close)
    camera.resolution = sizeData[config.mode][1]
    config.recording = False
    stream = io.BytesIO() # Capture into in-memory stream
#    path = "/home/pi/recorded_videos"
    #parameters while recording is on
    yuv1 = bytearray(sizeData[config.mode][0][0]*sizeData[config.mode][0][1]*3/2)
    rgb1 = bytearray(sizeData[config.mode][0][0]*sizeData[config.mode][0][1]*3)
    #parameters while recording is off
    yuv2 = bytearray(320 * 240 * 3 / 2)
    rgb2 = bytearray(320 * 240 * 3)

    calculate_count()
    print camera.resolution


def deinit_camera():
    global camera, stream
    config.recording = False
    camera.close()
    stream.close()

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
    global sizeMode, camera, yuv1, rgb1, yuv2, rgb2, sizeData, stream
    stream = io.BytesIO() # Capture into in-memory stream
    camera.capture(stream, use_video_port=True, format='raw')
    stream.seek(0)
    if config.recording:
      #  yuv = bytearray(sizeData[config.mode][0][0]*sizeData[config.mode][0][1]*3/2)
      #  rgb = bytearray(sizeData[config.mode][0][0]*sizeData[config.mode][0][1]*3)
        stream.readinto(yuv1)  # stream -> YUV buffer
        yuv2rgb.convert(yuv1, rgb1, sizeData[config.mode][0][0], sizeData[config.mode][0][1])
        img = pygame.image.frombuffer(rgb1[0:(sizeData[config.mode][0][0] * sizeData[config.mode][0][1] * 3)],sizeData[config.mode][0], 'RGB')
        #os.system("convert img -resize 200X100 img")
        img = pygame.transform.scale(img, (320,240))
    else:
      #  rgb = bytearray(320 * 240 * 3)
      #  yuv = bytearray(320 * 240 * 3 / 2)
        stream.readinto(yuv2)  # stream -> YUV buffer
        yuv2rgb.convert(yuv2, rgb2, sizeData[config.mode][1][0],sizeData[config.mode][1][1])
        img = pygame.image.frombuffer(rgb2[0:(sizeData[config.mode][1][0] * sizeData[config.mode][1][1] * 3)],sizeData[config.mode][1], 'RGB')

#    stream.close()
#    if config.recording:
#    else:
    screen.blit(img,((320 - img.get_width() ) / 2,(240 - img.get_height()) / 2))

def increment_count():
    config.count = (config.count + 1)%1000

def record():
    global camera, sizeData
    if not config.recording:
#        camera.resolution = size_Data[sizeMode][0]
        camera.resolution = sizeData[config.mode][0]
        if DEBUG:
            print camera.resolution
           # print config.count 
           # print config.max_count
#        config.camera_preview = False   # to turn off the preview
        import time 		#needs to be moved above
        date = time.strftime("%d-%m-%y")
        full_path = config.path + "/video" + "%03d"%config.max_count + "_" + date
        if DEBUG:
            print full_path
            print "Recording Started"

        camera.start_recording(full_path, 'h264')
#        api_audio.t.start()
        config.recording = True
        if config.count > config.max_count:
            config.max_count = config.count
        increment_count()
        config.start_time = datetime.datetime.now()
#        camera.resoultion = sizeData[config.mode][0]
    elif config.recording:
        camera.stop_recording()
        config.recording = False
#        api_audio.t.join()
        camera.resolution = (320,240)
        if DEBUG: print "Recording Stopped"
#        camera.resolution = sizeData[config.mode][0]

def navigation(n):
#    global path
    if config.camera_preview:
        config.camera_preview = False
    config.count = (config.count + n) % config.max_count


