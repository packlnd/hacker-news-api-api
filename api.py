import urllib2
import json

#https://developer.github.com/v3/search/

def get_apis():
    raw_json = get_from_github("hacker-news-api")

def get_from_github(q):
    api_string = urllib2.urlopen("https://api.github.com/search/repositories?" + \
                                 "q=" + q + "&" + \
                                 "sort=stars&" + \
                                 "order=desc").read()
    return json.loads(api_string)

def get_endpoints(aid):
    raise NotImplementedError

def get_statistics(aid):
    raise NotImplementedError
