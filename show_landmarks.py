import cv2
import matplotlib.pyplot as plt
import sys

pts_path = str(sys.argv[1])
# image_path = pts_path.replace("pts/","").replace("txt","jpg")
# print(image_path)
image_path = str(sys.argv[2])

image = cv2.imread(image_path)
# print(image)

with open(pts_path) as f:
    points = f.read().splitlines()

print(len(points))

for i in range(len(points)):
    cv2.circle(image, (int(points[i].split(", ")[1]), int(points[i].split(", ")[0])), 1, (0, 255, 0), 2)

cv2.imwrite(image_path.split(".")[0] + "-dlib.jpg", image) 
