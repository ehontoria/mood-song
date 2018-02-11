from cv2 import *
import indicoio
import json
import math
import SpotifyController
import scipy.misc

indicoKey ='aa4db01d2a72ceab00fd648d1c8d3583'

spot = SpotifyController.SpotifyControl()


f = open("finaldata.json")
songList = json.load(f)

indicoio.config.api_key = indicoKey
def getWebCamMood():
    
    cam = VideoCapture(0)
    s,img = cam.read()
    print("Image Captured - Processing")
          
    results = indicoio.analyze_image(img, apis=["fer"])

    #temp save
    scipy.misc.imsave("cap.jpg", img)
    
    return results['fer']


def findSong(mood):
    best = {}
    bestScore = 99999
    
    for i in songList:
        angerDiff = mood["Angry"] - i["mood"]["anger"]
        joyDiff = mood["Happy"] - i["mood"]["joy"]
        sadDiff = mood["Sad"] - i["mood"]["sadness"]
        fearDiff = mood["Fear"] - i["mood"]["fear"]
        surpriseDiff = mood["Surprise"] - i["mood"]["surprise"]

        score = math.sqrt(math.pow(angerDiff,2) + math.pow(joyDiff,2) + math.pow(sadDiff,2) + math.pow(fearDiff,2) + math.pow(surpriseDiff,2))
        
        if score < bestScore:
            bestScore = score
            best = i

    print()
    print("Finished.")
    print()
    print()
    print("Selected song: " + best["title"] + " by " + best["artist"])
    print()
    print("Your mood: " + str(mood))
    print("Songs mood: " + str(best["mood"]))
    print("Difference score: " + str(score))

    return best

def toSpot(songinfo):
    songID = spot.findSong(songinfo)
    spot.setSong(songID)
    spot.play()

    
toSpot(findSong(getWebCamMood()))


