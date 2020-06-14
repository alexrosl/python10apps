import glob
from pathlib import Path

import cv2

img = cv2.imread("resources/galaxy.jpg", 0)

print(type(img))
print(img)
print(img.shape)
print(img.ndim)
resized_image = cv2.resize(img, (int(img.shape[1]/2), int(img.shape[0]/2)))

# cv2.imshow("Galaxy", resized_image)
# cv2.waitKey(2000)
# cv2.destroyAllWindows()
cv2.imwrite("resources/galaxy_resized.jpg", resized_image)


images = glob.glob("resources/*.jpg")

for image in images:
    img = cv2.imread(image, 0)
    re = cv2.resize(img, (100, 100))
    cv2.imwrite("resources/resized_" + Path(image).stem + Path(image).suffix, re)