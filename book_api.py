"""
This module deals with the Google Books API (getting the desired book's description)
"""

import urllib.request
import urllib.parse
import json


def get_book_description(book_name):
    """
    Based on the data, return an object of all books on
    the NYT Best Sellers lists
    """
    try:
        api_key = 'AIzaSyBkewrVqQj_6yzWovCUPcyzm2fXxJKmujU'

        url = f"https://www.googleapis.com/books/v1/volumes?q=intitle:{book_name}"

        # request = urllib.request.Request(url)
        response = urllib.request.urlopen(url)
        book_data = json.load(response)
        response.close()
        return book_data['items'][0]['volumeInfo']['description']
    except json.JSONDecodeError:
        return RuntimeError
    
