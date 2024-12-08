import random # Random number generation
from time import strftime, sleep, perf_counter_ns 


def currentkey(): # secret number generator
    sleep(random.random())
    dayt = int(strftime("%d")) # current day
    sect = int(strftime("%S")) # current time
    msec = perf_counter_ns()
    keyt = dayt * sect
    keyt2 = keyt * msec
    random.seed(keyt2)
    # print(keyt2) # - FOR DEBUG ONLY


# CLI

print("Witaj w generatorze haseł")
print()
print("Oto mozliwe metody losowania")
print()
print("1. Numery")
print("2. Symbole")
print("3. Symbole i numery")


mode = int(input("Wybierz tryb pracy generatora: "))

# Generators 
times = int(input("Podaj długość hasła: "))
if times <= 0: # Checks if proper password length has been given
    print("Niepoprawny argument, proszę spróbować ponownie [Kod błędu: 01]") # Code 1: Improper password length
else:
    match mode:
        case 1: # numbers generation
            
            numberlist = []
            i = 0
            print("Proszę czekać, generowanie hasła...")
            currentkey()
            while i in range(times):
                
                rand = random.randrange(1,10)
                numberlist.append(rand)
                i+=1
            
            out = ''.join(str(x) for x in numberlist)
            print("Twoje nowe hasło to: ", end = '')
            print(out)
        case 2: # ASCII symbol generation (alphabet & symbols only)
            
            password = []
            i = 0
            print("Proszę czekać, generowanie hasła...")
            currentkey()
            while i in range(times):
                rand = int(random.randrange(65,122))
                if rand == 10: # Removes any randomly generated space symbols
                    rand = 1
                    
                else:
                    password.append(chr(rand))
                i+=1
            
            out = ''.join(str(x) for x in password)
            print("Twoje nowe hasło to: ", end = '')
            print(out)
        case 3: # Combined number and ASCII Symbol generation
            
            # print(times) # for DEBUG
            password = []
            i=0
            print("Proszę czeka, generowanie hasła...")
            currentkey()
            while i in range(times):
                rand1 = chr(int(random.randrange(65,122)))  # leters generation
                rand2 = int(random.randrange(0,10)) # numbers generation, it wokrs now! :)
                order = random.random()# randomly gives 0 or 1
                if order < 0.5:
                    password.append(rand1)
                else:
                    password.append(rand2)
                i+=1
            if len(password) == times :
                out = ''.join(str(x) for x in password)
                print("Twoje nowe hasło to: ", end = '')
                print(out)
            else:
                print("NIEPRAWIDŁOWA DŁUGOŚĆ")
                out = ''.join(str(x) for x in password)
                print("Twoje nowe hasło to: ", end = '')
                print(out)
        case _ : # Unexpected handler
            print("Niepoprawna opcja, proszę spróbować ponownie. [Kod błędu: 02]") # Code 2: Improper operation selected

    