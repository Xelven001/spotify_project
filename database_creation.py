import pandas as pd
import sqlite3

df = pd.read_csv("../project3/data/songs_normalize.csv")
connection = sqlite3.connect("spotify_data.db")
cursor = connection.cursor()


df.to_sql(
    name = 'song_metrics',
    con = connection, 
    if_exists = 'replace', 
    index = False, 
    dtype = { 
        'artist':'text', 
        'song': 'text',
        'duration_ms': 'integer',
        'explicit': 'boolean',
        'year' : 'integer',
        'popularity' :'integer',
        'danceability': 'float',
        'energy' : 'float',
        'key': 'real',
        'loudness': 'float',
        'mode':'real',
        'speechiness': 'float',
        'acousticness':'float',
        'instrumentalness':'float',
        'liveness':'float',
        'valence':'float',
        'tempo':'float',
        'genre':'float'}
)
