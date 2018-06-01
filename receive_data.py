# import modules
import RPi.GPIO as GPIO
import os
import time
import picamera
import picamera.array
import sys
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(7, GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
photo_num = int(sys.argv[1])

# Initialize camera
print "initializing camera"
camera = picamera.PiCamera()
camera.resolution = (int(sys.argv[2]), int(sys.argv[3]))
rawCapture = picamera.array.PiRGBArray(camera)
# Let camera warm up
print "warming up 2 secs"
time.sleep(2)
print "set camera"
camera.sharpness = 0
camera.contrast = 0
camera.brightness = 50
camera.saturation = 0
camera.ISO = 100
camera.video_stabilization = False
camera.exposure_compensation = 0
camera.exposure_mode = 'off'
camera.meter_mode = 'average'

camera.image_effect = 'none'
camera.color_effects = None
camera.rotation = 0
camera.hflip = False
camera.vflip = False
camera.crop = (0.0, 0.0, 1.0, 1.0)

camera.shutter_speed = camera.exposure_speed
camera.exposure_mode = 'off'
g = camera.awb_gains
camera.awb_mode = 'off'
camera.awb_gains = g

print "stabilization 10 secs"
time.sleep(10)

camera.start_preview()
path = "/home/pi/img/" + str(time.time())
os.makedirs(path)
i = 0

"""""
while True:
    if GPIO.input(3) == GPIO.LOW:
        print "low voltage"
        time.sleep(0.33)
    else:
        print "high voltage"
"""""
"""
for i in range(5):
    print "photo"
    img_path = path + "/img%02d.jpg" %i
    camera.capture(img_path)

"""
while True:
    channel = GPIO.wait_for_edge(7, GPIO.RISING)
    if channel is None:
        print "low voltage nothing happened"
        time.sleep(0.33)
    else:
        print "signal received"
        img_path = path + "/img%02d.jpg" %i
        camera.capture(img_path)
        i += 1

    if i == photo_num:
        print(photo_num)
        print "photos got"
        break

# GPIO.add_event_detect(3)

"""""
def my_callback(channel):
    print('This is a edge event callback function!')
    print('Edge detected on channel %s'%channel)
    print('This is run in a different thread to your main program')

GPIO.add_event_detect(channel, GPIO.RISING, callback=my_callback)
"""""
camera.stop_preview()

camera.close()

GPIO.cleanup()
