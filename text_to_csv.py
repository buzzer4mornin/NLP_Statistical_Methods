import csv
import codecs

with open('TEXTEN1.txt', 'r') as in_file:
    stripped = (line.strip() for line in in_file)
    lines = (line.split(",") for line in stripped if line)
    with open('myfile_EN.csv', 'w') as out_file:
        writer = csv.writer(out_file)
        writer.writerows(lines)

