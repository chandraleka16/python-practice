import base64
import json
import utility
import requests
from urllib.parse import quote


class Utils:
    refresh_token = ""
    
    def get_token_by_creds(self, scopes):
        
        print('Login')
        url = utility.LOGIN_BASE_URL+'/api/token'
        # creds = utility.CLIENT_ID + ':' + utility.CLIENT_SECRET
        # authorization = base64.b64encode(creds.encode()).decode()
        # headers = {
        #     "Authorization": f"Basic {authorization}",
        #     "Content-Type": "application/x-www-form-urlencoded"
        # }
        body = {
            "grant_type": "client_credentials",
            "scopes": "playlist-read-public"
        }
        print('url: ', url)
        print('body: ', body)
        # print(authorization)
        # response = requests.post(url, data=body, headers=headers, json=True)
        response = requests.post(url, data=body, auth = (utility.CLIENT_ID, utility.CLIENT_SECRET)) 
        print(response)
        token_raw = json.loads(response.text)
        # print(token_raw)
        print(token_raw["access_token"])
        return token_raw["access_token"]

    def get_token_by_auth_code(self, refresh_token):
        # encoded_scopes = quote(scopes)
        # auth_redirect_url = f'{utility.LOGIN_BASE_URL}/authorize?response_type=code&client_id={utility.CLIENT_ID}&redirect_uri={utility.CALLBACK_URI}&scopes={encoded_scopes}'
        refresh_url = utility.LOGIN_BASE_URL+'/api/token'
        auth_header = base64.b64encode((utility.CLIENT_ID + ':' + utility.CLIENT_SECRET).encode('ascii'))
        headers = {'Authorization': 'Basic %s' % auth_header.decode('ascii')}
        # print ("---  " + auth_redirect_url + "  ---")
        # auth_code = input('code: ')
        print('refresh_token: ', refresh_token)
        payload = {
            'refresh_token': refresh_token,
            'grant_type': 'refresh_token'
        }
        print("requesting refresh token")
        print(payload)
        refresh_token_response = requests.post(refresh_url, data=payload, headers=headers)

        # print ("response")
        print(refresh_token_response.headers)
        raw_res = json.loads(refresh_token_response.text)
        print('body: ', raw_res)
        print('token: ', raw_res['access_token'])
        return raw_res['access_token']

    def login_myspotify(self):
        scopes = f'{utility.PLAYLIST_MODIFY_PRIVATE} {utility.PLAYLIST_MODIFY_PUBLIC} {utility.PLAYLIST_READ_PRIVATE} {utility.PLAYLIST_READ_PUBLIC}'
        encoded_scopes = quote(scopes)

        auth_redirect_url = f'{utility.LOGIN_BASE_URL}/authorize?response_type=code&client_id={utility.CLIENT_ID}&redirect_uri={utility.CALLBACK_URI}&scopes={encoded_scopes}'
        token_url = utility.LOGIN_BASE_URL+'/api/token'
        print ("---  " + auth_redirect_url + "  ---")
        auth_code = input('code: ')

        data = {'grant_type': 'authorization_code', 'code': auth_code, 'redirect_uri': utility.CALLBACK_URI}
        print ("requesting access token")
        access_token_response = requests.post(token_url, data=data, verify=False, allow_redirects=False, auth=(utility.CLIENT_ID, utility.CLIENT_SECRET))

        # print ("response")
        print (access_token_response.headers)
        raw_res = json.loads(access_token_response.text)
        print('body: ', raw_res)
        print('token: ', raw_res['access_token'])
        self.access_token = raw_res['access_token']
        self.refresh_token = raw_res['refresh_token']

        return self.refresh_token

    def relogin_myspotify(self):
        scopes = f'{utility.PLAYLIST_MODIFY_PRIVATE} {utility.PLAYLIST_MODIFY_PUBLIC}'
        encoded_scopes = quote(scopes)

        auth_redirect_url = f'{utility.LOGIN_BASE_URL}/authorize?response_type=code&client_id={utility.CLIENT_ID}&scopes=playlist-modify-private&redirect_uri={utility.CALLBACK_URI}'
        token_url = utility.LOGIN_BASE_URL+'/api/token'
        print ("---  " + auth_redirect_url + "  ---")
        auth_code = input('code: ')

        data = {'grant_type': 'authorization_code', 'code': auth_code, 'redirect_uri': utility.CALLBACK_URI}
        print ("requesting access token")
        access_token_response = requests.post(token_url, data=data, verify=False, allow_redirects=False, auth=(utility.CLIENT_ID, utility.CLIENT_SECRET))

        # print ("response")
        print (access_token_response.headers)
        raw_res = json.loads(access_token_response.text)
        print('body: ', raw_res)
        print('token: ', raw_res['access_token'])
        self.access_token = raw_res['access_token']
        self.refresh_token = raw_res['refresh_token']

        return self.access_token

    # def display_data(self, data):
    #     print(data)
    #     # id
    #     # name
    #     # collaborative
    #     # description
    #     # spotify_url
    #     # owner_id
    #     # owner_spotify_url
    #     # owner_display_name
    #     # tracks_url
    #     # tracks_count
    #
    #     # df = pd.DataFrame(data, columns = ['Id','Name','Description', 'Spotify URL', 'Owner Id', 'Owner Spotify URL', 'Owner Name', 'Tracks URL', 'Tracks Count'])
    #     playlist_data = PrettyTable(
    #         ['Id', 'Name', 'Description', 'Spotify URL', 'Owner Id', 'Owner Spotify URL', 'Owner Name', 'Tracks URL',
    #          'Tracks Count'])
    #     for play in data:
    #         playlist_data.add_row(play.)
    #     print(playlist_data)





    