# getInfo(name, year)
# image =
# year
# rating

# data = getInfo(name,year)
# data.image

import requests
import json


def get_media_info(title:str, type:str="movie", year:int=None) -> dict:
    """
    Get the information for some media based on its title.
    """

    our_params = {
        "t": title,
        "type": type,
        "y": year,
        "apikey": "48ee7d00",
    }
    site = requests.get("http://www.omdbapi.com/", params=our_params)
    data = site.json()
    return data


def get_stream_locations(query:str, location:str) -> dict:
    url_location = {
        "UK": "en_GB",
        "USA": "en_US",
        "AUS": "en_AU",
    }[location]
    url = f"https://apis.justwatch.com/content/titles/{url_location}/popular"

    params = {
        "language": "en",
        "body": json.dumps({
            "page_size":5,
            "page":1,
            "query":query,
            "content_types":["show","movie"]
        })
    }

    site = requests.get(url, params=params)
    data = site.json()
    movie = data['items'][0]
    movie_name = movie['title']
    poster = movie['poster']
    free_provider_urls = [i['urls']['standard_web'] for i in [o for o in movie['offers'] if o['monetization_type'] == 'flatrate']]

    return {
        "title": movie_name,
        "poster": f"https://images.justwatch.com{poster.format(profile='s276')}/.jpg",
        "providers": list(set(free_provider_urls)),
    }
