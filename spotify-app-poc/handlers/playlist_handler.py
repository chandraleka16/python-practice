import imp
import json
import handlers
import requests
from utility.utils import Utils
from models.playlist import Playlist
from prettytable import PrettyTable

class PlaylistHandler:

    def __init__(self):
        self.utils = Utils()

    def get_playlist_by_id(self, refresh_token):

        print('Get Playlist by Id\n')
        playlist_id = input('Enter the Playlist Id: ')
        url = handlers.BASE_URL+f'/playlists/{playlist_id}'
        # scopes = f'{handlers.PLAYLIST_READ_PUBLIC} {handlers.PLAYLIST_READ_PRIVATE}'
        token = self.utils.get_token_by_auth_code(refresh_token)
        headers = {
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/x-www-form-urlencoded"
        }
        response = requests.get(url, headers=headers)
        # print(response)
        # print('output: ', json.loads(response.text))
        playlist_response = json.loads(response.text)
        playlist = Playlist()
        playlist.set_id(playlist_response['id'])
        playlist.set_name(playlist_response['name'])
        playlist.set_description(playlist_response['description'])
        playlist.set_collaborative(playlist_response['collaborative'])
        playlist.set_spotify_url(playlist_response['external_urls']['spotify'])
        playlist.set_owner_id(playlist_response['owner']['id'])
        playlist.set_owner_display_name(playlist_response['owner']['display_name'])
        playlist.set_owner_spotify_url(playlist_response['owner']['external_urls']['spotify'])
        playlist.set_tracks_url(playlist_response['tracks']['href'])
        playlist.set_tracks_count(playlist_response['tracks']['total'])

        # for play in my_playlists:
        #     print("Id: ", play.get_id(), "Name: ", play.get_name())

        playlist_data = PrettyTable(
            ['Id', 'Name', 'Description', 'Spotify URL', 'Owner Id', 'Owner Spotify URL', 'Owner Name', 'Tracks URL',
             'Tracks Count'])
        playlist_data.add_row(
            [playlist.get_id(), playlist.get_name(), playlist.get_description(), playlist.get_spotify_url(),
             playlist.get_owner_id(), playlist.get_owner_spotify_url(), playlist.get_owner_display_name(),
             playlist.get_tracks_url(), playlist.get_tracks_count()])
        print(playlist_data)


    def get_my_playlists(self, refresh_token):

        print('Get My Own Playlist\n')
        url = handlers.BASE_URL+'/me/playlists'
        # scopes = f'{handlers.PLAYLIST_READ_PRIVATE}'
        token = self.utils.get_token_by_auth_code(refresh_token)
        headers = {
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json"
        }
        # print('url: ', url)
        # print('header: ', headers)
        response = requests.get(url, headers=headers)
        # print(response)
        # print('output: ', json.loads(response.text))
        playlist_response = json.loads(response.text)
        my_playlists = []
        for item in playlist_response['items']:
            playlist = Playlist()
            playlist.set_id(item['id'])
            playlist.set_name(item['name'])
            playlist.set_description(item['description'])
            playlist.set_collaborative(item['collaborative'])
            playlist.set_spotify_url(item['external_urls']['spotify'])
            playlist.set_owner_id(item['owner']['id'])
            playlist.set_owner_display_name(item['owner']['display_name'])
            playlist.set_owner_spotify_url(item['owner']['external_urls']['spotify'])
            playlist.set_tracks_url(item['tracks']['href'])
            playlist.set_tracks_count(item['tracks']['total'])

            my_playlists.append(playlist)

        # for play in my_playlists:
        #     print("Id: ", play.get_id(), "Name: ", play.get_name())

        playlist_data = PrettyTable(
            ['Id', 'Name', 'Description', 'Spotify URL', 'Owner Id', 'Owner Spotify URL', 'Owner Name', 'Tracks URL',
             'Tracks Count'])
        for play in my_playlists:
            playlist_data.add_row(
                [play.get_id(), play.get_name(), play.get_description(), play.get_spotify_url(), play.get_owner_id(),
                 play.get_owner_spotify_url(), play.get_owner_display_name(), play.get_tracks_url(),
                 play.get_tracks_count()])
        print(playlist_data)


    def update_playlist_details(self):
        print('Update Playlist Details\n')
        playlist_id = input('Enter the Playlist Id: ')
        print('Enter the following details to update:\n')
        playlist_name = input('Playlist Name:')
        playlist_desc = input('Playlist Description:')
        playlist_public = input('Playlist Public Access (True/False): ')
        if playlist_public.lower() == 'true':
            is_public = True
        else:
            is_public = False
        payload = json.dumps({
            "name": playlist_name,
            "description": playlist_desc,
            "public": is_public
        })
        print('payload: ', payload)
        url = handlers.BASE_URL+f'/playlists/{playlist_id}'
        # scopes = f'{handlers.PLAYLIST_MODIFY_PRIVATE} {handlers.PLAYLIST_MODIFY_PUBLIC}'
        token = input('For creating new playlist, please enter OAuth Token: ')
        headers = {
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json"
        }
        print('url: ', url)
        print('header: ', headers)
        response = requests.put(url, headers=headers, data=payload)
        print('response: ', response)
        # playlist_response = json.loads(response.text)
        # print('output: ', playlist_response)
        # if 'Response [200]' in response:
        #     print('Updated the Playlist Successfully!\n')
        # else:
        #     print('Something went wrong!\n')


    def delete_playlist_items(self):

        print('Delete Playlist Items\n')
        playlist_id = input('Enter the Playlist Id: ')
        url = handlers.BASE_URL+f'/playlists/{playlist_id}/tracks'
        scopes = f'{handlers.PLAYLIST_MODIFY_PRIVATE} {handlers.PLAYLIST_MODIFY_PUBLIC}'
        token = input('For creating new playlist, please enter OAuth Token: ')
        # token = self.utils.get_token_by_auth_code(scopes)
        headers = {
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json"
        }
        print('url: ', url)
        print('header: ', headers)
        response = requests.delete(url, headers=headers)
        print('response: ', response)
        playlist_response = json.loads(response.text)
        if 'snapshot_id' in playlist_response.keys():
            print('Created the Playlist Successfully!\n')
        # if '200' in response:
        #     print('Created the Playlist Successfully!\n')
        else:
            print('Something went wrong!\n')
        print('output: ', json.loads(response.text))

    def create_playlist(self):

        print('Create a New Playlist\n')
        user_id = input('Enter the User Id: ')
        print('Enter the following details to update:\n')
        playlist_name = input('Playlist Name:')
        playlist_desc = input('Playlist Description:')
        playlist_public = input('Playlist Public Access (True/False): ')
        if playlist_public.lower() == 'true':
            is_public = True
        else:
            is_public = False
        payload = json.dumps({
            "name": playlist_name,
            "description": playlist_desc,
            "public": is_public
        })
        print('payload: ', payload)
        url = handlers.BASE_URL+f'/users/{user_id}/playlists'
        # scopes = f'{handlers.PLAYLIST_MODIFY_PRIVATE} {handlers.PLAYLIST_MODIFY_PUBLIC}'
        token = input('For creating new playlist, please enter OAuth Token: ')
        # token = self.utils.relogin_myspotify()
        headers = {
            "Accept": "application/json",
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json"
        }
        print('url: ', url)
        print('header: ', headers)
        response = requests.post(url, headers=headers, data=payload)
        playlist_response = json.loads(response.text)
        if 'id' in playlist_response.keys():
            print('Created the Playlist Successfully!\nThe Playlist Id: ', playlist_response['id'])
        else:
            print('Something went wrong!\n')

        print('output: ', json.loads(response.text))
        
