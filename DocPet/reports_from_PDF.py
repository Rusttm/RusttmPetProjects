# coding=utf8
"""
модуль подготовки данных для формирования финансового отчета
данные берутся из указанной папки (по умолчанию папка data), названия файлов пишем с указанием года отчета 2020.pdf
from https://github.com/danshorstein/pythonic-accountant/blob/master/019%20Importing%20data%20from%20another%20PDF%20file/pdf_extract.ipynb


"""

import pdfplumber
import re
import os
import json
import tqdm


DATA_DIR = 'data'

point_re = re.compile(r'(\d{4}\s)')
acc_point_re = r'(\d{4}\s)'
point_re_exclude = re.compile(r'[а..я][a..z]')
acc_point_re_exclude = r'[а..я][a..z]' # char

def tailConverter(result):
    tail = []
    result = result.replace('-', '0')
    result = result.replace('(', '-')
    result = result.replace(')', '')
    tail = result.split()
    try:
        for pos, elem in enumerate(tail):
            tail[pos] = int(elem)
    except:
        return [None]
    return tail

def PdfFilesList(pdf_dir = DATA_DIR):
    """ возвращает список файлов в директории """
    result_dict = {pdf_dir: {}}
    for file in os.listdir(f"{pdf_dir}/"):
        name = file.split('.')[0]
        extention = file.split('.')[1]
        if extention == 'pdf':
            result_dict[DATA_DIR][name] = file
    return  result_dict



def GetInfoFromPDF(pdf_file="data/2020.pdf"):
    """ берет информацию со всех файлов в директории data и возвращает словарь с указанием года и значениями позиций"""
    document = dict()
    with pdfplumber.open(pdf_file) as pdf:
        for page_number, page in enumerate(pdf.pages):
            page_data = dict()
            text = page.extract_text()
            for line_number, line in enumerate(text.split('\n')):
                page_data[line_number] = line
                comp = point_re.search(line)
                # comp = re.search(acc_point_re, line)
                if comp:
                    position = comp.span()[1]
                    result = line[position:]
                    comp_exclude = point_re_exclude.search(result)
                    if comp_exclude:
                        continue
                        # print(f'Excluded {line=}\n {result=}')
                    else:
                        values = tailConverter(result)
                        if (1 < len(values) < 5) and not document.get(comp.group()[:-1]):
                            document[comp.group()[:-1]] = values
                            # print(f'{position=} {comp.group()=}: {values=}\n {line} tail {result=}')

    return document

def GetInfoFromAllPDF(pdf_dir=DATA_DIR):
    """ возвращает словарь с данными из указанных файлов """
    with tqdm.tqdm(total=100, desc="Extract data from pdf") as pbar:
        list_files = PdfFilesList(pdf_dir=pdf_dir) # запрос на список файлов в директории
        pbar.update(20)
        data_dict = dict()
        for name, file in list_files[pdf_dir].items():
            data_dict[name] = GetInfoFromPDF(pdf_file=f"{pdf_dir}/{file}")
            pbar.update(20)
        with open(f'{pdf_dir}/data.json', 'w') as fp:
            json.dump(data_dict, fp)
        pbar.update(20)
    return data_dict


if __name__ == '__main__':
    print(GetInfoFromPDF())


