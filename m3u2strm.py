import tools
import logger
import streamClasses
import wget
import sys
import os
import shutil

user = sys.argv[1]
pw = sys.argv[2]
funct = sys.argv[3]
path = sys.argv[4]
urltype = ''
print('...Starting Download...')
if funct == 'latesttv':
    urltype = 'tvshows'
    ipttvurl = 'https://tv4.live/api/list/' + user + '/' + pw + '/m3u8/'+ urltype +'/1'
    print(wget.download(ipttvurl, ('m3u/apollotvshows-1.m3u')))
    apollolist = streamClasses.rawStreamList('m3u/apollotvshows-1.m3u')
    os.remove('m3u/apollotvshows-1.m3u')
    src = '/m3u2strm/tvshows'
    dest = path
    print('copying folder structure to ',path)
    destination = shutil.copytree(src, dest, dirs_exist_ok=True)
    print('cleaning up temp space')
    cleanup = shutil.rmtree('tvshows/')
elif funct == 'alltv':
    urltype = 'tvshows'
    ipttvurl = 'https://tvnow.best/api/list/' + user + '/' + pw + '/m3u8/'+ urltype
    print(wget.download(ipttvurl, ('m3u/apollotvshows.m3u')))
    apollolist = streamClasses.rawStreamList('m3u/apollotvshows.m3u')
    os.remove('m3u/apollotvshows.m3u')
    src = '/m3u2strm/tvshows'
    dest = path
    print('copying folder structure to ',path)
    destination = shutil.copytree(src, dest, dirs_exist_ok=True)
    print('cleaning up temp space')
    cleanup = shutil.rmtree('tvshows/')
elif funct == 'movies':
    urltype = 'movies'
    ipttvurl = 'https://tvnow.best/api/list/' + user + '/' + pw + '/m3u8/'+ urltype
    print(wget.download(ipttvurl, ('m3u/iptvmovies.m3u')))
    apollolist = streamClasses.rawStreamList('m3u/iptvmovies.m3u')
    os.remove('m3u/iptvmovies.m3u')
    src = '/m3u2strm/movies'
    dest = path
    print('copying folder structure to ',path)
    destination = shutil.copytree(src, dest, dirs_exist_ok=True)
    print('cleaning up temp space')
    cleanup = shutil.rmtree('movies/')
elif funct == 'events':
    urltype = 'events'
    ipttvurl = 'https://tv4.live/api/list/' + user + '/' + pw + '/m3u8/'+ urltype
    print(wget.download(ipttvurl, ('m3u/iptvevents.m3u')))
    apollolist = streamClasses.rawStreamList('m3u/iptvevents.m3u')
    os.remove('m3u/iptvevents.m3u')
    src = '/m3u2strm/events'
    dest = path
    print('copying folder structure to ',path)
    destination = shutil.copytree(src, dest, dirs_exist_ok=True)
    print('cleaning up temp space')
    cleanup = shutil.rmtree('events/')
print('done')
