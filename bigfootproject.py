Python 3.5.3 (default, Jan 19 2017, 14:11:04) 
[GCC 6.3.0 20170124] on linux
Type "copyright", "credits" or "license()" for more information.
>>> import picamera
from time import sleep
camera = picamera.PiCamera()
sleep(5)
print "before photo"
camera.capture('image.jpg')
print "after photo"