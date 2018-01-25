# import modules
import RPi.GPIO as gp
import os
import time
import picamera
import picamera.array
#import cv2

print("initializing camera")
# initialize camera
camera = picamera.PiCamera()
camera.resolution = (640, 480)
rawCapture = picamera.array.PiRGBArray(camera)
# let camera warm up
time.sleep(0.5)


camera.capture("test.jpg")
camera.close()

print("camera close")

# continuously capture photos
if False:
    for i, filename in enumerate(
            camera.capture_continuous('image{counter:02d}.jpg')):
        print(filename)
        time.sleep(1)
        if i == 59:
            break
# Capture image parameters
if False:
    camera.sharpness = 0
    camera.contrast = 0
    camera.brightness = 50
    camera.saturation = 0
    camera.ISO = 0
    camera.video_stabilization = False
    camera.exposure_compensation = 0
    camera.exposure_mode = 'auto'
    camera.meter_mode = 'average'
    camera.awb_mode = 'auto'
    camera.image_effect = 'none'
    camera.color_effects = None
    camera.rotation = 0
    camera.hflip = False
    camera.vflip = False
    camera.crop = (0.0, 0.0, 1.0, 1.0)
# capture image
if False:
    def capture_photo():
        camera.capture(rawCapture, format='bgr')
        img = rawCapture.array
        cv2.imshow()
    pass

print("GPIO setting")
gp.setwarnings(False)
gp.setmode(gp.BOARD)

gp.setup(3, gp.OUT)
#gp.setup(9, gp.IN)

#gp.output(3, True)
#gp.output(9, True)

# while i < 10:
for i in range(0,3):
    print("step %d" %i)
    gp.output(3,gp.HIGH)
    time.sleep(1)
    gp.output(3,gp.LOW)


#def capture(cam):
#    cmd = "raspistill -o capture_%d.jpg" % cam
#    os.system(cmd)


gp.cleanup()