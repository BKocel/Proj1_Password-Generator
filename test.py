from time import strftime, sleep
import random

def currentkey():
    interval = random.randrange(1,5)
    sleep(interval)
    dayt = int(strftime("%d")) # current day
    print(dayt)
    sect = int( strftime("%S")) # current time
    print(sect )
    keyt = dayt * sect
    print(keyt )
    return(keyt)

print(currentkey())
