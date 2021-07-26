import cv2
import time
from . import HandTrackingModule as htm
from pynput.keyboard import Key, Controller


def media_play_pause(*args, **kwargs):
    """Takes the array of fingers up and a keyboard object
       and uses the media button play/pause if the index
       and middle finger of the right hand are up.
    """
    fingers = kwargs['fingers']
    keyboard = kwargs['keyboard']
    if fingers[2] and fingers[1] and not fingers[0] and not fingers[3] and not fingers[4]:
        keyboard.press(Key.media_play_pause)
        keyboard.release(Key.media_play_pause)
        time.sleep(1)


#TODO: add a keyboard interruption such as escape 
def main(display: bool) -> None:    
    """Main function that processes the webcam input and
    then calls functions to apply depending on this input.

    Args:
        display (bool): Whether to prompt a video feedback or not.
    """
    ################################
    wCam, hCam = 640, 480
    #wCam, hCam = 1920, 1080
    functions= [media_play_pause]
    ################################

    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Cannot open camera")
        exit()

    cap.set(3, wCam)
    cap.set(4, hCam)
    pTime = 0
    
    detector = htm.handDetector(maxHands=1, detectionCon=0.8, trackCon=0.7)
    keyboard = Controller()    

    while True:
        success, img = cap.read()
        if not success:
            print("Can't receive frame (stream end?). Exiting ...")
            break
        img = detector.findHands(img)
        lmList,_ = detector.findPosition(img, draw=False)
        if len(lmList) != 0:
            fingers = detector.fingersUp()

            for func in functions:
                func(fingers=fingers, keyboard=keyboard)            

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
