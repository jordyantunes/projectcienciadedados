import sqlite3

conn = sqlite3.connect("reviews.db")
cursor = conn.cursor()
sql = "INSERT INTO `reviews` (`id_user`, `review`) VALUES (?, ?)"
cursor.execute(sql, (2, "tchau"))
conn.commit()
# print(cursor.fetchone())