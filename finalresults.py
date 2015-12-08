import sys
import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT



conn = psycopg2.connect(database="tcount", user="postgres", host="localhost", port="5432")
cur = conn.cursor()
if len(sys.argv) == 1:
	cur.execute("SELECT word, count from Tweetwordcount order by word")
if len(sys.argv) == 2:
	cur.execute("SELECT word, count from Tweetwordcount WHERE word=%s",(sys.argv[1],))
if len(sys.argv) == 3:
        cur.execute("SELECT word, count from Tweetwordcount WHERE count>=%s and count<=%s order by count desc",(sys.argv[1],sys.argv[2]))
if len(sys.argv) > 3:
 	print "Wrong number of arguments"
        sys.exit(1)	
records = cur.fetchall()

for rec in records:
#   print "word = ", rec[0]
#   print "count = ", rec[1], "\n"
	if len(sys.argv) == 2:
		print "Total number of occurences of", rec[0],": ", rec[1], "\n"
	else:
		print rec[0],": ",rec[1] 
conn.commit()

conn.close()

