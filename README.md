## m3u2strm
m3u2strm is a set of python scripts that will consume the VOD (video on demand) tv shows and movies from an apollogroup.tv subscription and make it into libraries useable by emby. We use ubuntu focal and these instructions are for this OS.

###Pre-reqs:
1. Make sure you have python3 installed.
2. `python3 -m ensurepip`
3. `python3 -m pip install tools`
4. `python3 -m pip install wget`

###Installation and setup:
1. Clone this repo (requires git to be installed). We clone to the root.
`git clone https://github.com/hooray4me/m3u2strm.git`
2. create a folder for tvshows and movies... make sure the emby user account has access to these folders.
3. create cron jobs to run these scripts once a day. In this example, we run tvshows at 12:10 and movies at 12:20... replace user/password and paths accordingly.

`crontab -e`
```
0 10 * * * cd /m3u2strm && $(which python3) m3u2strm.py apollo (apollo user) (apollo password) alltv "/path/to/tvshows/" >> ~/cron.log 2>&1

0 20 * * * cd /m3u2strm && $(which python3) m3u2strm.py apollo (apollo user) (apollo password) movies "/path/to/movies/" >> ~/cron.log 2>&1
  ```
You can run this manually:
  
`cd /m3u2strm`

###TV Shows
`$(which python3) m3u2strm.py apollo (apollo user) (apollo password) alltv "/path/to/tvshows/"`

###Movies
`$(which python3) m3u2strm.py apollo (apollo user) (apollo password) movies "/path/to/movies/"`

In emby, create a tvshows and movies library that points to these paths.
