# getInfo(name, year)
# image =
# year
# rating

# data = getInfo(name,year)
# data.image

import requests


def get_media_info(title, type = "movie", year = None):
    our_params = {
        "t": title,
        "type": type,
        "y": year,
        "apikey": "48ee7d00",
    }
    site = requests.get("http://www.omdbapi.com/", params=our_params)
    data = site.json()
    return data

