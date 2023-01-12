import pandas as pd
import tabula
import csv

file = open('LAB1CSV.csv')
type(file)
csvreader = csv.reader(file)

header = []
header = next(csvreader)
header
rows = []
for row in csvreader:
        rows.append(row)
rows
