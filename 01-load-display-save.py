from __future__ import print_function
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to image")
args = vars(ap.parse_args())

# read image from path using opencv imread function
image = cv2.imread(args["image"])

# let's print width, height, and channels of the images
print("width : {} pixels".format(image.shape[0]))
print("height: {} pixels".format(image.shape[1]))
print("channels: {}".format(image.shape[2]))


# let's show the image
cv2.imshow("Image", image)
cv2.waitKey(0)

# save the image in the new file
cv2.imwrite("./images/01-new-tyrex.jpg", image)
