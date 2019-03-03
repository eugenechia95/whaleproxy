from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, HttpResponseRedirect
import requests
from django.views.decorators.cache import cache_page
from django.core.cache import cache
from django import http
from django.conf import settings
import datetime, re
from django.http import JsonResponse
import ast

whaletoken = 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE1ODMxOTkzMTQsImlkIjoiRXVnZW5lX0NoaWFAbXltYWlsLnN1dGQuZWR1LnNnIiwib3JpZ19pYXQiOjE1NTEwNTg1MTR9.kNx9zaYjQAyn6dQSxdTIQHVoy9K1h32Bm5MTxXj91Iw'


# Create your views here.
@csrf_exempt
def getview(request):
    authorization_token = request.META.get('HTTP_AUTHORIZATION')
    print(authorization_token)
    if authorization_token != whaletoken:
        return HttpResponse(status = 401)

    cache_key = '100ab45hfc' # needs to be unique
    cache_time = 86400 # time in seconds for cache to be valid

    #GET Request returns dictionary of all whale instances
    if request.method == 'GET':
        data = cache.get(cache_key) # returns None if no key-value pair
        if data:
            print("Fetching from Cache")
            return HttpResponse(status = data.status_code, content = data.text)
        if not data:
            print("Not in Cache. Fetching from Server")
            url = 'https://whalemarket.saleswhale.io/whales'
            urlheaders = {}
            urlheaders['Authorization'] = authorization_token
            response = requests.get(url, headers = urlheaders)
            cache.set(cache_key, response, cache_time)
            return HttpResponse(status = response.status_code, content=response.text)

        #url = 'https://whalemarket.saleswhale.io/whales'
        #urlheaders = {}
        #urlheaders['Authorization'] = 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE1ODMxOTkzMTQsImlkIjoiRXVnZW5lX0NoaWFAbXltYWlsLnN1dGQuZWR1LnNnIiwib3JpZ19pYXQiOjE1NTEwNTg1MTR9.kNx9zaYjQAyn6dQSxdTIQHVoy9K1h32Bm5MTxXj91Iw'
        #response = requests.get(url, headers = urlheaders)
        #x = HttpResponse(status = response.status_code,content=response.text)
        #return HttpResponse(x)

    #POST Request creates new whale instance in whalemarket
    elif request.method == 'POST':
        url = 'https://whalemarket.saleswhale.io/whales'
        datadict = ast.literal_eval(request.body.decode('utf-8'))
        urlheaders = {}
        urlheaders['Authorization'] = authorization_token
        #return HttpResponse(status = 400)
        y = requests.post(url, json = datadict, headers = urlheaders)
        return HttpResponse(y)

    #DELETE Request purges cache of service
    elif request.method == 'DELETE':
        cache.clear()
        print('Cache Purged Successfully')
        return HttpResponse(status = '204')

    #PUT Request forces a sync of every whale in whalemarket
    elif request.method == 'PUT':
        print('Syncing all whales in cache')
        data = cache.get(cache_key)
        url = 'https://whalemarket.saleswhale.io/whales'
        urlheaders = {}
        urlheaders['Authorization'] = authorization_token
        response = requests.get(url, headers = urlheaders)
        cache.set(cache_key, response, cache_time)
        responselist = ast.literal_eval(response.text)
        whaleslist = responselist.get('whales')

        for whale in whaleslist:
            whaleid = whale.get('id')
            print(whaleid)
            newurl = url + '/' + str(whaleid)
            print(newurl)
            response = requests.get(newurl, headers = urlheaders)
            print(response)
            cache_key = whaleid
            cache.set(cache_key, response, cache_time)

        print('All Whales Synced!')

        return HttpResponse(status = '200', content= "All Whales Synced!")

#GET Request returns whale instance corresponding to id in argument.
@csrf_exempt
def getidview(request, id):
    authorization_token = request.META.get('HTTP_AUTHORIZATION')
    print(authorization_token)
    if authorization_token != whaletoken:
        return HttpResponse(status = 401)

    cache_key = id # needs to be unique
    cache_time = 86400 # time in seconds for cache to be valid

    if request.method == 'GET':
        data = cache.get(cache_key) # returns None if no key-value pair
        if data:
            print("Fetching from Cache")
            return HttpResponse(status = data.status_code, content = data.text)
        if not data:
            print("Not in Cache. Fetching from Server")
            url = 'https://whalemarket.saleswhale.io/whales/' + id
            urlheaders = {}
            urlheaders['Authorization'] = authorization_token
            response = requests.get(url, headers = urlheaders)
            cache.set(cache_key, response, cache_time)
            return HttpResponse(status = response.status_code, content=response.text)

@csrf_exempt
def hitratio(request):
    authorization_token = request.META.get('HTTP_AUTHORIZATION')
    print(authorization_token)
    if authorization_token != whaletoken:
        return HttpResponse(status = 401)

    cachestats = cache._cache.get_stats()[0][1]
    hits = int(cachestats.get('get_hits'))
    total_retrievals = int(cachestats.get('cmd_get'))
    if total_retrievals == 0:
        hitratio = 0
    else:
        hitratio = hits/total_retrievals*100
    outcome = ('Total Retrieval Request: %d \nTotal Cache Hits: %d \nCache Hit Ratio: %.2f' % (total_retrievals, hits, hitratio) + '%')
    return HttpResponse(status = 200, content = outcome)