# m3u2strm
m3u2strm is a set of python scripts that will consume the VOD (video on demand) tv shows and movies from an apollogroup.tv subscription and make it into libraries useable by emby. We use ubuntu focal and these instructions are for this OS.

Pre-reqs:
1. Make sure you have python3 installed.
2. python3 -m ensurepip
3. python3 -m pip install asyncio
4. python3 -m pip install tools
5. python3 -m pip install wget
6.  and clone the git repo to there with the emby user so permissions are correctly synced.

Installation and setup:
1. Create a folder in / called `embyroot`
2. Inside embyroot folder, create a folder called `streaming`
3. Inside the streaming folder create 2 sub folders: one called `tvshows` and one called `movies`
4. Set your emby user as the owner of embyroot and sub-folders with command `sudo chown -r emby:emby embyroot`
5. Change to the emby user (On Ubuntu you can run: `sudo su -s /bin/bash emby') 
6. Inside the `embyroot` folder clone this repo (requires git to be installed) with the command: git clone https://github.com/EagleMitchell/m3u2strm.git
7. Create cron jobs to run these scripts once a day. In this example, we run tvshows at 12:10 and movies at 12:20... replace user/password and paths accordingly.

Run these as the emby user, not as root or a sudoer otherwise the permissions will be incorrect for emby to access the media created:
crontab -e

0 10 * * * cd /embyroot/m3u2strm && $(which python3) m3u2strm.py (apollo user) (apollo password) alltv "/embyroot/streaming/tvshows/" >> ~/cron.log 2>&1

0 20 * * * cd /embyroot/m3u2strm && $(which python3) m3u2strm.py (apollo user) (apollo password) movies "/embyroot/streaming/movies/" >> ~/cron.log 2>&1


To manually run an content scan:
  
cd /embyroot/m3u2strm

$(which python3) m3u2strm.py (apollo user) (apollo password) alltv "/embyroot/streaming/tvshows/"

$(which python3) m3u2strm.py (apollo user) (apollo password) movies "/embyroot/streaming/movies/"
