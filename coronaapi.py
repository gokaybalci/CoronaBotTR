import requests

BASE_URL = "https://api.covid19api.com"

VAKA = "/total/country/turkey/status/confirmed"
IYILESEN = "/total/country/turkey/status/recovered"
OLUM = "/total/country/turkey/status/deaths"

def build_url(endpoint):
    """
    Build the final request URL for an endpoint.
    """
    
    if not endpoint:
        return None

    return BASE_URL + endpoint

def make_request(url, parameters = None):
    """
    Performs a request to the API, handling errors in the process.
    """
    try:
        r = requests.get(url = build_url(url), params = parameters)
    except:
        return "Error: Failed to retrieve data."

    try:
        data = r.json()
    except:
        return "Error: Retrieved unexpected data."

    return data

def fetch_vaka():

    return make_request(VAKA)

def fetch_iyilesen():

    return make_request(IYILESEN)

def fetch_olum():

    return make_request(OLUM)