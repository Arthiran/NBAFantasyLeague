import csv
import pandas as pd

'''df = pd.read_csv('PrePlayerStats.csv')
df.drop('Rk', axis = 1, inplace = True)
df.drop('Pos', axis = 1, inplace = True)
df.drop('Age', axis = 1, inplace = True)
df.drop('Tm', axis = 1, inplace = True)
df.drop('G', axis = 1, inplace = True)
df.drop('GS', axis = 1, inplace = True)
df.drop('MP', axis = 1, inplace = True)
df.drop('FG%', axis = 1, inplace = True)
df.drop('3PA', axis = 1, inplace = True)
df.drop('3P%', axis = 1, inplace = True)
df.drop('2P', axis = 1, inplace = True)
df.drop('2PA', axis = 1, inplace = True)
df.drop('2P%', axis = 1, inplace = True)
df.drop('eFG%', axis = 1, inplace = True)
df.drop('FT%', axis = 1, inplace = True)
df.drop('TRB', axis = 1, inplace = True)
df.drop('PF', axis = 1, inplace = True)
df.to_csv('PostPlayerStats.csv')'''

file = open('PostPlayerStats.csv','r+', newline='', encoding="utf8")
csvreader = csv.reader(file)
rows = []
index = 0
previousPlayer = ''

for row in csvreader:
        currentPlayer = row[1]
        if previousPlayer != currentPlayer:
                rows.append(row)
                previousPlayer = currentPlayer
        index = index+ 1

with open('CleanedPlayerStats.csv','w+', newline='', encoding="utf8") as my_csv:
    newarray = csv.writer(my_csv,delimiter=',')
    newarray.writerows(rows)
