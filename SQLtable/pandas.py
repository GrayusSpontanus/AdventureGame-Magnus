import sqlite3
import pandas as pd

conn = sqlite3.connect('FP.sqlite')

cursor = conn.cursor()

df = pd.read_csv("Spotify_Fiction_Podcasts.csv")
df.to_sql('FP', conn, if_exists='append', index=False)

df2 = pd.read_csv("Spotify_Fiction_Podcasts.csv")

