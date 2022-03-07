#!/usr/bin/env python3
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
directory =  os.path.abspath(os.path.dirname(__file__))
print('...Starting Download...')
if funct == 'alltv':
    urltype = 'tvshows'
    ipttvurl = 'https://tvnow.best/api/list/' + user + '/' + pw + '/m3u8/'+ urltype +'/'
    for i in range(1,21):
        url = ipttvurl + str(i)
        print(wget.download(url, ('m3u/apollotvshows-'+str(i)+'.m3u')))
        apollolist = streamClasses.rawStreamList('m3u/apollotvshows-'+str(i)+'.m3u')
        os.remove('m3u/apollotvshows-'+str(i)+'.m3u')
    src = directory+'/tvshows'
    dest = path
    print('copying folder structure to ',path)
    destination = shutil.copytree(src, dest, dirs_exist_ok=True)
    print('cleaning up temp space')
    cleanup = shutil.rmtree('tvshows/')
elif funct == 'latesttv':
    urltype = 'tvshows'
    ipttvurl = 'https://tvnow.best/api/list/' + user + '/' + pw + '/m3u8/'+ urltype
    print(wget.download(ipttvurl, ('m3u/apollotvshows.m3u')))
    apollolist = streamClasses.rawStreamList('m3u/apollotvshows.m3u')
    os.remove('m3u/apollotvshows.m3u')
    src = directory+'/tvshows'
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
    src = directory+'/movies'
    dest = path
    print('copying folder structure to ',path)
    destination = shutil.copytree(src, dest, dirs_exist_ok=True)
    print('cleaning up temp space')
    cleanup = shutil.rmtree('movies/')
print('done')
