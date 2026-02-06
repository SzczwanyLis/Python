import threading
import requests

def Uniwerki(country, result_dict):
    url = f"http://universities.hipolabs.com/search?country={country}"
    try:
        response = requests.get(url, timeout=10)
        data = response.json()
        names = [uni['name'] for uni in data[:20]]
        result_dict[country] = names
    except:
        result_dict[country] = []

countries = [
    "Poland", "Germany", "France", "Italy", "Spain", 
    "Portugal", "Belgium", "Netherlands", "Austria", "Switzerland",
    "Sweden", "Norway", "Denmark", "Finland", "Iceland",
    "USA", "China", "Mexico", "Japan", "Brazil"
]

results = {}
threads = []

for c in countries:
    t = threading.Thread(target=Uniwerki, args=(c, results))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

for country, unis in results.items():
    print(f"{country}: {unis}")