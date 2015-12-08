import sys
import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT



conn = psycopg2.connect(database="tcount", user="postgres", host="localhost", port="5432")
cur = conn.cursor()
if len(sys.argv) == 3:
        cur.execute("SELECT word, count from Tweetwordcount WHERE count>=%s and count<=%s order by count desc",(sys.argv[1],sys.argv[2]))
else:
        print "Wrong number of arguments"
        sys.exit(1)
records = cur.fetchall()

for rec in records:
                print rec[0],": ",rec[1]
conn.commit()

conn.close()
