from base import Base
import imutils
import cv2

#Take picture from folder like: imagename1,imagename2 etc or image.jpg

print("Enter the number of images you want to concantenate:")
no_of_images = int(input())
print("Enter the image name in order of left to right in way of concantenation:")
#like image_left.jpg, image_right.jpg
filename = []
for i in range(no_of_images):
    print("Enter the %d image:" %(i+1))
    filename.append(input())

images = []

for i in range(no_of_images):
    images.append(cv2.imread(filename[i]))

#We need to modify the image resolution and keep our aspect ratio use the function imutils

for i in range(no_of_images):
    images[i] = imutils.resize(images[i], width=400)

for i in range(no_of_images):
    images[i] = imutils.resize(images[i], height=400)


base = Base()
if no_of_images==2:
    (result, matched_points) = base.image_stitch([images[0], images[1]], match_status=True)
else:
    (result, matched_points) = base.image_stitch([images[no_of_images-2], images[no_of_images-1]], match_status=True)
    for i in range(no_of_images - 2):
        (result, matched_points) = base.image_stitch([images[no_of_images-i-3],result], match_status=True)

#to show the got panaroma image and valid matched points
for i in range(no_of_images):
    cv2.imshow("Image {k}".format(k=i+1), images[i])

cv2.imshow("Keypoint Matches", matched_points)
cv2.imshow("output", result)


#to write the images
cv2.imwrite("Matched_points.jpg",matched_points)
cv2.imwrite("Output_image.jpg",result)

cv2.waitKey(0)
cv2.destroyAllWindows()
