from api import API

a = API()
j = a.get_apis()
for api in j['items']:
    print api
