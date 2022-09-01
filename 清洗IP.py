import csv
import re

# 3. 执行查询
with open('../csv.csv', encoding='utf-8-sig') as f:
    for csv_list in csv.reader(f, skipinitialspace=True):
        # print(csv_list)
        for ip in csv_list:
            ip = re.compile('^(1\d{2}|2[0-4]\d|25[0-5]|[1-9]\d|[1-9])\.(1\d{2}|2[0-4]\d|25[0-5]|[1-9]\d|\d)\.'
                                    '(1\d{2}|2[0-4]\d|25[0-5]|[1-9]\d|\d)\.(1\d{2}|2[0-4]\d|25[0-5]|[1-9]\d|\d)$')
            print(ip)

