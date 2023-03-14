import re

# point_re = re.compile(r'(\d{4}\s)')
acc_point_re = r'\d{4}\s'
acc_point_re_exclude = r'\w\s' # char

line = 'И С М А И Л 0710003 0710004'
print(re.search(acc_point_re_exclude, line))

line = 'в 12:02'
print(re.search(acc_point_re_exclude, line))

line = '(-) (-)'
print(re.search(acc_point_re_exclude, line))