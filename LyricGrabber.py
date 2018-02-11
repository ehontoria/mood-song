#Uses musixmatch API to grab song lyrics

import requests
import json
import indicoio

apiroot='http://api.musixmatch.com/ws/1.1/'

grabber='track.lyrics.get?track_id='

mmapikey = "&apikey=c00142a8f220230892ebcc53784db989"

indicoKey ='aa4db01d2a72ceab00fd648d1c8d3583'

testid='15953433'


#config indico
indicoio.config.api_key = indicoKey


def getLyrics(songID):
    res = requests.get(apiroot + grabber + songID + mmapikey)
    data = json.loads(res.content,encoding="UTF-8")

    #Returns lyrics, separated with newline escapes. Disclaimer needs to be stripped.
    lyrics=data['message']['body']['lyrics']['lyrics_body']

    #Strip disclaimer and extra data:
    if lyrics.endswith('\n\n...\n\n******* This Lyrics is NOT for Commercial use *******'):
        return lyrics[:len('\n\n...\n\n******* This Lyrics is NOT for Commercial use *******')]

    else:
        return lyrics
        #panic - aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
        print('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')
       # return 0

def getScore(lyrics):
    emotionScore = indicoio.emotion(lyrics)
    return emotionScore
    

def removeNewline(lyrics):
    return lyrics.replace("\n",". ")
    
    
def get100Songs(page=1):
    #Returns list of songs, with dictionary of: title, artist, track ID no
    res = requests.get(apiroot + "chart.tracks.get?page=" + str(page) + "&page_size=100&f_has_lyrics=1" + mmapikey)
    data = json.loads(res.content,encoding="UTF-8")["message"]["body"]["track_list"]
    
    results = []

    for i in data:
        i = i["track"]

        results.append({"track_id":i["track_id"], "title":i["track_name"],"artist":i["artist_name"]})

    return results
    
