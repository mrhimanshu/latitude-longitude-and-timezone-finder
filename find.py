import time
import requests
from datetime import datetime
api_key = "AIzaSyC27SCqYDf9-JypKH33oKdaBSeIx-XvyhI"
g=[]
h=[]
i=1
addresses=input().strip().split()
addresses=([",".join(addresses)])
length=len(addresses)
import geocoder
for address in addresses:
    g = geocoder.google(str(address))
    latitude  = g.latlng[0]
    longitude = g.latlng[1]
    timestamp = time.time()


    api_response = requests.get('https://maps.googleapis.com/maps/api/timezone/json?location={0},{1}&timestamp={2}&key={3}'.format(latitude,longitude,timestamp,api_key))
    api_response_dict = api_response.json()

    if api_response_dict['status'] == 'OK':
        timezone_id = api_response_dict['timeZoneId']
        timezone_name = api_response_dict['timeZoneName']
        rawOffset = api_response_dict['rawOffset']
        dstOffset = api_response_dict['dstOffset']

        utc_dt = datetime.utcfromtimestamp(timestamp+dstOffset+rawOffset).strftime("%Y-%m-%e %I:%M:%S%p")
        timezone = datetime.utcfromtimestamp(timestamp+dstOffset+rawOffset).strftime("%I")
        timezone=int(timezone)*60+int(datetime.utcfromtimestamp(timestamp+dstOffset+rawOffset).strftime("%M"))
        j={'id':i,'address':address,'latitude':str(latitude),'longitude':str(longitude),'timezone':str(timezone),'UTC_time':str(utc_dt)}
        h.append(j)
        i=i+1
print(h)
