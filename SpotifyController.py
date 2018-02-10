import spotipy
import spotipy.util as util


#Auth information - super duper top secret 'kay?
SPOTIPY_CLIENT_ID="1dd9a22efd17418da5db84567d91208e"
SPOTIPY_CLIENT_SECRET="2efe887783454bae8aa67492d33b4ddc"
SPOTIPY_REDIRECT_URI="http://localhost/"

scopeType = 'user-modify-playback-state,user-read-currently-playing'

class SpotifyController:
    def __init__(self, username="electriczap4"):
        token = util.prompt_for_user_token(username, client_id=SPOTIPY_CLIENT_ID,client_secret=SPOTIPY_CLIENT_SECRET,redirect_uri=SPOTIPY_REDIRECT_URI,scope = scopeType)
        self.spot = spotipy.Spotify(auth=token)
        
        
    def pause(self):
        try:
            self.spot.pause_playback()
        except  spotipy.client.SpotifyException:
            print("Already paused.")

    def play(self):
        try:
            self.spot.start_playback()
        except  spotipy.client.SpotifyException:
            print("Already playing.")

    def setSong(self,songUri):
        self.spot.start_playback(uris=[songUri])
        self.play()
                


