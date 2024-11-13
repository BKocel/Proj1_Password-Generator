import random
import math
from time import strftime, sleep, perf_counter_ns

def currentkey():
    sleep(random.random())
    dayt = int(strftime("%d")) # current day
    sect = int(strftime("%S")) # current time
    msec = perf_counter_ns()
    keyt = dayt * sect
    keyt2 = keyt * msec
    random.seed(keyt2)
    print(keyt2) # - FOR DEBUG ONLY


while 1 == 1:    
    currentkey()