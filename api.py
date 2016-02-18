import urllib2
import json
import re

#https://developer.github.com/v3/search/

class API:
    def get_apis(self):
        apis = []
        page = 1
        while True:
            raw_json = self.get_from_github("hacker-news-api", page)
            if not len(raw_json['items']):
                break
            page += 1
            apis.extend(self.filter(raw_json))
        self.apis = {'items':apis, 'count':len(apis)}
        return self.apis

    def filter(self, j):
        filtered_json = []
        for repo in j['items']:
            if self.is_api(repo):
                item = {'id':repo['id'],
                        'desc':repo['description'],
                        'name':repo['name'],
                        'full_name':repo['full_name'],
                        'url':repo['html_url'],
                        'created':repo['created_at'],
                        'stars':repo['stargazers_count'],
                        'open_issues':repo['open_issues_count'],
                        'score':repo['score']}
                filtered_json.append(json.dumps(item))
        return filtered_json

    def get_from_github(self, q, p):
        api_string = urllib2.urlopen("https://api.github.com/search/" +\
            "repositories?" +\
            "q=" + q + "&" +\
            "sort=stars&" +\
            "order=desc&" +\
            "page=" + str(p) + "&" +\
            "per_page=100").read()
        return json.loads(api_string)

    def word_distance(self, words, word_list):
        for w in word_list:
            if not w in words:
                return False
        ind = {w:i for i,w in enumerate(words)}
        dist = [abs(ind[w1]-ind[w2]) for w1 in word_list for w2 in word_list]
        for d in dist:
            if d > 3:
                return False
        return True

    def is_api(self, repo):
        # change to point-based feature system.
        words = [w.lower() for w in re.findall(r"[\w']+", repo['description'])]
        dist = self.word_distance(words, ['hacker','news','api'])
        if not dist:
            return False
        return 'firebase' not in words and \
               'app' not in words and \
               'ios' not in words and \
               'wrapper' not in words and \
               'android' not in words and \
               'hacker' in words and \
               'news' in words and \
               'api' in words

    def get_endpoints(self, aid):
        api = {}
        for a in self.apis:
            if a['id'] != aid:
                next
            api = a
        # Find endpoints

    def get_statistics(self, aid):
        raise NotImplementedError
