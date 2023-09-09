import csv
import json

csvfile = open('paldea.csv', 'r')
jsonfile = open('paldea-dex.json', 'w')

pokemons = []
data = {}
fieldnames = ("Number", "Status")
reader = csv.DictReader( csvfile, fieldnames)
for row in reader:
    pokemon = row
    pokemonNumber = pokemon['Number']
    newLine = {}
    newLine[pokemonNumber] = pokemon['Status']
    pokemons.append(newLine)
data["pokemon"] = pokemons
json.dump(data, jsonfile)
jsonfile.write(',\n')