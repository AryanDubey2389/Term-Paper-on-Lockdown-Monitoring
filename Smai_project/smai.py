import cv2
import numpy as np
 
filename = 'random-shapes-small.jpg'
img = cv2.imread(filename)
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
 
gray = np.float32(gray)
dst = cv2.cornerHarris(gray,2,3,0.04)
 
#result is dilated for marking the corners, not important
dst = cv2.dilate(dst,None)
 
# Threshold for an optimal value, it may vary depending on the image.
img[dst>0.01*dst.max()]=[0,0,255]
 
cv2.imshow('dst',img)
if cv2.waitKey(0) & 0xff == 27:
    cv2.destroyAllWindows()
##########################
import numpy as np
import cv2
from matplotlib import pyplot as plt
 
img = cv2.imread('random-shapes-small.jpg')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
 
# Find the top 20 corners
corners = cv2.goodFeaturesToTrack(gray,20,0.01,10)
corners = np.int0(corners)
 
for i in corners:
    x,y = i.ravel()
    cv2.circle(img,(x,y),3,255,-1)
 
cv2.imshow('Shi-Tomasi', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
################
import numpy as np
import cv2 as cv
 
# Read the image
img = cv.imread('chessboard.jpg')
 
# Convert to grayscale
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
 
# Find the features (i.e. keypoints) and feature descriptors in the image
sift = cv.SIFT_create()
kp, des = sift.detectAndCompute(gray,None)
 
# Draw circles to indicate the location of features and the feature's orientation
img=cv.drawKeypoints(gray,kp,img,flags=cv.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
 
# Save the image
cv.imwrite('sift_with_features_chessboard.jpg',img)
###########################
import numpy as np
import cv2 as cv
 
# Read the image
img = cv.imread('chessboard.jpg')
 
# Find the features (i.e. keypoints) and feature descriptors in the image
surf = cv.xfeatures2d.SURF_create(400)
kp, des = sift.detectAndCompute(img,None)
 
# Draw circles to indicate the location of features and the feature's orientation
img=cv.drawKeypoints(gray,kp,img,flags=cv.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
 
# Save the image
cv.imwrite('surf_with_features_chessboard.jpg',img)
######################
import numpy as np 
import cv2 
from matplotlib import pyplot as plt
     
# Read the training and query images
query_img = cv2.imread('query_image.jpg') 
train_img = cv2.imread('training_image.jpg') 
 
# Convert the images to grayscale 
query_img_gray = cv2.cvtColor(query_img,cv2.COLOR_BGR2GRAY) 
train_img_gray = cv2.cvtColor(train_img, cv2.COLOR_BGR2GRAY) 
 
# Initialize the ORB detector algorithm 
orb = cv2.ORB_create() 
 
# Detect keypoints (features) cand calculate the descriptors
query_keypoints, query_descriptors = orb.detectAndCompute(query_img_gray,None) 
train_keypoints, train_descriptors = orb.detectAndCompute(train_img_gray,None) 
 
# Match the keypoints
matcher = cv2.BFMatcher() 
matches = matcher.match(query_descriptors,train_descriptors) 
 
# Draw the keypoint matches on the output image
output_img = cv2.drawMatches(query_img, query_keypoints, 
train_img, train_keypoints, matches[:20],None) 
 
output_img = cv2.resize(output_img, (1200,650)) 
 
# Save the final image 
cv2.imwrite("feature_matching_result.jpg", output_img) 
 
# Close OpenCV upon keypress
cv2.waitKey(0)
cv2.destroyAllWindows()
######################
