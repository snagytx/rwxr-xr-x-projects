import urllib,urllib2,re,xbmcplugin,xbmcgui,xbmcaddon,os,socket
from subprocess import check_output 

sopdatapath = 'special://profile/addon_data/plugin.video.sopvid'
selfAddon = xbmcaddon.Addon(id='plugin.video.sopvid')

url=None
name=None
mode=None
iconimage=None
        
class MyPlayer( xbmc.Player ):
      	def __init__ ( self ):
        	xbmc.Player.__init__( self )
              	self.state=0

	def onPlayBackStarted(self):
		print "XXXXXXXXXXXXXXXXXXXXX START PLAY XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
		self.state=1
                                                                                                                                                        
	def onPlayBackStopped(self):
		if self.state == 0 :
			Notify('small', self.channel, 'Channel \'' + self.channel + '\' not abailable', '')

        	KILLSOP("xx")
        	self.state=2;
        	print "XXXXXXXXXXXXXXXXXXXXX STOP PLAY XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
                                            
	def onPlayBackEnded(self):
        	KILLSOP("xx")
        	self.state=2
        	print "XXXXXXXXXXXXXXXXXXXXX END PLAY XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"

def openfile(filename):
     fh = open(filename, 'r')
     contents=fh.read()
     fh.close()
     return contents

def save(filename,contents):  
     fh = open(filename, 'w')
     fh.write(contents)  
     fh.close()

def getSopcastUrl():
	ao = xbmcaddon.Addon(id='plugin.video.sopvid')
	path = ao.getSetting('sopcast_path')

	if not path.endswith("/") :
		path = path + "/"
	
#	xbmc.log(path)
	return path
	
def getSopcastTimeout():
	ao = xbmcaddon.Addon(id='plugin.video.sopvid')
	path = int(ao.getSetting('timeout'))

	if path < 10 :
		path = 10
	
#	xbmc.log(path)
	return path


def setView(content, viewType):
	
	xbmcplugin.setContent(int(sys.argv[1]), content)
#	xbmcplugin.setContent(int(sys.argv[1]), 'tvshows');
#	if selfAddon.getSetting('auto-view') == 'true':
#		xbmc.executebuiltin("Container.SetViewMode(%s)" % selfAddon.getSetting(viewType) )
		
#	xbmcplugin.addSortMethod( handle=int(sys.argv[1]), sortMethod=xbmcplugin.SORT_METHOD_VIDEO_TITLE )
#	xbmcplugin.addSortMethod( handle=int(sys.argv[1]), sortMethod=xbmcplugin.SORT_METHOD_LABEL )
#	xbmcplugin.addSortMethod( handle=int(sys.argv[1]), sortMethod=xbmcplugin.SORT_METHOD_UNSORTED )
	xbmcplugin.addSortMethod( handle=int(sys.argv[1]), sortMethod=xbmcplugin.SORT_METHOD_VIDEO_RATING )
#	xbmcplugin.addSortMethod( handle=int(sys.argv[1]), sortMethod=xbmcplugin.SORT_METHOD_DATE )
#	xbmcplugin.addSortMethod( handle=int(sys.argv[1]), sortMethod=xbmcplugin.SORT_METHOD_PROGRAM_COUNT )
#	xbmcplugin.addSortMethod( handle=int(sys.argv[1]), sortMethod=xbmcplugin.SORT_METHOD_VIDEO_RUNTIME )
#	xbmcplugin.addSortMethod( handle=int(sys.argv[1]), sortMethod=xbmcplugin.SORT_METHOD_GENRE )

                                                                        

