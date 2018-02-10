#Uses musixmatch API to grab song lyrics

import requests
import json

apiroot='http://api.musixmatch.com/ws/1.1/'

grabber='track.lyrics.get?track_id='

mmapikey = "&apikey=c00142a8f220230892ebcc53784db989"

testid='15953433'



data = json.loads(res.content,encoding="UTF-8")



def getLyrics(songID):
    res = requests.get(apiroot + grabber + songID + mmapikey)
    data = json.loads(res.content,encoding="UTF-8")

    #Returns lyrics, separated with newline escapes. Disclaimer needs to be stripped.
    lyrics=data['message']['body']['lyrics']['lyrics_body']

    #Strip disclaimer and extra data:
    if lyrics.endswith('\n\n...\n\n******* This Lyrics is NOT for Commercial use *******'):
        return lyrics = lyrics[:len('\n\n...\n\n******* This Lyrics is NOT for Commercial use *******')]

    else:
        #panic - aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
        print('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')
        return 0

def getScore(lyrics)

    

    
    
    
    
