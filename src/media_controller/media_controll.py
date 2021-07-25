import cv2
import time
from . import HandTrackingModule as htm
import win32api
from win32con import VK_MEDIA_PLAY_PAUSE, KEYEVENTF_EXTENDEDKEY


#TODO: add a keyboard interruption such as escape 
def play_button(display: bool) -> None:


    ################################
    wCam, hCam = 640, 480
    #wCam, hCam = 1920, 1080
    ################################
    
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Cannot open camera")
        exit()

    cap.set(3, wCam)
    cap.set(4, hCam)
    pTime = 0
    
    detector = htm.handDetector(maxHands=1, detectionCon=0.8, trackCon=0.7)
    
    while True:
        success, img = cap.read()
        if not success:
            print("Can't receive frame (stream end?). Exiting ...")
            break
        img = detector.findHands(img)
        lmList,_ = detector.findPosition(img, draw=False)
        if len(lmList) != 0:
            fingers = detector.fingersUp()
            
            if fingers[2] and fingers[1] and not fingers[0] and not fingers[3] and not fingers[4]:
                win32api.keybd_event(VK_MEDIA_PLAY_PAUSE, 0, KEYEVENTF_EXTENDEDKEY, 0)
                time.sleep(1)
    

        if display:   
            cTime = time.time()
            fps = 1 / (cTime - pTime)
            pTime = cTime
            cv2.putText(img, f'FPS: {int(fps)}', (40, 50), cv2.FONT_HERSHEY_COMPLEX,
                        1, (255, 0, 0), 3)

            cv2.imshow("Img", img)
        
        if cv2.waitKey(1) == 27:
            cv2.destroyAllWindows()
            break