from socket import *
from random import randint
from sys import *

def IpSrc():
    num1 = randint(0, 255)
    num2 = randint(0, 255)
    num3 = randint(0, 255)
    num4 = randint(0, 255)
    IpOrigin = str(num1) + "." + str(num2) + "." + str(num3) + "." + str(num4)
    return IpOrigin

arg = str(argv[3])

