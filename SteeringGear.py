#舵机
import RPi.GPIO as GPIO
import time


def init():
    GPIO.setmode(GPIO.BOARD)
    Vcc_Pin = 37
    In_Pin = 35  # 操控线（黄线）
    GPIO.setup(Vcc_Pin, GPIO.OUT, initial=GPIO.HIGH)
    GPIO.setup(In_Pin, GPIO.OUT, initial=GPIO.LOW)
    p = GPIO.PWM(In_Pin, 50)  # 设置频率为50KHz,20ms左右的时基脉冲(1/0.020s=50HZ)
    return p

    # class sg():
#     def __init__(self):
#         GPIO.setmode(GPIO.BOARD)
#         self.Vcc_Pin = 37
#         self.In_Pin = 35  # 操控线（黄线）
#         GPIO.setup(self.Vcc_Pin, GPIO.OUT, initial=GPIO.HIGH)
#         GPIO.setup(self.In_Pin, GPIO.OUT, initial=GPIO.LOW)
#         self.p = GPIO.PWM(self.In_Pin, 50)  # 设置频率为50KHz,20ms左右的时基脉冲(1/0.020s=50HZ)
#         self.p.start(0)
#         self.duty_cycle = 76
#         time.sleep(1)
#
#     def sg_op(self):
#         self.p.ChangeDutyCycle(2.5 + self.duty_cycle / 360 * 20)
#         time.sleep(0.2)
#         self.p.stop()
#         # GPIO.cleanup()
# for i in range(3):
#     s = sg()
#     s.sg_op()
# GPIO.cleanup()
#77-87
# def SG_op():
#     str1 = "please input the degree(0<=a<=120)\nor press q to quit\n"
#     r = input(str1)
#     try:
#         while not r == "q":
#             if r.isdigit():  # 判断输入的字符串是不是数字
#                 r = int(r)  # 是数字转换成数字
#             else:
#                 print("please input a number(0<=num<=120)")
#                 continue
#             if r < 0 or r > 180:  # 越界提示
#                 print("a must be [0,120]")
#                 continue
#             p.ChangeDutyCycle(2.5 + r / 360 * 20)  # 通过用户输入的角度来改变舵机的角度
#             time.sleep(0.02)
#             r = str(input(str1))
#     except KeyboardInterrupt:
#         pass
#     p.stop()
#     GPIO.cleanup()
def tonum(num):
    fm=10.0/180.0
    num=num*fm+2.5
    num=int(num*10)/10.0
    return num

def SG_op(angle):
    p = init()
    p.start(0)
    time.sleep(0.02)
    p.ChangeDutyCycle(tonum(angle))
    # p.ChangeDutyCycle(2.5+10*angle/180)
    time.sleep(0.4)
    p.ChangeDutyCycle(0)
    time.sleep(0.02)
    p.stop()
    GPIO.cleanup()
    # for i in range(0,91,10):
    #     p.ChangeDutyCycle(tonum(i))
    #     time.sleep(0.2)
    #     p.ChangeDutyCycle(0)
    #     time.sleep(0.02)
    # for i in range(91,-1,-10):
    #     p.ChangeDutyCycle(tonum(i))
    #     time.sleep(0.2)
    #     p.ChangeDutyCycle(0)
    #     time.sleep(0.02)
    # p.stop()
    # GPIO.cleanup()



