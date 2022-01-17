#人脸传感器
import RPi.GPIO as GPIO
import time

def HC_init():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(12, GPIO.IN)
# print(11122)
i=0
def HC_detected():
    global i
    if GPIO.input(12) == True:
        time.sleep(1)
        if GPIO.input(12) == True:
            print(i)
            i += 1
            GPIO.cleanup()

            return 1
        else:
            GPIO.cleanup()
            return 0
    else:
        GPIO.cleanup()
        return 0
