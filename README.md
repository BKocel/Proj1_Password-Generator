## Nazwa programu: "Generator haseł" <br> Plik zawierający program: "main.py"

#### Opis działania programu:
Użytkownik wybiera tryb losowania programu:
1. Generacja liczb: program generuje wybraną przez użytkownika liczbę cyfr od 1 do 10; <br>
2. Generacja alfabetu: program generuje wybraną przez użytkownika liczbę liter, losując ich kodu ASCII (**65 - 122**); <br>
3. Generacja liczb i alfabetu: program generuję wybraną przez użytkownika liczbę liter lub cyfer (*Wybierane losowo*) , za pomocą ich kodów ASCII (**0-10, 65-122**). 

#### Użyte zmienne i ich typy:
1. **mode** - typ *int*, przechowuje wybrany tryb pracy generatora haseł (*Sposób generacji hasła*). <br>
2. **times** - typ *int*, przechowuje wybraną przez użytkownika długość hasła. <br>
3. **rand** - typ *int*, przechowuje aktualnie generowaną literę hasła w postaci liczby(*przy generowaniu liczb*) lub jej codu ASCII(*generowanie znaków oraz znaków i liczb*). <br>
4. **password** - typ *list*, przechowuje całość wygenerowanego hasła w postaci liter i znaków ASCII. <br>
5. **out** - typ *string*, przechowuje hasło w postaci tekstu. <br>
6. **order** - typ *int*, generowana losowo, decyduje czy generowana będzie cyfra, czy litera (***Używana tylko w 3 trybie!***).

#### Najważniejsze funkcje:
1. Funkcja ***random.randrange(a, b)*** z biblioteki **random**, użyta do generowania losowych wartości zmiennoprzecinkowych z zakresu a - b (konwertowanych potem do liczby całkowitej); <br>
2. Funkcja ***tim.strftime*** z biblioteki **time**, użyta do pozyskana aktualnego czasu, użytego do generowania losowego ziarna, wspomagającego generację losowych wartości; <br>
3. Funkcja ***currentkey** zawarta w programie, generuje ziarno dla funkcji *random*, używając aktualnego dnia i czasu w milisekundach. <br>

#### Działanie programu:
Po uruchomieniu program pyta użytkownika, jak metoda losowania ma być użyta. <br>
> Do wybrou są trzy metody opisane w sekcji **Opis działania programu**

Po wybraniu metody generacji program pyta użytkownika o długość hasła. I podaje gotowe hasło. <br>
Przykładowo: 
```

Witaj w generatorze haseł

Oto mozliwe metody losowania

1. Numery
2. Symbole
3. Symbole i numery
Wybierz tryb pracy generatora: 3
Podaj długość hasła: 6
Proszę czeka, generowanie hasła...
Twoje nowe hasło to: 31V6E0 
```




