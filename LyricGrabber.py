#Uses musixmatch API to grab song lyrics

import requests
import json

apiroot='http://api.musixmatch.com/ws/1.1/'

grabber='track.lyrics.get?track_id='

apikey = "&apikey=c00142a8f220230892ebcc53784db989"

testid='15953433'

res = requests.get(apiroot + grabber + testid + apikey)



data = json.loads(res.content,encoding="UTF-8")



#def getLyrics(songID):
    
