import sqlite3


conn = sqlite3.connect('movie.db')
cur = conn.cursor()

cur.execute("SELECT title, budget FROM movies ORDER BY popularity DESC LIMIT 1")
result = cur.fetchall()
print('1.', result)

cur.execute("SELECT title FROM movies WHERE release_date >= '2009-12-01' AND release_date < '2010-01-01' ORDER BY budget DESC LIMIT 1")
result = cur.fetchall()
print('2.', result)

cur.execute("SELECT title FROM movies WHERE tagline = 'The battle within.'")
result = cur.fetchall()
print('3.', result)

cur.execute("SELECT title FROM movies WHERE release_date < '1980-01-01' AND vote_average > 8 ORDER BY vote_count DESC LIMIT 1")
result = cur.fetchall()
print('4.', result)

conn.close()