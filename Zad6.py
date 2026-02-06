import requests
import matplotlib.pyplot as plt

url = "https://danepubliczne.imgw.pl/api/data/meteo"
try:
    dane = requests.get(url, timeout=10).json()
except:
    exit()

cele = ["KRAKÓW", "ZAKOPANE", "WARSZAWA"]
wyniki = {}

for wpis in dane:
    nazwa = wpis.get('nazwa_stacji')
    if nazwa:
        nazwa_up = nazwa.upper()
        for miasto in cele:
            if miasto in nazwa_up and miasto not in wyniki:
                wyniki[miasto] = float(wpis.get('wiatr_srednia_predkosc') or 0)

miasta = list(wyniki.keys())
wartosci = list(wyniki.values())
kolory = ["royalblue", "darkorange", "crimson"]

plt.figure(figsize=(10, 6))
slupki = plt.bar(miasta, wartosci, color=kolory[:len(miasta)], edgecolor='black')

for s in slupki:
    h = s.get_height()
    plt.text(s.get_x() + s.get_width()/2., h + 0.1, f'{h}', ha='center', fontweight='bold')

plt.title('Wiatr: Krakow, Zakopane, Warszawa')
plt.ylabel('m/s')
plt.show()