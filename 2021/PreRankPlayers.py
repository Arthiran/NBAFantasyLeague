import csv

file = open('CleanedPlayerStats.csv','r', newline='', encoding="utf8")
csvreader = csv.reader(file)
rows = []
index = 0

for row in csvreader:
    if index != 0:
        total = ((int(row[2]) * 2)
                 + (int(row[3]) * -1)
                 + (int(row[4]) * 1)
                 + (int(row[5]) * 1)
                 + (int(row[6]) * -1)
                 + (int(row[7]) * 2)
                 + (int(row[8]) * 1)
                 + (int(row[9]) * 2)
                 + (int(row[10]) * 4)
                 + (int(row[11]) * 4)
                 + (int(row[12]) * -2)
                 + (int(row[13]) * 1))
        tempArray = [row[1], total]
        rows.append(tempArray)
    index = index+ 1

with open('UnrankedPlayers.csv','w+', newline='', encoding="utf8") as my_csv:
    newarray = csv.writer(my_csv,delimiter=',')
    newarray.writerows(rows)
