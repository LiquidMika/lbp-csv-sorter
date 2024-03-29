#!/usr/bin/env python

import re
import sys
import csv

try:
    chemin = sys.argv[1]
    print(chemin)
except:
    print("Manque le chemin du .csv")

# Format dd/mm/yyyy or dd.mm.yyyy 
regex1 = re.compile(r"\d{2}(\.|\/)\d{2}(\.|\/)\d{4}")

# Format dd/mm/yy or dd.mm.yy 
regex2 = re.compile(r"\d{2}(\.|\/)\d{2}(\.|\/)\d{2}")

def get_time(chaine):
    '''Récupère la date de transaction dans la chaine de caractères'''
    d = None
    if regex1.search(chaine):
        d = regex1.search(chaine).group()
        d = d[-4:] + '-' + d[3:5] + '-' + d[:2]
    elif regex2.search(chaine):
        d = regex2.search(chaine).group()
        d = '20' + d[-2:] + '-' + d[3:5] + '-' + d[:2]
    return d

def optim_string(chaine):
    '''Réduit la chaine "Description" à 50 caractères
    Si la chaine est < 50 : ajout d'espace à la fin'''
    taille = 50
    if len(chaine) > 50:
        opt = chaine[:50]
    elif len(chaine) < 50:
        opt = chaine + (50 - len(chaine)) * ' '
    else:
        opt = chaine
    return opt

# Parcours du fichier CSV et création d'une liste non triée
notSorted = []
with open(chemin, encoding='iso8859-15') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=';')
    line_count = 0
    for row in csv_reader:
        if line_count < 7: # Sauter l'entete du fichier CSV
            line_count += 1
            continue
        else:
            tmp = get_time(row[1])
            if tmp == None:
                dt = row[0]
                # formatage de la date AAAA-MM-DD
                dt = dt[6:10] + "-" + dt[3:5] + "-" + dt[:2]
            else:
                dt = tmp
            notSorted.append(dt + "\t" + optim_string(row[1]) + "\t" +  row[2])
            line_count += 1

# Tri de la liste
toto = sorted(notSorted)
 
# Ajout de saut de ligne entre les jours
dp = ""
for i in toto:
    if i[0:10] == dp:
        print(i)
    else:
        print('\n')
        print(i)
    dp = i[0:10]

