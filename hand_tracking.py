import cv2 as cv
import mediapipe as mp
import time # to track frame rate

class handDetector():
    def __init__(self, mode=False, max_num_hands=1, detection_confidence=1,
                 track_confidence=0.5):
        self.mode = mode
        self.max_num_hands = max_num_hands
        # self.model_complexity = model_complexity
        self.detection_confidence = detection_confidence
        self.track_confidence = track_confidence

        self.mp_hands = mp.solutions.hands
        self.hands = self.mp_hands.Hands(self.mode, self.max_num_hands, self.detection_confidence,
                                         self.track_confidence)
        self.mp_draw = mp.solutions.drawing_utils

    def findHands(self, frame, draw=True):
        img_RGB = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
        # function that converts an image from one color space to another (here to rgb)
        results = self.hands.process(img_RGB)  # processes the frame
        # results.multi_hand_landmarks - gives hand coordinates if its in frame
        if results.multi_hand_landmarks:  # in hand in the frame
            for hand_landmarks in results.multi_hand_landmarks:
                # for id, lmark in enumerate(hand_landmarks.landmark):
                #    h,w,c = frame.shape
                #    cx, cy = int(lmark.x*w), int(lmark.y*h) # positions in pixels
                # if id == 0: # make this landmark bigger
                #    cv.circle(frame, (cx, cy), 25, (255,0,255), cv.FILLED)
                if draw:
                    self.mp_draw.draw_landmarks(frame, hand_landmarks, self.mp_hands.HAND_CONNECTIONS)  # draws landmarks on hands
        return frame

def main():
    previous_time = 0
    current_time = 0
    capture = cv.VideoCapture(0)  # choose which webcam to use, 0 is the default
    detector = handDetector()

    while True:
        ret, frame = capture.read()
        # ret is a boolean variable that returns true if the frame is available
        # frame is an image array vector captured based on the default
        # frames per second defined explicitly or implicitly

        frame = detector.findHands(frame)

        current_time = time.time()
        fps = 1 / (current_time - previous_time)
        previous_time = current_time

        cv.putText(frame, str(int(fps)), (10, 70), cv.FONT_HERSHEY_PLAIN, 3,
                   (255, 0, 255), 3)  # display fps rate

        cv.imshow("Webcam window", frame)
        cv.waitKey(1)

if __name__ == "__main__":
    main()