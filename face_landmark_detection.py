import sys
import os
import dlib
import glob
import numpy as np
from skimage import io
import cv2
from imutils import face_utils

class NoFaceFound(Exception):
   """Raised when there is no face found"""
   pass

def generate_face_correspondences(theImage1, theImage2):
    # Detect the points of face.
    detector = dlib.get_frontal_face_detector()
    predictor = dlib.shape_predictor('utils/shape_predictor_68_face_landmarks.dat')
    corresp = np.zeros((68,2))

    imgList = [theImage1,theImage2]
    list1 = []
    list2 = []
    j = 1

    for img in imgList:

        if(j == 1):
            currList = list1
        else:
            currList = list2

        # Ask the detector to find the bounding boxes of each face. The 1 in the
        # second argument indicates that we should upsample the image 1 time. This
        # will make everything bigger and allow us to detect more faces.

        dets = detector(img, 1)

        try:
            if len(dets) == 0:
                raise NoFaceFound
        except NoFaceFound:
            print("Sorry, but I couldn't find a face in the image.")

        j=j+1

        for k, rect in enumerate(dets):
            
            # Get the landmarks/parts for the face in rect.
            shape = predictor(img, rect)
            # corresp = face_utils.shape_to_np(shape)
            
            for i in range(0,68):
                x = shape.part(i).x
                y = shape.part(i).y
                currList.append((x, y))
                corresp[i][0] += x
                corresp[i][1] += y
                # cv2.circle(img, (x, y), 2, (0, 255, 0), 2)

        # cv2.imshow("img", img)
        # cv2.waitKey(0)
        # cv2.destroyAllWindows()
        # cv2.imwrite(content_path.split(".jpg")[0] + "-dlib.jpg", img) 

    return [list1,list2]

content_path = str(sys.argv[1])
style_path = str(sys.argv[2])
content_pts_path = str(sys.argv[3])
style_pts_path = str(sys.argv[4])

image1 = cv2.imread(content_path)
image2 = cv2.imread(style_path)
[points1, points2] = generate_face_correspondences(image1, image2)

with open(content_pts_path, 'w+') as f:
    for j in range(len(points1)):
        f.write('%i, %i\n' % (points1[j][1], points1[j][0]))
with open(style_pts_path, 'w+') as f:
    for j in range(len(points2)):
        f.write('%i, %i\n' % (points2[j][1], points2[j][0]))
        