#!/usr/bin/env python

import re
import sys
import csv

try:
    chemin = sys.argv[1]
    print(chemin)
except:
    print("Manque le chemin du .csv")

# with openemin,'r') as f:
#    list_transactions = f.readlines()

regex = re.compile(r"\d{2}\.\d{2}\.\d{2}")

def get_time(chaine):
    d = None
    if regex.search(chaine):
        d = regex.search(chaine).group()
        d = '20' + d[-2:] + '-' + d[3:5] + '-' + d[:2]
    return d

def optim_string(chaine):
    taille = 50
    if len(chaine) > 50:
        opt = chaine[:50]
    elif len(chaine) < 50:
        opt = chaine + (50 - len(chaine)) * ' '
    else:
        opt = chaine
    return opt

notSorted = []

with open(chemin, encoding='iso8859-15') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=';')

    line_count = 0
    for row in csv_reader:
        # print(line_count, row)
        if line_count < 8:
            line_count += 1
            continue
        else:
            tmp = get_time(row[1])
            if tmp == None:
                dt = row[0]
                dt = dt[6:10] + "-" + dt[3:5] + "-" + dt[:2]
            else:
                dt = tmp
            notSorted.append(dt + "\t" + optim_string(row[1]) + "\t" +  row[2])
            line_count += 1

toto = sorted(notSorted)
 
dp = ""
for i in toto:
    if i[0:10] == dp:
        print(i)
    else:
        print('\n')
        print(i)
    dp = i[0:10]

