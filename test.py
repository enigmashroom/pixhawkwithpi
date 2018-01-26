# import modules
import RPi.GPIO as gp
import os
import time
import picamera
import picamera.array
#import cv2

print("initializing camera")
# initialize camera
#camera = picamera.PiCamera()
#camera.resolution = (640, 480)
#rawCapture = picamera.array.PiRGBArray(camera)

#time.sleep(5)


#camera.capture("test.jpg")


#print("camera close")

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
gp.setup(3, gp.OUT, initial=gp.LOW)
# gp.setup(9, gp.IN)

# gp.output(3, True)
# gp.output(9, True)
# wait_for_edge()?
# while i < 10:

with picamera.Picamera() as camera:
    camera.resolution = (1280, 720)
    camera.framerate = 30
    camera.start_preview()
    # let camera warm up
    print("warming up")
    time.sleep(5)
    try:
        for i, filename in enumerate(
                camera.capture_continuous("img{counter:02d}.jpg", use_video_port=True)):
            print(filename)
            gp.output(3, gp.HIGH)
            time.sleep(0.1)
            gp.output(3, gp.LOW)
            time.sleep(0.5)
            if i == 5:
                break
    finally:
        camera.stop_preview()



for i in range(5):
    print("step %d" %i)
    camera.capture("image%s.jpg" % i)
    gp.output(3, gp.HIGH)
    time.sleep(0.1)
    gp.output(3, gp.LOW)
    time.sleep(0.5)

camera.close()
gp.cleanup()

#def capture(cam):
#    cmd = "raspistill -o capture_%d.jpg" % cam
#    os.system(cmd)

