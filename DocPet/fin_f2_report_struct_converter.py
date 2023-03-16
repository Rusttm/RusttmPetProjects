# coding="utf-8"
import csv
import json


my_name_code_dict = dict()
file_path = '/Users/johnlennon/RusttmGDrive/Python/PetProjects/DocPet/data/fin_f2rep_structure.csv'
with open(file_path) as csvfile:
    spamreader = csv.reader(csvfile)
    for row in spamreader:
        print(row)
        if my_name_code_dict.get(row[0], None):
            new_name = f'{row[0]}_'
            my_name_code_dict[new_name] = row[1]
        else:
            my_name_code_dict[row[0]] = row[1]
with open('/Users/johnlennon/RusttmGDrive/Python/PetProjects/DocPet/config/fin_f2rep_structure.json', "w") as outfile:
    json.dump(my_name_code_dict, outfile, indent=4, sort_keys=False, ensure_ascii=False)
print(my_name_code_dict)