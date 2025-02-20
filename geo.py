from geopy.geocoders import Nominatim
import time

def get_coordinates(address):
    time.sleep(3)
    geolocator = Nominatim(user_agent="myGeocoder")

    # Получаем местоположение по адресу
    location = geolocator.geocode(address)

    if location:
        return [location.latitude, location.longitude]
    else:
        return None

if __name__ == '__main__':
    list_address = [
        "24 Minin Street, Building 1, Nizhny Novgorod, Russia",
        "260 Maxim Gorky Street, Office 27, 4th Floor, Nizhny Novgorod, Russia",
        "68 Karl Marx Street, Kazan, Republic of Tatarstan, Russia"
    ]

    for address in list_address:
        coordinates = get_coordinates(address)
        time.sleep(1)

        if coordinates:
            print(f"Координаты для '{address}': {coordinates}")
        else:
            print(f"Не удалось найти координаты для '{address}'")
