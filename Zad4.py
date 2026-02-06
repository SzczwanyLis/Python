import multiprocessing
import math


def oblicz_fragment(zakres_x):
    wyniki = []
    for x in zakres_x:
        
        f_x = math.cos(x) + math.log(x + 1)**2
        wyniki.append(f_x)
    return wyniki

if __name__ == '__main__':
    start = 1
    stop = 1000000
    krok = 0.01
    
    wszystkie_x = []
    aktualny = start
    while aktualny <= stop:
        wszystkie_x.append(aktualny)
        aktualny += krok

    liczba_rdzeni = multiprocessing.cpu_count()
    rozmiar_fragmentu = len(wszystkie_x) // liczba_rdzeni
    fragmenty = [wszystkie_x[i:i + rozmiar_fragmentu] for i in range(0, len(wszystkie_x), rozmiar_fragmentu)]

    with multiprocessing.Pool(processes=liczba_rdzeni) as pool:
        finalne_wyniki = pool.map(oblicz_fragment, fragmenty)

    wynik_koncowy = [item for sublist in finalne_wyniki for item in sublist]

    print(f"Obliczono {len(wynik_koncowy)} wartości.")
    print(f"Pierwsze 5 wyników: {wynik_koncowy[:5]}")
