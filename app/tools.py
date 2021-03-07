from fastapi import HTTPException
import requests

def connection(url, **kwargs):
    """
    Args: (url)
    Return: response_data
    function to fetch data to PokeAPI
    """
    if kwargs:
        response = requests.get(url, params=kwargs)
        if response.status_code != 200:
            raise HTTPException(status_code=404, detail="data not found")
    else:
        response = requests.get(url)
        if response.status_code != 200:
            raise HTTPException(status_code=404, detail="Pokemon name not found")

    return response
