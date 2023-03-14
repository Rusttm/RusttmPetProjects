
""" from https://github.com/danshorstein/pythonic-accountant/blob/master/019%20Importing%20data%20from%20another%20PDF%20file/pdf_extract.ipynb"""
import pdfplumber
import re

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



def GetInfoFromPDF():
    """ берет информацию со всех файлов в директории data и возвращает словарь с указанием года и значениями позиций"""
    document = dict()
    with pdfplumber.open("data/2020.pdf") as pdf:
        pages = pdf.pages
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
                        print(f'Excluded {line=}\n {result=}')
                    else:
                        values = tailConverter(result)
                        if 1 < len(values) < 5:
                            document[comp.group()[:-1]] = values
                            print(f'{position=} {comp.group()=}: {values=}\n {line} tail {result=}')



if '__name__' == '__main__':
    pass


