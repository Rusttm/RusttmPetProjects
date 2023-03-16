import csv
my_code_dict = dict()
with open('data/value_cod.csv') as csvfile:
    spamreader = csv.reader(csvfile)
    for row in spamreader:
        print(row)