def channels():
#       Manual ones
        addLink('sop://broker.sopcast.com:3912/111947', 'HBO - S2', 3, '/imgtv/hbo.jpg')
        addLink('sop://broker.sopcast.com:3912/86738', 'PRO TV - S2', 3, '/imgtv/protv.jpg')
        addLink('sop://broker.sopcast.com:3912/86738', 'PRO TV - S2', 3, '/imgtv/protv.jpg')
        addLink('sop://broker.sopcast.com:3912/111617', 'PRO TV - S3', 3, '/imgtv/protv.jpg')
        addLink('sop://broker.sopcast.com:3912/90686', 'PRO TV - S4', 3, '/imgtv/protv.jpg')
        addLink('sop://broker.sopcast.com:3912/112101', 'HBO Comedy - S2', 3, '/imgtv/protv.jpg')

        addLink('sop://broker.sopcast.com:3912/112099', 'TVR 1', 3, '/imgtv/tvr1.jpg')
        addLink('sop://broker.sopcast.com:3912/80620', 'TVR 2', 3, '/imgtv/tvr2.jpg')
        addLink('sop://broker.sopcast.com:3912/80625', 'Antena 1', 3, '/imgtv/antena1.jpg')
        addLink('sop://broker.sopcast.com:3912/80621', 'PRO TV - S1', 3, '/imgtv/protv.jpg')
        addLink('sop://broker.sopcast.com:3912/60586', 'Prima TV', 3, '/imgtv/primatv.jpg')
        addLink('sop://broker.sopcast.com:3912/74841', 'B1TV', 3, '/imgtv/b1tv.jpg')
        addLink('sop://broker.sopcast.com:3912/60704', 'National TV', 3, '/imgtv/nationaltv.jpg')
        addLink('sop://broker.sopcast.com:3912/80562', 'SportRo', 3, '/imgtv/sportro.jpg')
        addLink('sop://broker.sopcast.com:3912/60713', 'Eurosport', 3, '/imgtv/eurosport.jpg')
        addLink('sop://broker.sopcast.com:3912/80398', 'Eurosport2', 3, '/imgtv/eurosport2.jpg')
        addLink('sop://broker.sopcast.com:3912/111618', 'GSPTV', 3, '/imgtv/gsptv.jpg')
        addLink('sop://broker.sopcast.com:3912/111719', 'DigiSport', 3, '/imgtv/digisport.jpg')
        addLink('sop://broker.sopcast.com:3912/111378', 'Digisport 2', 3, '/imgtv/digisport2.jpg')
        addLink('sop://broker.sopcast.com:3912/98660', 'Digisport 3', 3, '/imgtv/digisport3.jpg')
        addLink('sop://broker.sopcast.com:3912/112093', 'Dolcesport ', 3, '/imgtv/dolcesport.jpg')
        addLink('sop://broker.sopcast.com:3912/112094', 'Dolcesport2', 3, '/imgtv/dolcesport2.jpg')
        addLink('sop://broker.sopcast.com:3912/80624', 'HBO', 3, '/imgtv/hbo.jpg')        
        addLink('sop://broker.sopcast.com:3912/112101', 'HBO Comedy', 3, '/imgtv/hbocomedy.jpg')
        addLink('sop://broker.sopcast.com:3912/112229', 'Digi Film', 3, '/imgtv/digifilm.jpg')
        addLink('sop://broker.sopcast.com:3912/60709', 'AXN', 3, '/imgtv/axn.jpg')
        addLink('sop://broker.sopcast.com:3912/60711', 'AXN Crime', 3, '/imgtv/axncrime.jpg')
        addLink('sop://broker.sopcast.com:3912/60710', 'AXN Scifi', 3, '/imgtv/axnscifi.jpg')
        addLink('sop://broker.sopcast.com:3912/80622', 'Pro Cinema', 3, '/imgtv/procinema.jpg')
        addLink('sop://broker.sopcast.com:3912/60703', 'Tv1000', 3, '/imgtv/tvrm.jpg')
        addLink('sop://broker.sopcast.com:3912/80555', 'AcasaTV', 3, '/imgtv/acasatv.jpg')
        addLink('sop://broker.sopcast.com:3912/60702', 'Kanal D', 3, '/imgtv/kanald.jpg')
        addLink('sop://broker.sopcast.com:3912/112096', 'Euforia Tv', 3, '/imgtv/euforiatv.jpg')
        addLink('sop://broker.sopcast.com:3912/116003', 'Favorit Tv', 3, '/imgtv/favorit.jpg')
        addLink('sop://broker.sopcast.com:3912/111690', '10 TV', 3, '/imgtv/10tv.jpg')
        addLink('sop://broker.sopcast.com:3912/112098', 'Diva', 3, '/imgtv/diva.jpg')
        addLink('sop://broker.sopcast.com:3912/110989', 'CinemaX', 3, '/imgtv/cinemax.jpg')
        addLink('sop://broker.sopcast.com:3912/74842', 'Antena 3', 3, '/imgtv/antena3.jpg')
        addLink('sop://broker.sopcast.com:3912/74843', 'Realitatea TV', 3, '/imgtv/realitateatv.jpg')
        addLink('sop://broker.sopcast.com:3912/60705', 'Disney Channel', 3, '/imgtv/disneychannel.jpg')
        addLink('sop://broker.sopcast.com:3912/80593', 'Cartoon Network', 3, '/imgtv/cn.jpg')
        addLink('sop://broker.sopcast.com:3912/60712', 'Boomerang', 3, '/imgtv/boomerang.jpg')
        addLink('sop://broker.sopcast.com:3912/74631', 'Animal Planet', 3, '/imgtv/animalplanet.jpg')
        addLink('sop://broker.sopcast.com:3912/80397', 'National Geographic', 3, '/imgtv/ngc.jpg')
        addLink('sop://broker.sopcast.com:3912/80626', 'National Geographic Wild', 3, '/imgtv/nationalgeowild.jpg')
        addLink('sop://broker.sopcast.com:3912/60708', 'OTV', 3, '/imgtv/otv.jpg')
        addLink('sop://broker.sopcast.com:3912/74846', 'Taraf Tv', 3, '/imgtv/taraftv.jpg')
        addLink('sop://broker.sopcast.com:3912/90686', 'Pro Tv International', 3, '/imgtv/protvint.jpg')
        addLink('sop://broker.sopcast.com:3912/116000', 'PVTV', 3, '/imgtv/pvtv.jpg')
        addLink('sop://broker.sopcast.com:3912/80623', 'Discovery Channel', 3, '/imgtv/discovery.jpg')
        addLink('sop://broker.sopcast.com:3912/74844', 'N24 Plus', 3, '/imgtv/n24plus.jpg')
        addLink('sop://broker.sopcast.com:3912/74633', 'Discovery World', 3, '/imgtv/discoveryworld.jpg')
        addLink('sop://broker.sopcast.com:3912/74636', 'Discovery Travel', 3, '/imgtv/discoverytravel.jpg')
        addLink('sop://broker.sopcast.com:3912/74634', 'Discovery Investigation', 3, '/imgtv/discoveryinvestigation.jpg')
        addLink('sop://broker.sopcast.com:3912/74635', 'Discovery Science', 3, '/imgtv/discoveryscience.jpg')

        setView("tvshows", "tvshows-view")

