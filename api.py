import urllib2
import json
import re

#https://developer.github.com/v3/search/

class API:
    def get_apis(self):
        raw_json = self.get_from_github("hacker-news-api")
        json = self.filter(raw_json)
        return json

    def filter(self, j):
        filtered_json = []
        print j['total_count']
        print len(j['items'])
        for repo in j['items']:
            if self.is_api(repo):
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

    def get_from_github(self, q):
        api_string = urllib2.urlopen("https://api.github.com/search/" +\
                                     "repositories?" +\
                                     "q=" + q + "&" +\
                                     "sort=stars&" +\
                                     "order=desc&" +\
                                     "per_page=100").read()
        return json.loads(api_string)

    def is_api(self, repo):
        # change to point-based feature system.
        words = [w.lower() for w in re.findall(r"[\w']+", repo['description'])]
        return 'firebase' not in words and \
               'hacker' in words and \
               'news' in words and \
               'api' in words

    def get_endpoints(self, aid):
        raise NotImplementedError

    def get_statistics(self, aid):
        raise NotImplementedError
