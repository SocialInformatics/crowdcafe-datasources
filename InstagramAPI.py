from lib.instagram_lbs.instagram import client, subscriptions
from lib.instagram_lbs.instagram.client import InstagramAPI
import urllib2

class Instagram_API(object):
	
	def __init__(self,client_id,client_secret):
                self.client_id=client_id
                self.client_secret=client_secret
		self.api = InstagramAPI(self.client_id, self.client_secret)

## Gets the user ID from the given username
## I suppose it would be better to use some kind of json library
	def getUserID(self,username):
		url='https://api.instagram.com/v1/users/search?q='+username+'&client_id='+self.client_id
		response = urllib2.urlopen(url)
		html = response.read()
		html=html.split('"')
		return html[len(html)-2] 

## Method to get the photos from a keyword	
	def getPhotos(self, keyword, amount, last_photoid, new=True):
		photos=[]
		if keyword[0]=="@":
			keyword=keyword.split('@',1)
			uid=self.getUserID(keyword[1])
			if new == True:
				user_media = self.api.user_recent_media(user_id=uid, count=amount, min_id=last_photoid)
			else:
				user_media = self.api.user_recent_media(user_id=uid, count=amount, max_id=last_photoid)
			return user_media
		elif keyword[0]=="#":
			keyword=keyword.split('#',1)
			if new == True:
				hash_media = self.api.tag_recent_media(count=amount, min_id=last_photoid, tag_name=keyword[1])
			else:
				hash_media = self.api.tag_recent_media(count=amount, max_id=last_photoid, tag_name=keyword[1])
			return hash_media
				
		else:
			print "Error, you have to provide either an @username or an #hashtag"



		


