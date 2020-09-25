from cv2 import imread
from cv2 import imshow
from cv2 import waitKey
from cv2 import destroyAllWindows
from cv2 import CascadeClassifier
from cv2 import rectangle
from PIL import Image
import os

inputImage = input('Enter image name with extension:')
image = Image.open(inputImage)
filename, fileExtension = os.path.splitext(inputImage)
new_image = image.resize((600, 420))
new_image.save('test{et}'.format(et = fileExtension))
pixels = imread('test{et}'.format(et = fileExtension))
classifier = CascadeClassifier('haarcascade_frontalface_default.xml')
bboxes = classifier.detectMultiScale(pixels)
for box in bboxes:
	x, y, width, height = box
	x2, y2 = x + width, y + height
	rectangle(pixels, (x, y), (x2, y2), (0,0,255), 1)
imshow('face detection', pixels)
print(Completed successfully !!)
waitKey(0)
destroyAllWindows()
