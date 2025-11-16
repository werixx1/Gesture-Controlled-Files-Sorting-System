import cv2 as cv
import mediapipe as mp
import time # to track frame rate
import math

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
        # EACH FINGER HAS 4 LANDMARKS
        # 1-4 - thumb
        # 5-8 - second finger
        # 9-12 - third
        # 13-16 - fourth
        # 17-20 - last
        # 0 - wrist (kinda like start point)
        self.tip_ids = [4, 8, 12, 16, 20]

    def findHands(self, frame, draw=True):
        img_RGB = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
        # function that converts an image from one color space to another (here to rgb)
        self.results = self.hands.process(img_RGB)  # processes the frame
        # results.multi_hand_landmarks - gives hand coordinates if its in frame
        if self.results.multi_hand_landmarks:  # in hand in the frame
            for hand_landmarks in self.results.multi_hand_landmarks:
                # for id, lmark in enumerate(hand_landmarks.landmark):
                #    h,w,c = frame.shape
                #    cx, cy = int(lmark.x*w), int(lmark.y*h) # positions in pixels
                # if id == 0: # make this landmark bigger
                #    cv.circle(frame, (cx, cy), 25, (255,0,255), cv.FILLED)
                if draw:
                    self.mp_draw.draw_landmarks(frame, hand_landmarks, self.mp_hands.HAND_CONNECTIONS)  # draws landmarks on hands
        return frame

    def findPosition(self, img, hand_no=0, draw=True):
        # lists for all x and y coordinates
        x_list = []
        y_list = []
        bbox = []
        self.lm_list = []
        if self.results.multi_hand_landmarks:
            my_hand = self.results.multi_hand_landmarks[hand_no] # get hand from the ones that were detected
            for _id, lm in enumerate(my_hand.landmark): # iterating through all hands landmarks
                h,w,c = img.shape
                cx, cy = int(lm.x*w), int(lm.y*h) # turning landmark positions to pixels??
                x_list.append(cx)
                y_list.append(cy)
                self.lm_list.append([_id, cx, cy])
                if draw:
                    cv.circle(img, (cx, cy), 5, (255, 0, 255), cv.FILLED)
            xmin, xmax = min(x_list), max(x_list)
            ymin, ymax = min(y_list), max(y_list)
            bbox = xmin, ymin, xmax, ymax # bounding box for hands

            if draw:
                cv.rectangle(img, (xmin - 20, ymin - 20), (xmax + 20, ymax + 20),
                              (0, 255, 0), 2)

            return self.lm_list, bbox

    def fingersUp(self):
        fingers = []
        # thumb
        # get id where is the end of thumb and landmark closer to wrist
        # if its further from wrist (>) thumb must be up
        # using [1] - x coordinates (left and right movement)
        if self.lm_list[self.tip_ids[0]][1] > self.lm_list[self.tip_ids[0] - 1][1]:
            fingers.append(1) # thumb up
        else:
            fingers.append(0) # thumb down

        # rest of the fingers
        for _id in range(1, 5):
            # again checking the coordinates of the ends of fingers
            # using [2] - y coordinates (up and down movement)
            if self.lm_list[self.tip_ids[_id]][2] < self.lm_list[self.tip_ids[_id] - 2][2]:
                fingers.append(1)
            else:
                fingers.append(0)

        # totalFingers = fingers.count(1)

        return fingers # returns list of which fingers are currently up ex. [0,1,1,0,0]

    def findDistance(self, p1, p2, img, draw=True, r=15, t=3):
        # coordinates between two landmarks
        x1, y1 = self.lm_list[p1][1:]
        x2, y2 = self.lm_list[p2][1:]
        cx, cy = (x1 + x2) // 2, (y1 + y2) // 2 # middle point

        if draw:
            cv.line(img, (x1, y1), (x2, y2), (255, 0, 255), t) # line that connects the points
            # circles on both points
            cv.circle(img, (x1, y1), r, (255, 0, 255), cv.FILLED)
            cv.circle(img, (x2, y2), r, (255, 0, 255), cv.FILLED)
            cv.circle(img, (cx, cy), r, (0, 0, 255), cv.FILLED) # circle at the middle
        length = math.hypot(x2 - x1, y2 - y1) # euclidean distance between points

        return length, img, [x1, y1, x2, y2, cx, cy]

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

        # binding box
        # lm_list, bbox = detector.findPosition(frame)
        # if len(lm_list) != 0:
        #    print(lm_list[4])

        current_time = time.time()
        fps = 1 / (current_time - previous_time)
        previous_time = current_time

        cv.putText(frame, str(int(fps)), (10, 70), cv.FONT_HERSHEY_PLAIN, 3,
                   (255, 0, 255), 3)  # display fps rate

        cv.imshow("Webcam window", frame)
        cv.waitKey(1)

if __name__ == "__main__":
    main()