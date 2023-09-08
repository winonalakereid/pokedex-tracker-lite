import csv
import json

csvfile = open('pokemon.csv', 'r')
jsonfile = open('shiny-dex.json', 'w')

pokemons = []
data = {}
fieldnames = ("Number", "Name")
reader = csv.DictReader( csvfile, fieldnames)
for row in reader:
    pokemon = row
    newLine = {}
    print(pokemon['Name'] + " (" + pokemon['Number'] + ")")
    readline = input("Is this pokemon in the normal dex? (y/n): ")
    if readline == 'y':
        newLine['Number'] = pokemon['Number']
        newLine['Have'] = 'true'
    elif readline == 'n':
        newLine['Number'] = pokemon['Number']
        newLine['Have'] = 'false'
    pokemons.append(newLine)
data["pokemon"] = pokemons
json.dump(data, jsonfile)
jsonfile.write(',\n')