from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt
from elasticsearch import Elasticsearch
import os
import requests
import json
es = Elasticsearch()


__author__ = 'Asus'
from TwitterAPI import TwitterAPI
import nltk



def index(request):
    #return HttpResponse("hi")
    #context = {'username': 'Cat'}
    return render_to_response('index.html', context_instance = RequestContext(request))

@csrf_exempt
def update_likes(request):
    #import pdb; pdb.set_trace()
    if request.method == "POST":
        
        _dir = request.POST['_dir']
        _id = request.POST['_id']
        if _dir == "up":
            weight = 1
        else:
            weight = -1
        url = "http://localhost:9200/blog_index/doc/%s/_update" % _id
        data = {
                "script":"ctx._source.likes+=%d" % weight
                }
        requests.post(url, json=data)
        return HttpResponse("")
    else:
        return HttpResponse("")

@csrf_exempt
def search(request):
    if request.method == "POST":
        term = request.POST['term']
        data = {"query":{
  "function_score": {
    "query": 
                                                             {"match": 
                                                                {"title":term}
                                                     },
    "functions": [
        {
            "script_score": {
              "script" : "_score / (1 + pow(1.5,(-doc['likes'].value)) )"
            }
        }
    ],
    "max_boost": 100,
    "score_mode": "max",
    "boost_mode": "replace",
    "min_score" : 0
  }
}
}
        #pro
        #command = "curl XGET localhost:9200/blog_index/doc/_search -d '{\"query\":{\"custom_score\":{\"query\":{\"match\":{\"title\":%s}},\"script\":\"_score * (doc['likes'].value)\"}}}' " % term
        url = "http://localhost:9200/blog_index/doc/_search"
        json_item = json.loads(requests.post(url, json=data).text)

        prodocs = [elem['_source'] for elem in json_item['hits']['hits']]
        for index,doc in enumerate(prodocs):
            prodocs[index]['body'] = prodocs[index]['body'][:250]
            prodocs[index]['Id'] = json_item['hits']['hits'][index]['_id']
        #avg
        avgdocs = []
        #consumer_key, consumer_secret, access_token_key, access_token_secret
        api = TwitterAPI("tmNbyIDjNn1SkEPJENTUy9XUC",
                 "raddZenV7CaOiR29akB0DlabmpFUwPVY1V4qZHQwRFGyqacKT3",
                 "3051564974-ancG9igjFccXFMLe0k8OMTVmW5euR8hES4NFnRM",
                 "XxU9lcVtnjHeYiHtSxIvqE3ub6cEgI6HBriwW4eYlfVvl")
        r = api.request('search/tweets', {'q':term,'count':'5','lang':'en'})
        response = r.json()
        for post in response["statuses"]:
            url = "https://twitter.com/%s/status/%d" % (post['user']['screen_name'], post['id'])
            avgdocs.append({'created_at':post['created_at'],'user':post['user']['screen_name'],'source':url,'text':post['text']})
    else:
        prodocs,avgdocs = [],[]
    #return HttpResponse("hi")
    #context = {'username': 'Cat'}
    return render_to_response('result.html',{'prodocs':prodocs,'avgdocs':avgdocs}, context_instance = RequestContext(request))