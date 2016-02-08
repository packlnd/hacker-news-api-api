import urllib2
import json
import re

#https://developer.github.com/v3/search/

class API:
    def __init__(self):
        raw_json = get_from_github("hacker-news-api")
        json = filter(raw_json)
        for j in json:
            print j

    def filter(j):
        filtered_json = []
        print j['total_count']
        print len(j['items'])
        for repo in j['items']:
            if not is_api(repo):
                next
            item = {#'id':repo['id'],
                    'name':repo['name'],
                    #'full_name':repo['full_name'],
                    #'url':repo['html_url'],
                    'desc':repo['description']}#,
                    #'created':repo['created_at'],
                    #'stars':repo['stargazers_count'],
                    #'open_issues':repo['open_issues_count'],
                    #'score':repo['score']}
            filtered_json.append(json.dumps(item))
        print len(filtered_json)
        return filtered_json

    def get_from_github(q):
        api_string = urllib2.urlopen("https://api.github.com/search/repositories?" + \
                                     "q=" + q + "&" + \
                                     "sort=stars&" + \
                                     "order=desc").read()
        return json.loads(api_string)

    def is_api(repo):
        words = re.findall(r"[\w']+", repo['description'])
        return 'hacker' in words and 'news' in words and 'api' in words

    def get_endpoints(aid):
        raise NotImplementedError

    def get_statistics(aid):
        raise NotImplementedError
