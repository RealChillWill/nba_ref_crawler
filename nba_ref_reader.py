import sys # system
import os # operation system
import psycopg2
import pprint

connection = psycopg2.connect (database = "postgres", user = "postgres", password = "will0723", 
                               host = "127.0.0.1", port = "5432")

cursor = connection.cursor()
cursor.execute ('''SELECT * FROM nba_reference_data.team_advanced_statistics''')
rows = cursor.fetchall()
tspct = [row[1] for row in rows]
efgpct = [row[2] for row in rows]
threepar = [row[3] for row in rows]
ftr = [row[4] for row in rows]
orbpct = [row[5] for row in rows]
drbpct = [row[6] for row in rows]
trbpct = [row[7] for row in rows]
astpct = [row[8] for row in rows]
stlpct = [row[9] for row in rows]
blkpct = [row[10] for row in rows]
tovpct = [row[11] for row in rows]
ortg = [row[12] for row in rows]
drtg = [row[13] for row in rows]
result = [1 if row[14] == "W" else 0 for row in rows]

# # PRINT
# pp = pprint.PrettyPrinter(indent = 4)
# pp.pprint(result)
