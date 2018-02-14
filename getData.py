import requests
import json
import datetime


now = datetime.datetime.now()
date =now.strftime("%Y-%m-%d")

token='eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiI2RlFRS1giLCJhdWQiOiIyMkNMVFIiLCJpc3MiOiJGaXRiaXQiLCJ0eXAiOiJhY2Nlc3NfdG9rZW4iLCJzY29wZXMiOiJyaHIgcnNsZSIsImV4cCI6MTUxOTAxMzQ4MiwiaWF0IjoxNTE4NDMwMTY5fQ.Kx5CBJ0RFgoWW80VOMdDrXCjaHJKMZUXqaEkV1-zdLo'

#fill user id with your user id
url = 'https://api.fitbit.com/1.2/user/"user id"/sleep/list.json?afterDate='+ date +'&limit=1&offset=0&sort=asc'

filename = 'SleepData'+ date +'.json'
response = requests.get(url=url, headers ={'Authorization':'Bearer ' + token})
if response.ok:
    with open(filename, 'w') as f:
        # json.dump(response.content, f)
        f.write(response.content)
    print ('Sleep data '+date + ' is saved!')

else:
    print ('The file of %s is not saved due to error!' % date)
json_data = json.loads(response.content)

i = 0
for each in json_data["sleep"][0]["levels"]["data"]:
    print ("Level:\t"+each["level"])
    print ("Time:\t"+each["dateTime"])

print
print("program ended")
