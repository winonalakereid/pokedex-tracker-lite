import csv
import json

csvfile = open('pokemon.csv', 'r')
jsonfile = open('national-dex.json', 'w')

pokemons = []
data = {}
fieldnames = ("Number", "Name")
reader = csv.DictReader( csvfile, fieldnames)
for row in reader:
    pokemon = row
    pokemonNameLower = pokemon["Name"].lower()
    if pokemonNameLower != 'nidoran(female)' and  pokemonNameLower != 'nidoran(male)' and pokemonNameLower != "farfetch'd" and pokemonNameLower != 'mr. mime' and pokemonNameLower != 'great tusk' and pokemonNameLower != 'mime jr.' and pokemonNameLower != "sirfetch'd" and pokemonNameLower != 'type: null' and pokemonNameLower != 'flabebe' and pokemonNameLower != 'mr. rime' and pokemonNameLower != 'tapu bulu' and pokemonNameLower != 'tapu fini' and pokemonNameLower != 'tapu koko' and pokemonNameLower != 'tapu lele' and pokemonNameLower != 'scream tail' and pokemonNameLower != 'brute bonnet' and pokemonNameLower != 'flutter mane' and pokemonNameLower != 'slither wing' and pokemonNameLower != 'sandy shocks' and pokemonNameLower != 'iron treads' and pokemonNameLower != 'iron bundle' and pokemonNameLower != 'iron hands' and pokemonNameLower != 'iron jugulis' and pokemonNameLower != 'iron moth' and pokemonNameLower != 'iron thorns' and pokemonNameLower != 'roaring moon' and pokemonNameLower != 'iron valiant' and pokemonNameLower != 'walking wake' and pokemonNameLower != 'iron leaves': 
        pokemon['NormalSprite'] = "https://img.pokemondb.net/sprites/home/normal/" + pokemonNameLower + ".png"
        pokemon['ShinySprite'] = "https://img.pokemondb.net/sprites/home/shiny/" + pokemonNameLower + ".png"
    elif pokemonNameLower == 'nidoran(female)':
        pokemon['NormalSprite'] = "https://img.pokemondb.net/sprites/home/normal/nidoran-f.png"
        pokemon['ShinySprite'] = "https://img.pokemondb.net/sprites/home/shiny/nidoran-f.png"
        pokemon['Name'] = 'Nidoran\u2640'
    elif pokemonNameLower == 'nidoran(male)':
        pokemon['NormalSprite'] = "https://img.pokemondb.net/sprites/home/normal/nidoran-m.png"
        pokemon['ShinySprite'] = "https://img.pokemondb.net/sprites/home/shiny/nidoran-m.png"
        pokemon['Name'] = 'Nidoran\u2642'
    elif pokemonNameLower == "farfetch'd":
        pokemon['NormalSprite'] = "https://img.pokemondb.net/sprites/home/normal/farfetchd.png"
        pokemon['ShinySprite'] = "https://img.pokemondb.net/sprites/home/shiny/farfetchd.png"
        pokemon['Name'] = "Farfetch\\'d"
    elif pokemonNameLower == 'mr. mime':
        pokemon['NormalSprite'] = "https://img.pokemondb.net/sprites/home/normal/mr-mime.png"
        pokemon['ShinySprite'] = "https://img.pokemondb.net/sprites/home/shiny/mr-mime.png"
    elif pokemonNameLower == 'great tusk':
        pokemon['NormalSprite'] = "https://img.pokemondb.net/sprites/home/normal/great-tusk.png"
        pokemon['ShinySprite'] = "https://img.pokemondb.net/sprites/home/shiny/great-tusk.png"
    elif pokemonNameLower == 'mime jr.':
        pokemon['NormalSprite'] = "https://img.pokemondb.net/sprites/home/normal/mime-jr.png"
        pokemon['ShinySprite'] = "https://img.pokemondb.net/sprites/home/shiny/mime-jr.png"
    elif pokemonNameLower == "sirfetch'd":
        pokemon['NormalSprite'] = "https://img.pokemondb.net/sprites/home/normal/sirfetchd.png"
        pokemon['ShinySprite'] = "https://img.pokemondb.net/sprites/home/shiny/sirfetchd.png"
        pokemon['Name'] = "Sirfetch\\'d"
    elif pokemonNameLower == 'type: null':
        pokemon['NormalSprite'] = "https://img.pokemondb.net/sprites/home/normal/type-null.png"
        pokemon['ShinySprite'] = "https://img.pokemondb.net/sprites/home/shiny/type-null.png"
    elif pokemonNameLower == 'flabebe':
        pokemon['NormalSprite'] = "https://img.pokemondb.net/sprites/home/normal/flabebe.png"
        pokemon['ShinySprite'] = "https://img.pokemondb.net/sprites/home/shiny/flabebe.png"
        pokemon['Name'] = 'Flab\u00e9b\u00e9'
    elif pokemonNameLower == 'mr. rime':
        pokemon['NormalSprite'] = "https://img.pokemondb.net/sprites/home/normal/mr-rime.png"
        pokemon['ShinySprite'] = "https://img.pokemondb.net/sprites/home/shiny/mr-rime.png"
    elif pokemonNameLower == 'tapu bulu':
        pokemon['NormalSprite'] = "https://img.pokemondb.net/sprites/home/normal/tapu-bulu.png"
        pokemon['ShinySprite'] = "https://img.pokemondb.net/sprites/home/shiny/tapu-bulu.png"
    elif pokemonNameLower == 'tapu fini':
        pokemon['NormalSprite'] = "https://img.pokemondb.net/sprites/home/normal/tapu-fini.png"
        pokemon['ShinySprite'] = "https://img.pokemondb.net/sprites/home/shiny/tapu-fini.png"
    elif pokemonNameLower == 'tapu koko':
        pokemon['NormalSprite'] = "https://img.pokemondb.net/sprites/home/normal/tapu-koko.png"
        pokemon['ShinySprite'] = "https://img.pokemondb.net/sprites/home/shiny/tapu-koko.png"
    elif pokemonNameLower == 'tapu lele':
        pokemon['NormalSprite'] = "https://img.pokemondb.net/sprites/home/normal/tapu-lele.png"
        pokemon['ShinySprite'] = "https://img.pokemondb.net/sprites/home/shiny/tapu-lele.png"
    elif pokemonNameLower == 'scream tail':
        pokemon['NormalSprite'] = "https://img.pokemondb.net/sprites/home/normal/scream-tail.png"
        pokemon['ShinySprite'] = "https://img.pokemondb.net/sprites/home/shiny/scream-tail.png"
    elif pokemonNameLower == 'brute bonnet':
        pokemon['NormalSprite'] = "https://img.pokemondb.net/sprites/home/normal/brute-bonnet.png"
        pokemon['ShinySprite'] = "https://img.pokemondb.net/sprites/home/shiny/brute-bonnet.png"
    elif pokemonNameLower == 'flutter mane':
        pokemon['NormalSprite'] = "https://img.pokemondb.net/sprites/home/normal/flutter-mane.png"
        pokemon['ShinySprite'] = "https://img.pokemondb.net/sprites/home/shiny/flutter-mane.png"
    elif pokemonNameLower == 'slither wing':
        pokemon['NormalSprite'] = "https://img.pokemondb.net/sprites/home/normal/slither-wing.png"
        pokemon['ShinySprite'] = "https://img.pokemondb.net/sprites/home/shiny/slither-wing.png"
    elif pokemonNameLower == 'sandy shocks':
        pokemon['NormalSprite'] = "https://img.pokemondb.net/sprites/home/normal/sandy-shocks.png"
        pokemon['ShinySprite'] = "https://img.pokemondb.net/sprites/home/shiny/sandy-shocks.png"
    elif pokemonNameLower == 'iron treads':
        pokemon['NormalSprite'] = "https://img.pokemondb.net/sprites/home/normal/iron-treads.png"
        pokemon['ShinySprite'] = "https://img.pokemondb.net/sprites/home/shiny/iron-treads.png"
    elif pokemonNameLower == 'iron bundle':
        pokemon['NormalSprite'] = "https://img.pokemondb.net/sprites/home/normal/iron-bundle.png"
        pokemon['ShinySprite'] = "https://img.pokemondb.net/sprites/home/shiny/iron-bundle.png"
    elif pokemonNameLower == 'iron hands':
        pokemon['NormalSprite'] = "https://img.pokemondb.net/sprites/home/normal/iron-hands.png"
        pokemon['ShinySprite'] = "https://img.pokemondb.net/sprites/home/shiny/iron-hands.png"
    elif pokemonNameLower == 'iron jugulis':
        pokemon['NormalSprite'] = "https://img.pokemondb.net/sprites/home/normal/iron-jugulis.png"
        pokemon['ShinySprite'] = "https://img.pokemondb.net/sprites/home/shiny/iron-jugulis.png"
    elif pokemonNameLower == 'iron moth':
        pokemon['NormalSprite'] = "https://img.pokemondb.net/sprites/home/normal/iron-moth.png"
        pokemon['ShinySprite'] = "https://img.pokemondb.net/sprites/home/shiny/iron-moth.png"
    elif pokemonNameLower == 'iron thorns':
        pokemon['NormalSprite'] = "https://img.pokemondb.net/sprites/home/normal/iron-thorns.png"
        pokemon['ShinySprite'] = "https://img.pokemondb.net/sprites/home/shiny/iron-thorns.png"
    elif pokemonNameLower == 'roaring moon':
        pokemon['NormalSprite'] = "https://img.pokemondb.net/sprites/home/normal/roaring-moon.png"
        pokemon['ShinySprite'] = "https://img.pokemondb.net/sprites/home/shiny/roaring-moon.png"
    elif pokemonNameLower == 'iron valiant':
        pokemon['NormalSprite'] = "https://img.pokemondb.net/sprites/home/normal/iron-valiant.png"
        pokemon['ShinySprite'] = "https://img.pokemondb.net/sprites/home/shiny/iron-valiant.png"
    elif pokemonNameLower == 'walking wake':
        pokemon['NormalSprite'] = "https://img.pokemondb.net/sprites/home/normal/walking-wake.png"
        pokemon['ShinySprite'] = "https://img.pokemondb.net/sprites/home/shiny/walking-wake.png"
    elif pokemonNameLower == 'iron leaves':
        pokemon['NormalSprite'] = "https://img.pokemondb.net/sprites/home/normal/iron-leaves.png"
        pokemon['ShinySprite'] = "https://img.pokemondb.net/sprites/home/shiny/iron-leaves.png"
    pokemons.append(pokemon)
data["pokemon"] = pokemons
json.dump(data, jsonfile)
jsonfile.write(',\n')