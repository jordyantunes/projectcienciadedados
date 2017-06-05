from geopy.geocoders import Nominatim

geolocator = Nominatim()
location = geolocator("Las Vegas")

print(location)