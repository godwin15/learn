import requests
import spotipy

CLIENT_ID = '8bf32fefc80749ebaf4d999f33b71679'
CLIENT_SECRET = '45556c5c0fa440d19ff98fbad1ce2718'

#authenticate to start using spotify api
AUTH_URL = 'https://accounts.spotify.com/api/token'
#store everything after we get authentication request to spotify
auth_response = requests.post(AUTH_URL, {
	'grant_type': 'client_credentials',
	'client_id': CLIENT_ID,
	'client_secret': CLIENT_SECRET,
})

print(auth_response.status_code)

auth_response_data = auth_response.json()

print(auth_response_data)

access_token = auth_response_data['access_token']

headers = {
	'Authorization': 'Bearer {token}'.format(token=access_token)}

BASE_URL ='https://api.spotify.com/v1/'