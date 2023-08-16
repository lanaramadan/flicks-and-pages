import requests


def get_movie_image(movie_name):
    """
    Based on the movie name, return an image of the poster
    """

    url = f"https://moviesdatabase.p.rapidapi.com/titles/search/title/{movie_name}"

    querystring = {"exact":"true","titleType":"movie"}

    headers = {
        "X-RapidAPI-Key": "1564830b34mshee73b6d673e70a6p1f62afjsn9502fc6f202d",
        "X-RapidAPI-Host": "moviesdatabase.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring).json()

    # print("RESULTS:", response['results'][0]['primaryImage']['url'])
    try:
        return response['results'][0]['primaryImage']['url']
    except:
        return "No Image"