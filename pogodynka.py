import requests, json
print("Pogodynka")
resp= requests.get("https://danepubliczne.imgw.pl/api/data/synop")
#print(json.loads(resp.text))
x=input("Wypisać miasta? t/n ")
for row in json.loads(resp.text):
    if x=="t":
        print(row['stacja'])

odp="t"
while odp=="t":
    city= input("PODAJ MIASTO: ")
    for row in json.loads(resp.text):
        if row["stacja"] in city:
            print(f"{row['stacja'].upper()}")
            print(f" 'id stacji' : {row['id_stacji']}")
            print(f" 'datapomiru' : {row['data_pomiaru']}")
            print(f"'godzinapomiaru': {row['godzina_pomiaru']} ")
            print(f"'temperaturapomiaru': {row['temperatura']} ")
            print(f" 'prędkość wiatru' : {row['predkosc_wiatru']}")
            print(f" 'kierunek_wiatru' : {row['kierunek_wiatru']}")
            print(f" 'wilgotnosc_wzgledna' : {row['wilgotnosc_wzgledna']}")
            print(f" 'suma_opadu' : {row['suma_opadu']}")
            print(f" 'cisnienie' : {row['cisnienie']}")
            print()
            odp=input("Jeszcze raz? t/n ")

            

