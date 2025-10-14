import cv2 as cv
import mediapipe as mp
import time # to track frame rate

capture = cv.VideoCapture(0) # choose which webcam to use, 0 is the default
mp_hands = mp.solutions.hands
hands = mp_hands.Hands() # leaving default constructor parameters, 2 hands
mp_draw = mp.solutions.drawing_utils
previous_time = 0
current_time = 0

while True:
    ret, frame = capture.read()
    # ret is a boolean variable that returns true if the frame is available
    # frame is an image array vector captured based on the default
    # frames per second defined explicitly or implicitly
    img_RGB = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
    # function that converts an image from one color space to another (here to rgb)
    results = hands.process(img_RGB) # processes the frame
    # results.multi_hand_landmarks - gives hand coordinates if its in frame
    if results.multi_hand_landmarks: # in hand in the frame
        for hand_landmarks in results.multi_hand_landmarks:
            #for id, lmark in enumerate(hand_landmarks.landmark):
            #    h,w,c = frame.shape
            #    cx, cy = int(lmark.x*w), int(lmark.y*h) # positions in pixels
            #if id == 0: # make this landmark bigger
            #    cv.circle(frame, (cx, cy), 25, (255,0,255), cv.FILLED)
            mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS) # draws landmarks on hands

    current_time = time.time()
    fps = 1/(current_time-previous_time)
    previous_time = current_time

    cv.putText(frame, str(int(fps)), (10,70), cv.FONT_HERSHEY_PLAIN, 3,
               (255,0,255), 3) # display fps rate

    cv.imshow("Webcam window", frame)
    cv.waitKey(1)