import numpy as np
import cv2

name=input()
name=name+'.jpg'

img = cv2.imread(name)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = np.float32(gray)

corners = cv2.goodFeaturesToTrack(gray,10,0.1,10)
corners = np.int0(corners)

#print (len(corners))

shapes=['triangle','rectangle','pentagon','hexagon','heptagon','octagon','nonagon','decagon']

print(shapes[len(corners)-3])
    
