##provisional

import InstagramAPI

client_id='b460411fcea54457b70d03cdd52c0a9a'
client_secret='0dc3e870ff414c0199b7f13645996bd3'

Instagram=InstagramAPI.Instagram_API(client_id,client_secret)
print 'Instagram.getPhotos("@snoopdog",1,2)'
print Instagram.getPhotos("@snoopdog",1,2)
print 'Instagram.getPhotos("#sun",1,99999,False)'
print Instagram.getPhotos("#sun",1,99999,False)
