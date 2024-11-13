import random
import math
from time import strftime, sleep, perf_counter_ns

# secret number generator
def currentkey():
    sleep(random.random())
    dayt = int(strftime("%d")) # current day
    sect = int(strftime("%S")) # current time
    msec = perf_counter_ns()
    keyt = dayt * sect
    keyt2 = keyt * msec
    random.seed(keyt2)

# CLI

print("Witaj w generatorze haseł")
print()
print("Oto mozliwe metody losowania")
print()
print("1. Numery")
print("2. Wyrazy")
print("3. Znaki i Numery")
print("4. Wyrazy z numerami")

mode = int(input("Wybierz tryb pracy generatora: "))



match mode:
    case 1:
        times = int(input("Podaj długość liczby: "))
        numberlist = []
        i = 0
        print("Proszę czekać, generowanie liczby, to może chwilę potrwać")
        while i in range(times):
            currentkey()
            rand = random.randrange(1,10)
            numberlist.append(rand)
            i+=1
        print()
        out = ''.join(str(x) for x in numberlist)
        print(out)

    case 2:
        print()
    case 3:
        print()
    case 4: 
        print()
    case _ :
        print("Niepoprawna opcja, proszę spróbować ponownie.")