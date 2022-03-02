import csv

f = open('data/raw_data.csv', 'r')
reader = csv.reader(f)
data_list = list(reader)


f = open('data/clean_data.csv', 'w')
clean_data = csv.writer(f, delimiter=',')


for line in data_list:
    if (len(line) > 7):
        line[1] = line[1].strip("Jr. & family")
        line[1] = line[1].strip("Jr.")
        line[1] = line[1].strip("II.")
        line[1] = line[1].strip("III.")
        line[2] = line[2].strip("$").strip("B") .strip(" ")
        line[4] = line[4].replace("√©", "é")

    line[1] = line[1].strip("$").strip("B") .strip(" ")
    line[0] = line[0].replace("√©", "é")
    line[3] = line[3].replace("√©", "é")
    line[0] = line[0].replace("√ß", "ç")
        
    clean_data.writerow(line)