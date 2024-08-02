import cv2
import time
import random
inTime = time.time()
def take_Screenshot():
    screen = cv2.VideoCapture(0)
    randNum = random.randint(1,1000)
    imageName = ""
    result = True
    while (result):
        ret, frame = screen.read()
        imageName = "screenshot" + str(randNum) + ".jpeg"
        cv2.imwrite(imageName, frame)
        result = False
    screen.release()
    cv2.destroyAllWindows()
    print("Screenshots taken", imageName)
take_Screenshot()
def main():
    global inTime
    while True:
        if(time.time()-inTime)>=5:
            take_Screenshot()
            inTime = time.time()
main()
