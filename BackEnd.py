from cv2 import *
import indicoio

indicoKey ='aa4db01d2a72ceab00fd648d1c8d3583'


cam = VideoCapture(0)

f = open("finaldata.json")
songList = json.dumps(f)

indicoio.config.api_key = indicoKey
def getWebCamMood():
    s,img = cam.read()
    print("image captured")
          
    results = indicoio.analyze_image(img, apis=["fer"])

    return results['fer']

print(getWebCamMood())


def findSong():
    
    
