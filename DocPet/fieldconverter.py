import pandas as pd
import json

df = pd.read_csv ('data/report_templates.csv')
result_json = {'year': '2020', 'name': 'Бухгалтерский баланс', 'data': {}}

my_column = df['Задание 1. Рассчитать коэффициенты эффективности ОАО «Восток-Запад»']
i = 0
for row in my_column:
    # field = row.split()
    row_ = str(row)
    if row_ != 'nan' and row_ != 'Бухгалтерский баланс' and row_ != 'Статья':
        pos_number = f'number{i}'
        result_json['data'][pos_number] = {'name': row_, 'value': 0}
        i += 1
        # print(row_)
print(result_json)
with open("config/reportnames.json", 'w', encoding='utf-8') as fout:
    json_dumps_str = json.dumps(result_json, indent=4, ensure_ascii=False)
    print(json_dumps_str, file=fout)

if '__name__' == '__main__':
    pass