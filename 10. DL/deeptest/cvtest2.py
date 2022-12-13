import cv2

# video = cv2.VideoCapture( 'Office-Parkour.mp4' )
video = cv2.VideoCapture( 0 )
while video.isOpened():
    check, frame = video.read()
    print( 'check' , check)
    if not check:
        print('end video' )
        break

    cv2.imshow( 'test', frame )
    if cv2.waitKey(25) == ord('q'):
        print('end...')
        break
video.release()
cv2.destroyAllWindows()