def RUNSOP(url):
        out = check_output([soppath + "run.sh", url, "3902", "8908"])
        xbmc.log("Started stream : %s" % (out))
        
def KILLSOP(url):
	out = check_output([soppath  + "kill.sh"])
	xbmc.log("Stopped stream: %s" % (out))

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
                                param[splitparams[0]]=splitparams[1]
                                
        return param

def Notify(typeq,title,message,times):
     #simplified way to call notifications. common notifications here.     
     if title == '':
     	title='Sopcast Notification'
     if typeq == 'small':
     	if times == '':
     		times='5000'
        xbmc.executebuiltin("XBMC.Notification("+title+","+message+","+times+",'')")


def handle_wait(time_to_wait,title,text):
	print 'waiting '+str(time_to_wait)+' secs'
	
	pDialog = xbmcgui.DialogProgress()
	ret = pDialog.create(' '+title)
	
	secs=0
	percent=0
	increment = int(100 / time_to_wait)
	
	cancelled = False
	while secs < time_to_wait:
		secs = secs + 1
		percent = increment*secs
		secs_left = str((time_to_wait - secs))
		remaining_display = ' Wait '+secs_left+' seconds for the video stream to activate...'
		pDialog.update(percent,' '+text,remaining_display)
		xbmc.sleep(1000)
		if (pDialog.iscanceled()):
			cancelled = True
			break
	if cancelled == True:
		print 'wait cancelled'
		return False
	else:
		print 'done waiting'
		return True

def handle_file(filename,getmode=''):
     #bad python code to add a get file routine.
     if filename == 'poster':
	     return_file = xbmcpath(sopdatapath,'Poster.txt')

def StartServer(url):
	RUNSOP(url)
	wait = handle_wait(timeout,'Sopcast','Initializing Stream')

	if wait == True:
		return "http://" + socket.gethostname()  + ":8908/tv.asf"
	else:
		return ''

def Item_Meta(name, iconimage):
	description='asdasd asd asd as dasd sa sa'
	listitem = xbmcgui.ListItem(name)
	listitem.setInfo('video', {'Title': name})
	if len(iconimage) > 0 :
	    iconimage = "http://sports-tv.eu" + iconimage
	listitem.setThumbnailImage(iconimage)
	return listitem

def playStream(name, url, iconimage):

	link = StartServer(url)
	listitem = Item_Meta(name, iconimage)	
	print 'attempting to stream file'
	
	try:
		p.channel = name
		p.play( link, listitem )
		while (1):
			if p.state < 2:
				xbmc.sleep(100)
			else:
				break
		print "XXXXXXXXXXXXXXXXXXXXX EXIT PLAY XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
		
	except:
		print 'File streaming failed'
		Notify('failedstream',',','')	

def addLink(url, name,mode,iconimage):
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&iconimage="+urllib.quote_plus(iconimage)
#        xbmc.log(u)
        ok=True
        if len(iconimage) > 0 :
        	iconimage = 'http://sports-tv.eu'+iconimage
        liz=xbmcgui.ListItem(name, iconImage=iconimage, thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name } )
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz)
        return ok

def addDir(name,url,mode,iconimage='DefaultFolder.png'):
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name } )
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
        return ok
   
params=get_params()
p = MyPlayer()
soppath = getSopcastUrl()
timeout = getSopcastTimeout()
              
try:
        url=urllib.unquote_plus(params["url"])
except:
        pass
        
try:
        name=urllib.unquote_plus(params["name"])
except:
        pass
        
try:
        mode=int(params["mode"])
except:
        pass
        
try:
        iconimage=urllib.unquote_plus(params["iconimage"])
except:
        pass

print "Mode: "+str(mode)
print "URL: "+str(url)
print "Name: "+str(name)
print "IconImage: "+str(iconimage)

if mode==None or url==None or len(url)<1:
        print ""
        channels()
        xbmcplugin.endOfDirectory(int(sys.argv[1]))
	
elif mode==1:
        print ""+url
        RUNSOP(url)
        
elif mode==2:
        print ""+url
        KILLSOP(url)

elif mode==3:
	print ""+url
	playStream(name, url, iconimage)

