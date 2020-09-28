import csv
import codecs

with codecs.open('TEXTCZ1.txt', 'r', encoding='ISO-8859-2',  errors='replace') as in_file:
    stripped = (line.strip() for line in in_file)
    lines = (line.split(",") for line in stripped if line)
    with open('myfile_CZ.csv', 'w') as out_file:
        writer = csv.writer(out_file)
        writer.writerows(lines)

