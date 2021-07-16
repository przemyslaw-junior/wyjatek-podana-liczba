# definicja przedziału liczb
def readint(prompt, min, max):
# wejście w pętle nieskończoną dopuki warunek nie zostanie spełniony
    while True:
        try:
            x = int(input("Wprowadź liczbę: "))
# żądany warunek do wyścia z pętli
            if x > min and x < max:
                print('liczba mieści się w zakresie')
# wyjście z pętli
                break
# sprawdzenie warunku poza zakresem 
            elif x < min or x > max:
                print('liczba poza zakresem')
# kontynuacja pętli
                continue
# wyjątek - wprowadzenie liczby zmienno przecinkowej lub łańcucha znaków "string"
        except ValueError: 
            print("Musisz wpisać wartość całkowitą.")
# kontynuacja pętli
            continue
# zwrucenie poprawnej liczby użytkownika
    return x

# wywołanie funkcji "readint"
v = readint("Podaj liczbę od -10 do 10: ", -10, 10)

# wyświetlenie wyniku
print("Liczba to:", v)
