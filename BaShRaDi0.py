import pyaudio
import urllib.request
import pickle

# Funkcja do odtwarzania stacji radiowej
def play_station(url):
    u = urllib.request.urlopen(url)
    audio_data = u.read()

    p = pyaudio.PyAudio()

    stream = p.open(format=p.get_format_from_width(width=2),
                    channels=2,
                    rate=44100,
                    output=True)

    stream.write(audio_data)
    stream.stop_stream()
    stream.close()

    p.terminate()

# Funkcja do dodawania stacji do pliku
def add_station(name, url):
    try:
        # Odczytanie listy stacji z pliku
        with open('stations.pickle', 'rb') as f:
            stations = pickle.load(f)
    except FileNotFoundError:
        # Jeśli plik nie istnieje, utworzenie pustej listy stacji
        stations = []

    # Dodanie nowej stacji do listy
    stations.append({'name': name, 'url': url})

    # Zapisanie zaktualizowanej listy stacji do pliku
    with open('stations.pickle', 'wb') as f:
        pickle.dump(stations, f)

while True:
    # Pobranie wyboru użytkownika
    print ('BaShRaDi0 by lysyr')
    choice = input('Wprowadź "play" aby odtworzyć stację, "add" aby dodać stację lub "exit" aby zakończyć: ')

    if choice == 'exit':
        break
    elif choice == 'play':
        # Odczytanie listy stacji z pliku
        with open('stations.pickle', 'rb') as f:
            stations = pickle.load(f)

        # Wypisanie listy stacji
        for i, station in enumerate(stations):
            print(f'{i+1}. {station["name"]}')

        # Pobranie wyboru stacji od użytkownika
        station_num = int(input('Wybierz numer stacji, którą chcesz odtworzyć: '))
        station = stations[station_num - 1]

        # Odtworzenie wybranej stacji
        play_station(station['url'])
    elif choice == 'add':
        # Pobranie nazwy i adresu URL stacji od użytkownika
        name = input('Wprowadź nazwę stacji: ')
        url = input('Wprowadź adres URL stacji: ')

        # Dodanie stacji do pliku
        add_station(name, url)
    else:
        print('Nieprawidłowa opcja.')
