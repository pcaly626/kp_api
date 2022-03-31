import requests
import enum
import base64

class Spotify_Urls(enum.Enum):
    GET_TOKEN ="https://accounts.spotify.com/api/token"


class Spotify:

    def __init__(self, client_id, client_secret):
        self.client_id = client_id
        self.client_secret = client_secret
        self.urls = Spotify_Urls

    def authenticate(self):
        auth = '%s:%s' % (self.client_id, self.client_secret)
        headers = {'Content-Type': 'application/x-www-form-urlencoded',
                   'Authorization': base64.b64encode(bytes(auth, 'utf-8'))}
        body = {'client_id': client_id,
                'grant_type': 'client_credientials'}
        return requests.post(self.urls.GET_TOKEN.value, headers=headers, body=body)
