import requests
import time
import urllib3
from io import BytesIO
from PIL import Image, ImageDraw
import cognitive_face as CF
KEY = '9c4fc424129a4ff69dd74805848e2944'  # Replace with a valid subscription key (keeping the quotes in place).
CF.Key.set(KEY)
# If you need to, you can change your base API url with:
#CF.BaseUrl.set('https://westcentralus.api.cognitive.microsoft.com/face/v1.0/')
BASE_URL = 'https://eastus.api.cognitive.microsoft.com/face/v1.0'  # Replace with your regional Base URL
CF.BaseUrl.set(BASE_URL)
# You can use this example JPG or replace the URL below with your own URL to a JPEG image.

urllib3.disable_warnings()

#url1 = 'https://upload.wikimedia.org/wikipedia/commons/5/55/President_Barack_Obama%2C_2012_portrait_crop.jpg'
url2 = 'https://upload.wikimedia.org/wikipedia/commons/0/01/Poster-sized_portrait_of_Barack_Obama_OrigRes.jpg'
url3 = 'https://raw.githubusercontent.com/Microsoft/Cognitive-Face-Windows/master/Data/detection2.jpg'
url4 = 'http://images.glaciermedia.ca/polopoly_fs/1.23163993.1517704161!/fileImage/httpImage/image.jpg_gen/derivatives/landscape_804/justin-trudeau.jpg'
url5 = 'https://s-i.huffpost.com/gen/1279181/images/o-PRESIDENT-OBAMA-LA-facebook.jpg'
url6 = 'https://upload.wikimedia.org/wikipedia/commons/thumb/1/18/Ben_Carson_official_portrait.jpg/1200px-Ben_Carson_official_portrait.jpg'

urls = [url2, url3, url4, url5, url6]

results =[]
all_faceid = []

for url in urls:
    r = CF.face.detect(url)
    string = str(r)
    faceid = string[13:-76]
    results.append(r)
    all_faceid.append(faceid)
    
print(all_faceid)

test_url = 'https://upload.wikimedia.org/wikipedia/commons/9/9d/Barack_Obama.jpg'
test_result = CF.face.detect(test_url)
test_faceId = test_result[0]['faceId']

compresults = []

def test(idlist):
    for f in idlist: 
         r = CF.face.verify(f, test_faceId)
         print(r)
         if (CF.face.verify(f, test_faceId)['isIdentical'] == True) and (CF.face.verify(f, test_faceId)['confidence'] >= 0.6):
             compresults.append(1)
         else:
             compresults.append(0)
         time.sleep(1)

test(all_faceid)
print(compresults)

# print(faces)
# #Convert width height to a point in a rectangle
# def getRectangle(faceDictionary):
#     rect = faceDictionary['faceRectangle']
#     left = rect['left']
#     top = rect['top']
#     bottom = left + rect['height']
#     right = top + rect['width']
#     return ((left, top), (bottom, right))
# #Download the image from the url
# response = requests.get(img_url)
# img = Image.open(BytesIO(response.content))
# #For each face returned use the face rectangle and draw a red box.
# draw = ImageDraw.Draw(img)
# for face in faces:
#     draw.rectangle(getRectangle(face), outline='red')
# 
# #x = faces.faceLandmarks.pupilLeft.x
# #y = faces.faceLandmarks.pupilLeft.y
# #for i in range(x-3, x+6):
# #    for j in range(y-3, y+3):
# #        img[i,j]='red'
# 
# 
# 
# facestr= str(faces[0])
# faceidstr=facestr[12:-1256]
# pupilleftx=facestr[161:-1138]
# pupillefty=facestr[173:-1126]
# pupilrightx=facestr[201:-1098]
# pupilrighty=facestr[213:-1086]
# 
# 
# faceidlist = []
# faceidlist.append(faceidstr)
# 
# 
# 
# 
# 
# #Display the image in the users default image browser.
# img.show()

