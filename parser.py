import csv, json, re

cols = {
    "number": 0,
    "date": 2,
    "type": 4,
    "dimensions": 6,
    "thickness": 7,
    "width": 8,
    "note": 10,
    "bin": 12,
    "book": 14
}

filename = "file.csv"

def parseFile():
    f = open(filename)
    reader = csv.reader(f)
    for row in reader:
        print(row[cols["number"]])
