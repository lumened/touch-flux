# This file defines the navigation screen.
# This requires the following procedures:
#  init()
#  draw()
#  handle_event()
import time, datetime
import atexit, io, os, picamera, yuv2rgb, picamera, pygame
from gui_button import *
from api_interface import *
import custom_events

DEBUG = True

#some variables defined

def init():
    global menu

    menu = {}
#Defining rectangular buttons
    menu['btn1'] = Button('navigation') #go back to navigation window
    menu['btn2'] = Button('left') #navigate left in the videos
    menu['btn3'] = Button('right')#navigate right in the videos
    menu['btn4'] = Button('Settings')#Settings
    menu['surface'] = Button(' ')
    return None

def init_camera():
    global camera, sizeMode, sizeData,yuv, rgb, path
    s = os.getenv("SUDO_UID")
    uid = int(s) if s else os.getuid()
    s = os.getenv("SUDO_GID")
    gid = int(s) if s else os.getgid()
#variables used:
    sizeMode = 0     #default to large 
    sizeData = [ # Camera parameters for different size settings
     # Full res      Viewfinder  Crop window
    [(2592, 1944), (320, 240), (0.0   , 0.0   , 1.0   , 1.0   )], # Large
    [(1920, 1080), (320, 180), (0.1296, 0.2222, 0.7408, 0.5556)], # Med
    [(1440, 1080), (320, 240), (0.2222, 0.2222, 0.5556, 0.5556)]] # Small
    # Buffers for viewfinder data
    rgb = bytearray(320 * 240 * 3)
    yuv = bytearray(320 * 240 * 3 / 2)

    camera            = picamera.PiCamera()
#    atexit.register(camera.close)
    camera.resolution = sizeData[sizeMode][1]
    config.recording = False
    path = "/home/pi/recorded_videos"
    calculate_count()


def deinit_camera():
    global camera
    camera.close()   

#to find the count of the file to be written next for the first time when the camera module is initiated
def calculate_count():      
    global path, count
    files = os.listdir(path)
    if files == []:
        count = 0
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
        count = int(last_file[start_index:end_index])  
        if count == 999:
            count = 0
        else:
            count = count + 1

def preview(screen):
    global sizeMode, camera, yuv, rgb, sizeData
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
    screen.blit(img,
      ((320 - img.get_width() ) / 2,
       (240 - img.get_height()) / 2))

def increment_count():
    global count
    if count < 999:
        count = count + 1
    else:
        count = 0
 
def record(): 
    global camera, count, start_time
    if not config.recording:
        date = time.strftime("%d-%m-%Y")
        full_path = path + "/video" + "%03d"%count + "_" + date
        print full_path     
        camera.start_recording(full_path, 'h264')
        config.recording = True
        increment_count()
        start_time = datetime.datetime.now()
    else:
        camera.stop_recording()
        config.recording = False
   
def render_time(screen):
    global start_time
    myfont = pygame.font.SysFont("monospace", 15)
    # render text
    current_time = datetime.datetime.now()
#    elapsed_time = str((current_time.hour - start_time.hour)%24) + ":" + str((current_time.minute- start_time.minute)%60) + ":" +  str((current_time.second - start_time.second)%60)
    elapsed_time = str(current_time - start_time)
    elapsed_time = elapsed_time.rpartition(".")[0]            # to remove the milliseconds
    label = myfont.render(elapsed_time, 1, config.colors['orange'])
    screen.blit(label, (130, 20))

def draw(screen, mouse, transparent = 0xFF):
    global menu

    x = 10
    y = 10
 
    height = 80 
    width = 60
    menu['surface'].draw_rect(screen, mouse, (20,20,200,280), (0,0),0)    #surface not becoming transparent
    menu['btn1'].draw_rect(screen, mouse, (x,y,height,width), (x+10,y+20), transparent)
    menu['btn2'].draw_rect(screen, mouse, (x,y+160,height,width), (x+30,y+170+10), transparent)
    menu['btn3'].draw_rect(screen, mouse, (x+220,y+160,height,width), (x+230+20,y+170+10), transparent)
    menu['btn4'].draw_rect(screen, mouse, (x+220,y,height,width), (x+230+5,y+20), transparent)
    if config.recording:
         render_time(screen)
          #btn.check_hover(mouse)
    return None


def handle_event(mouse):
    global menu

#    if playback_find_player() is not None :
#        pygame.event.post(custom_events.SWITCH_TO_PLAYBACK)

    if menu['btn1'].obj.collidepoint(mouse):
        if DEBUG : print('button 1 clicked')
        pygame.event.post(custom_events.SWITCH_TO_NAVIGATION)
#        return 2
            
    elif menu['btn2'].obj.collidepoint(mouse):
        if DEBUG : print('button 2 clicked')
                  
    elif menu['btn3'].obj.collidepoint(mouse):
        if DEBUG : print('button 3 clicked')
        record()          

    elif menu['btn4'].obj.collidepoint(mouse):
        if DEBUG : print('button 4 clicked')
             
    elif menu['surface'].obj.collidepoint(mouse):
        if DEBUG : print('surface clicked')
        record()
    return None
