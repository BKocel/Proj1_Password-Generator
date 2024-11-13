import random
import math
import datetime

# Generators



def dictionary(wcount):
    print("Function 'dictionary' was called, but it is not implemented")
    return(1)

def symbols(scount):
    char = []
    print("Function 'symbols' was called, but it is not implemented")
    return(1)


def random(nrcount):
    i= 0
    numbers = []
    while i in range(nrcount):
        rand = int(random(1))
        numbers.append(rand)
        i += 1
    
    # print("Function 'random' was called, but it is not implemented")
    return(numbers)

# CLI

print("Witaj w generatorze haseł")
print()
print("Oto mozliwe metody losowania")
print()
print("1. Numery")
print("2. Wyrazy")
print("3. Znaki i Numery")
print("4.Wyrazy z numerami")

mode = int(input("Wybierz tryb pracy generatora: "))



match mode:
    case 1:
        print()
        print(random(1))
    case 2:
        print()
    case 3:
        print()
    case 4: 
        print()
    case _ :
        print("Niepoprawna opcja, proszę spróbować ponownie.")