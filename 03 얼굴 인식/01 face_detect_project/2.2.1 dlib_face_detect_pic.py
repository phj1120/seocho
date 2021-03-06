# wget https://woman.jeongps.com/shape_predictor_68_face_landmarks.dat
# http://dlib.net/files/shape_predictor_68_face_landmarks.dat.bz2

# import the necessary packages

from imutils import face_utils
import dlib
import cv2, os

# initialize dlib's face detector (HOG-based) and then create
# the facial landmark predictor

imgs_path = 'test_image'
imgs = os.listdir(imgs_path)

for img in imgs:
    p = "etc/shape_predictor_68_face_landmarks.dat"
    detector = dlib.get_frontal_face_detector()
    predictor = dlib.shape_predictor(p)
    
    path = f'{imgs_path}/{img}'

    image = cv2.imread(path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # detect faces in the grayscale image
    rects = detector(gray, 0)
    
    # loop over the face detections
    for (i, rect) in enumerate(rects):
    	# determine the facial landmarks for the face region, then
    	# convert the facial landmark (x, y)-coordinates to a NumPy
    	# array
    	shape = predictor(gray, rect)
    	shape = face_utils.shape_to_np(shape)
    
    	# loop over the (x, y)-coordinates for the facial landmarks
    	# and draw them on the image
    	for (x, y) in shape:
    		cv2.circle(image, (x, y), 2, (0, 255, 0), -1)
    
    # show the output image with the face detections + facial landmarks
    cv2.imshow("image", image)
    cv2.waitKey(0)

cv2.destroyAllWindows()