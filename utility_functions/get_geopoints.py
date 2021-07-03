from geopy.geocoders import Nominatim


def get_points(country, city):
    """

    :param country: Name of the country
    :param city: Name of the city
    :return: Tuple of latitude,longitude
    """
    geolocator = Nominatim(user_agent="my_user_agent")
    loc = geolocator.geocode(city + ',' + country)

    try:
        gps_coordinates = (loc.latitude, loc.longitude)
    except:
        gps_coordinates = (None, None)
    return gps_coordinates
