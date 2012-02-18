#! /usr/bin/python2.7
# -*- coding: utf-8 -*-

#Note this is _not_ the twitter module provided by easy_install or pip
#for the correct module check: http://code.google.com/p/python-twitter/
import twitter
import urllib,urllib2
import simplejson

#the url pointing to the json SpaceApi, for details check: https://hackerspaces.nl/spaceapi/
api_url = 'http://shackspace.de/spaceapi-query'
api = twitter.Api()
#create this at http://dev.twitter.com and make sure to give the app read _and_ write permissions
api = twitter.Api(
    consumer_key='XXXX',
    consumer_secret='XXXX',
    access_token_key='XXXX',
    access_token_secret='XXXX')


def update_status(condition):
    if condition == True:
        new_status = 'The space is now open, feel free to come by!'
    else:
        new_status = 'The space is now closed, but we\'ll be back soon.'
    api.PostUpdate(new_status)
def check_spaceapi():
    params = {'format':'json'}
    eparams = urllib.urlencode(params)
    s = urllib2.urlopen(api_url,eparams)
    r = s.read()
    r = r.strip()
    get_status(r)

def get_status(json_data):
    data = simplejson.loads(json_data)
    #The open key should return a boolean from the SpaceApi. 
    #If it doesn't either fix your SpaceAPI or this code.
    update_status(data['open'])

check_spaceapi()
