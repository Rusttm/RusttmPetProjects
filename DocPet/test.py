# coding="utf-8"
import  json
try:
    with open('config/code_name.json') as json_file:
        code_name = json.load(json_file)
except Exception as e:
    print("не смог загрузить данные из файла", e)