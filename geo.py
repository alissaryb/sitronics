from geopy.geocoders import Nominatim
import time

def get_coordinates(address):
    time.sleep(1)
    geolocator = Nominatim(user_agent="myGeocoder")

    # Получаем местоположение по адресу
    location = geolocator.geocode(address)

    if location:
        return [location.latitude, location.longitude]
    else:
        return None

# Пример использования
list_address = [
    "1600 Amphitheatre Parkway, Mountain View, CA, 94043, USA",
    "Red Square, Moscow, Russia",
    "221B Baker Street, London, UK",
    "Tverskaya St, 7, Moscow, Russia"
]

for address in list_address:
    coordinates = get_coordinates(address)
    time.sleep(1)  # Задержка в 1 секунду между запросами

    if coordinates:
        print(f"Координаты для '{address}': {coordinates}")
    else:
        print(f"Не удалось найти координаты для '{address}'")
