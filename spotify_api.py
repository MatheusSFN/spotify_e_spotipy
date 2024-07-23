import spotipy
import spotipy.util as util
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv
import os
import json
from spotify_db import insert_values

load_dotenv()

#Carga das variáveis de ambiente
CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")
REDIRECT_URI = os.getenv("REDIRECT_URI")
USERNAME = os.getenv("USERNAME")

#Conexão com a API do Spotify
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID,
                                               client_secret=CLIENT_SECRET,
                                               redirect_uri=REDIRECT_URI,
                                               scope="user-library-read user-top-read"))

#Pegar o usuário logado
# user = sp.current_user()
# print(f"Usuário: {user['display_name']}") 

# print(json.dumps(sp.current_user_top_artists(limit=10, time_range="long_term")['items'], sort_keys=True ,indent=4))

#Pegar os 5 artistas mais ouvidos
def get_top_artists():
    results_top_artists = sp.current_user_top_artists(limit=10, time_range="long_term")
    print(json.dumps(results_top_artists, sort_keys=True ,indent=4))
    print("\n")
    return results_top_artists

def get_artist_albums():
    results_artist_albuns = sp.artist_albums('spotify:artist:0jOs0wnXCu1bGGP7kh5uIu', album_type=None, include_groups=None, country='BR', limit=100, offset=0)
    print(json.dumps(results_artist_albuns, sort_keys=True ,indent=4))
    print("\n")
    return results_artist_albuns

def get_album_tracks():
    results_album_tracks = sp.album_tracks('spotify:album:59W9kTRepoDqDGFgn0kPBa', limit=None, offset=0, market=None)
    print(json.dumps(results_album_tracks, sort_keys=True ,indent=4))
    print("\n")
    return results_album_tracks

def get_related_artists():
    results_related_artists = sp.artist_related_artists('spotify:artist:0jOs0wnXCu1bGGP7kh5uIu')
    print(json.dumps(results_related_artists, sort_keys=True ,indent=4))
    print("\n")
    return results_related_artists

def get_artist_top_tracks():
    results_artist_top_tracks = sp.artist_top_tracks('spotify:artist:0jOs0wnXCu1bGGP7kh5uIu', country='BR')
    print(json.dumps(results_artist_top_tracks, sort_keys=True ,indent=4))
    print("\n")
    return results_artist_top_tracks

# artists = results['items']
# for item in artists:
#     tuple_artist = str(item['name']), str(item['id']), str(item['type']), str(item['genres']), int(item['popularity']), int(item['followers']['total'])
#     insert_values('artists', tuple_artist)



# tim_maia_uri = 'spotify:artist:0jOs0wnXCu1bGGP7kh5uIu'

# results = sp.artist_albums(tim_maia_uri, album_type='album')
# albums = results['items']
# while results['next']:
#     results = sp.next(results)
#     albums.extend(results['items'])

# for album in albums:
#     print(album['name'])

# 1. Pegar os 5 top artistas mais ouvidos
#Retorna os 5 artistas mais ouvidos pelo usuário
# top_artists = sp.current_user_top_artists()

# 2. Listar todos os albuns desses artistas
# for artist in top_artists['items']:
#     print(f"Artista: {artist['name']}")
#     artist_uri = artist['uri']
#     results = sp.artist_albums(artist_uri, album_type='album')
#     albums = results['items']
#     while results['next']:
#         results = sp.next(results)
#         albums.extend(results['items'])
#     for album in albums:
#         print(album['name'])

# 3. Listar todas as músicas desses albuns
# for album in albums:
#     album_uri = album['uri']
#     results = sp.album_tracks(album_uri)
#     tracks = results['items']
#     while results['next']:
#         results = sp.next(results)
#         tracks.extend(results['items'])
#     for track in tracks:
#         print(track['name'])

# 4. Criar um database com 3 tabelas: Artistas, Albuns, Músicas
# 5. Popular as tabelas com os dados coletados
