import json
import handlers
import requests
from utility.utils import Utils

class AlbumHandler:

    def get_album_by_id(album_id):

        print('testing')
        url = handlers.BASE_URL+f'/albums/{album_id}'
        token = Utils.get_auth_token()
        headers = {
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/x-www-form-urlencoded"
        }
        print('url: ', url)
        print('header: ', headers)
        response = requests.get(url, headers=headers)
        print('output: ', json.loads(response.text))

    def get_all_albums():

        print('testing')
        url = handlers.BASE_URL+'/albums'
        token = Utils.get_auth_token()
        headers = {
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json"
        }
        print('url: ', url)
        print('header: ', headers)
        response = requests.get(url, headers=headers)
        print('output: ', json.loads(response.text))
        # print(response)

    def save_album(album_id):

        print('testing')
        url = handlers.BASE_URL+f'/me/albums'
        token = Utils.get_auth_token()
        headers = {
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json"
        }
        body = {
            "ids": [
                album_id
            ]
        }
        print('url: ', url)
        print('header: ', headers)
        response = requests.put(url, headers=headers, data=body)
        print('output: ', json.loads(response.text))
        
