import os

from flask import Flask, session, request, redirect, url_for, render_template

# set up authorization with spotipy library
from spotipy import Spotify
from spotipy.oauth2 import SpotifyOAuth
from spotipy.cache_handler import FlaskSessionCacheHandler

app = Flask(__name__)
# key to encrypt session data to prevent user tampering
app.config['SECRET_KEY'] = os.urandom(64)

client_id = '8996ce409a564c8bad2d182582494df4'
client_secret = 'fbbb7731825142268c7e022726a0641e'
redirect_uri = 'http://127.0.0.1:8002/callback'
scope = 'playlist-read-private, streaming'

# use authorization code flow (OAuth) - access user resources & access token refresh

cache_handler = FlaskSessionCacheHandler(session)
# authentication manager
sp_oauth = SpotifyOAuth(
    client_id=client_id,
    client_secret=client_secret,
    redirect_uri=redirect_uri,
    scope=scope,
    cache_handler=cache_handler,
    show_dialog=True
)
# instance of client
sp = Spotify(auth_manager=sp_oauth)

# define homepage


@app.route('/')
def home():
    # a nonexpired valid token that can be used to interact w/ spotify API
    if not sp_oauth.validate_token(cache_handler.get_cached_token()):
        auth_url = sp_oauth.get_authorize_url()
        return redirect(auth_url)
    # redirect to url to search page
    return redirect(url_for('search'))

# callback endpoint (refresh token)


@app.route('/callback')
def callback():
    # code from login allows token refresh
    sp_oauth.get_access_token(request.args['code'])
    return redirect(url_for('search'))


@app.route('/search')
def search():
    return render_template('index.html')

# logout


@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('\home'))


if __name__ == '__main__':
    app.run(port=8002, debug=True)
