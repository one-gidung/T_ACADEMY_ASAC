import cv2


img = cv2.imread( 'myimg/cat/cat1.jpg' )
cv2.imshow( 'test', img )
cv2.waitKey(1000)
cv2.destroyAllWindows()