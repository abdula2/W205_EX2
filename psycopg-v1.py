#Sample code snippets for working with psycopg

#Connecting to a database
#Note: If the database does not exist, then this command will create the database

import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

conn = psycopg2.connect(database="postgres", user="postgres", password="pass", host="localhost", port="5432")
dbname = "Tcount"
conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
cur = conn.cursor()
cur.execute('CREATE DATABASE ' + dbname)
cur.close()
conn.close()

conn = psycopg2.connect(database="tcount", user="postgres", host="localhost", port="5432")

#Create a Table
#The first step is to create a cursor. 


cur = conn.cursor()
cur.execute('''CREATE TABLE Tweetwordcount
       (word TEXT PRIMARY KEY     NOT NULL,
       count INT     NOT NULL);''')
conn.commit()
conn.close()


#Running sample SQL statements
#Inserting/Selecting/Updating

#Rather than executing a whole query at once, it is better to set up a cursor that encapsulates the query, 
#and then read the query result a few rows at a time. One reason for doing this is
#to avoid memory overrun when the result contains a large number of rows. 

#cur = conn.cursor()

#Insert
#cur.execute("INSERT INTO Tweetwordcount (word,count) \
#      VALUES ('exercise', 3)");
#conn.commit()

#Update
#Assuming you are passing the tuple (uWord, uCount) as an argument
#cur.execute("UPDATE Tweetwordcount SET count=%s WHERE word=%s", (uWord, uCount))
#conn.commit()

#Select
#cur.execute("SELECT word, count from Tweetwordcount order by count")
#records = cur.fetchall()
#for rec in records:
#   print "word = ", rec[0]
#   print "count = ", rec[1], "\n"
#conn.commit()

#conn.close()
