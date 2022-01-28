


class Playlist:
    # id
    # name
    # collaborative
    # description
    # spotify_url
    # owner_id
    # owner_spotify_url
    # owner_display_name
    # tracks_url
    # tracks_count
    # def __init__(self, id = 'spotify', name = 'spotify'):
    #     print('Playlist Model Class')


    def set_id(self, id):
        self.id = id
    def get_id(self):
        return self.id

    def set_name(self, name):
        self.name = name
    def get_name(self):
        return self.name

    def set_collaborative(self, collaborative):
        self.collaborative = collaborative
    def get_collaborative(self):
        return self.collaborative

    def set_description(self, description):
        self.description = description
    def get_description(self):
        return self.description

    def set_spotify_url(self, spotify_url):
        self.spotify_url = spotify_url
    def get_spotify_url(self):
        return self.spotify_url

    def set_owner_id(self, owner_id):
        self.owner_id = owner_id
    def get_owner_id(self):
        return self.owner_id
    
    def set_owner_spotify_url(self, owner_spotify_url):
        self.owner_spotify_url = owner_spotify_url
    def get_owner_spotify_url(self):
        return self.owner_spotify_url
    
    def set_owner_display_name(self, owner_display_name):
        self.owner_display_name = owner_display_name
    def get_owner_display_name(self):
        return self.owner_display_name

    def set_tracks_url(self, tracks_url):
        self.tracks_url = tracks_url
    def get_tracks_url(self):
        return self.tracks_url

    def set_tracks_count(self, tracks_count):
        self.tracks_count = tracks_count
    def get_tracks_count(self):
        return self.tracks_count
    
    def display(self):
        print('Id: ', self.id)
        print('Name: ', self.name)
