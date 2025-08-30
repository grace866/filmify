# filmify
Filmify is a web app that uses the Spotify and TMDb APIs to recommend music based on a selected movie.

## Dependencies
- Flask
- spotipy
- tmdbsimple
- python dot-env

## Installation
1. Clone the repository
   - In terminal:
       - cd your-repo
       - git clone (web URL found under "code" tab)
3. (Optional but recommended) Create and activate a virtual environment
   - In terminal: python -m venv venv 
   - On macOS/Linux: venv/bin/activate
   - On Windows: venv\Scripts\activate
4. Install the dependencies listed in requirements.txt
   - In terminal: pip install -r requirements.txt
  
## Setting up API Keys
This app requires API keys and configuration values to access Spotify and TMDb

1. Spotify API key
   - Go to the [Spotify Developer Dashboard (https://developer.spotify.com/dashboard/applications)
   - Log in and create a new app
   - Copy your Client ID and Client Secret
   - Set the redirect URI to `http://localhost:8002/callback`
2. TMDb API key
   - Create an account at [The Movie Database](https://www.themoviedb.org/account/signup)
   - Go to your account settings > API section
   - Click Create > Developer > Accept
   - Fill out app details & copy API key

## Create a `.env` File

In the root directory of the project, create a `.env` file with the following content:

```env
CLIENT_ID=your_spotify_client_id
CLIENT_SECRET=your_spotify_client_secret
REDIRECT_URI=http://localhost:8002/callback
API_KEY=your_tmdb_api_key
```

Note: loading songs after clicking on a movie might take some time; if there are no movie keywords, no songs will be recommended




