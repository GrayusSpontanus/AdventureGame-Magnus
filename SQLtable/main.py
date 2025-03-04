import sqlite3
import csv

conn = sqlite3.connect('FP.sqlite')

cursor = conn.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS Podcasts (ID INTEGER PRIMARY KEY,"
               "Title TEXT NOT NULL,"
               "Writer TEXT,"
               "Director TEXT,"
               "Genre TEXT,"
               "Main_Character TEXT,"
               "Network TEXT);")

with open('H:/Spotify Fiction Podcasts.csv','r') as file:
    dr = csv.DictReader(file)
    to_db = [(i['ID'], i['Title'], i['Writer'], i['Director'], i['Genre'],i['Main_Character'], i['Network'])for i in dr]


cursor.executemany("INSERT INTO Podcasts(ID,Title,Writer,Director,Genre,Main_Character,Network) VALUES (?,?,?,?,?,?,?)", to_db)

conn.commit()

conn.close()