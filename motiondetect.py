import numpy as np		     
import cv2                           
from datetime import datetime         
def diffImg(t0, t1, t2):              
  d1 = cv2.absdiff(t2, t1)
  d2 = cv2.absdiff(t1, t0)
  return cv2.bitwise_and(d1, d2)

threshold = 78000                   
cam = cv2.VideoCapture(0)            
winName = "Movement Indicator"	      
cv2.namedWindow(winName)             


t_minus = cv2.cvtColor(cam.read()[1], cv2.COLOR_RGB2GRAY)
t = cv2.cvtColor(cam.read()[1], cv2.COLOR_RGB2GRAY)
t_plus = cv2.cvtColor(cam.read()[1], cv2.COLOR_RGB2GRAY)

timeCheck = datetime.now().strftime('%Ss')

while True:
  ret, frame = cam.read()	      
  totalDiff = cv2.countNonZero(diffImg(t_minus, t, t_plus))
  text = "threshold: " + str(totalDiff)				
  cv2.putText(frame, text, (20,40), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,0), 2)   
  if totalDiff > threshold and timeCheck != datetime.now().strftime('%Ss'):
    dimg= cam.read()[1]
    cv2.imwrite(datetime.now().strftime('%Y%m%d_%Hh%Mm%Ss%f') + '.jpg', dimg)
  timeCheck = datetime.now().strftime('%Ss')
 
  t_minus = t
  t = t_plus
  t_plus = cv2.cvtColor(cam.read()[1], cv2.COLOR_RGB2GRAY)
  cv2.imshow(winName, frame)
  
  key = cv2.waitKey(10)
  if key == 27:			
    cv2.destroyWindow(winName)
    break
