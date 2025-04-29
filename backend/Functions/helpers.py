from urllib.parse import urlencode
import requests

def validate_address_format(address, address_key):
    """
    Helper function to validate an address using Google's Address Validation API.
    """
    base_url = "https://addressvalidation.googleapis.com/v1:validateAddress"
    params = {
        "key": address_key,
    }
    url = f'{base_url}?{urlencode(params)}'

    # Make the API request
    response = requests.post(url, json={"address": address})
    google_data = response.json()

    # Extract and return the verdict along with the full response
    verdict = google_data.get("result", {}).get("verdict", {})
    return verdict, google_data