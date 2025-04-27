import hashlib
import hmac
import base64
from urllib.parse import urlencode, urlparse, urlunparse

def sign_url(base_url, params, secret):
    url_parts = urlparse(base_url)
    query = urlencode(params)

    url_to_sign = f"{url_parts.path}?{query}"

    decoded_secret = base64.urlsafe_b64decode(secret)
    signature = hmac.new(decoded_secret, url_to_sign.encode(), hashlib.sha1)
    
    encoded_signature = base64.urlsafe_b64encode(signature.digest()).decode()
    return f'{base_url}?{query}&signature={encoded_signature}'

