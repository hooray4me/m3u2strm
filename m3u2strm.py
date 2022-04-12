#!/usr/bin/env python3
"""$(which python3) m3u2strm.py apollo user pass alltv '/streaming/tv/' remoteSharePath localmount credentialFilebbbbbbbbbbbbbbbbbb"""
import tools
import streamClasses
import wget
import sys
import os
import shutil
import filecmp

provider = sys.argv[1]
user = sys.argv[2]
pw = sys.argv[3]
funct = sys.argv[4]
path = sys.argv[5]
share = sys.argv[6]
localmount = sys.argv[7]
cred = sys.argv[8]
urltype = ''
providerUrl = ''
directory =  os.path.abspath(os.path.dirname(__file__))
if provider == 'apollo':
    providerUrl = 'https://tvnow.best/api/list/'+ user + '/' + pw + '/m3u8/'
if not os.path.ismount(localmount):
    os.system("sudo mount -t cifs -o credentials="+cred+" "+share+" "+localmount)
if os.path.ismount(localmount):
    print('...Starting Download...')
    if funct == 'alltv':
        urltype = 'tvshows'
        for i in range(1,21):
            url = providerUrl + urltype +'/' + str(i)
            print(wget.download(url, ('m3u/apollotvshows-'+str(i)+'.m3u')))
            apollolist = streamClasses.rawStreamList('m3u/apollotvshows-'+str(i)+'.m3u')
            os.remove('m3u/apollotvshows-'+str(i)+'.m3u')
        print('comparing destination ',path)
        c = filecmp.dircmp(directory+'/tvshows', path)
        tools.compare_and_update(c)
        print('cleaning up temp space')
        cleanup = shutil.rmtree('tvshows/')
    elif funct == 'latesttv':
        urltype = 'tvshows'
        print(wget.download(providerUrl+urltype, ('m3u/apollotvshows.m3u')))
        apollolist = streamClasses.rawStreamList('m3u/apollotvshows.m3u')
        os.remove('m3u/apollotvshows.m3u')
        print('comparing destination ',path)
        c = filecmp.dircmp(directory+'/tvshows', path)
        tools.compare_and_update(c)
        print('cleaning up temp space')
        cleanup = shutil.rmtree('tvshows/')
    elif funct == 'movies':
        urltype = 'movies'
        print(wget.download(providerUrl+urltype, ('m3u/iptvmovies.m3u')))
        apollolist = streamClasses.rawStreamList('m3u/iptvmovies.m3u')
        os.remove('m3u/iptvmovies.m3u')
        print('comparing destination ',path)
        c = filecmp.dircmp(directory+'/movies', path)
        tools.compare_and_update(c)
        print('cleaning up temp space')
        cleanup = shutil.rmtree('movies/')
    os.system("sudo umount "+localmount)
    print('done')
else:
    print("couldn't mount remote storage")