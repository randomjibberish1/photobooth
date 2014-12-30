#Python Booth Project
#photobooth.py
#!/usr/bin/python

# RPi.GPIO is already installed on the Pi
import RPi.GPIO as GPIO, time, os, subprocess

# GPIO setup
GPIO.setmode(GPIO.BCM)
SWITCH = 24
GPIO.setup(SWITCH, GPIO.IN)
RESET = 25
GPIO.setup(RESET, GPIO.IN)
PRINT_LED = 22
POSE_LED = 18
BUTTON_LED = 23
GPIO.setup(POSE_LED, GPIO.OUT)
GPIO.setup(BUTTON_LED, GPIO.OUT)
GPIO.setup(PRINT_LED, GPIO.OUT)
GPIO.output(BUTTON_LED, True)
GPIO.output(PRINT_LED, False)

while True:
  if (GPIO.input(SWITCH)):
    snap = 0
    while snap < 4:
      print("pose!")
      GPIO.output(BUTTON_LED, False)
      GPIO.output(POSE_LED, True)
      time.sleep(1.5)
      for i in range(5):
        GPIO.output(POSE_LED, False)
        time.sleep(0.4)
        GPIO.output(POSE_LED, True)
        time.sleep(0.4)
      for i in range(5):
        GPIO.output(POSE_LED, False)
        time.sleep(0.1)
        GPIO.output(POSE_LED, True)
        time.sleep(0.1)
      GPIO.output(POSE_LED, False)
      print("SNAP")
#changed from gphoto 2 to picamera, also changed photobooth%H%M%S.jpg to image.jpg
      gpout = subprocess.check_output("picamera --capture-image-and-download --filename /home/pi/photobooth_images/image.jpg", stderr=subprocess.STDOUT, shell=True)

#inserted code to adjust the camera size of the picamera
import picamera
import time
  with picamera.PiCamera() as camera:
    camera.resolution = (640, 480)
    camera.framerate = 24
    camera.start_preview()
    camera.annotate_text = 'Say Cheese!'
    time.sleep(0.5)
    # Take a picture including the annotation
    #removed camera.capture('image.jpg')
      print(gpout)
      if "ERROR" not in gpout: 
        snap += 1
      GPIO.output(POSE_LED, False)
    #removed time.sleep(0.5)
    print("please wait while your photos print...")
    GPIO.output(PRINT_LED, True)

#display image on monitor for demo purposes. Open a view, setting the view to the size of the captured image
my_view = viewer(my_image.width, my_image.height, "Basic image processing")
my_image.width = 
my_image.height =

# display the image on the screen
my_view.displayImage(my_image)

# wait for 5 seconds, so we can see the image
waitTime(5000)
   
##build image and send to printer  This is greyed as this is how to print.  3 tabs  indicate code. Remove # on this lines to active. 
#      subprocess.call("sudo /home/pi/scripts/photobooth/assemble_and_print", shell=True)
# TODO: implement a reboot button
# Wait to ensure that print queue doesn't pile up
# TODO: check status of printer instead of using this arbitrary wait time
#      time.sleep(110)
#      print("ready for next round")
#      GPIO.output(PRINT_LED, False)
#      GPIO.output(BUTTON_LED, True)

    #Ok
    
    #picture