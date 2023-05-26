import requests
import json
import sqlite3
import win10toast
from datetime import datetime

pokemon = input('Enter Pokemon you love the most: ')
url = f'https://pokeapi.co/api/v2/pokemon/{pokemon}'
r = requests.get(url)

result_json = r.text
res = json.loads(result_json)
res_structured = json.dumps(res, indent=5)
# print(res_structured)
# print(r.text)
# print(r.status_code)
# print(r.headers)
for pokemon_ability in res['abilities']:
    pokemon_ability_name = pokemon_ability['ability']['name']
    print(pokemon_ability_name)

conn = sqlite3.connect("pokemon.sqlite")
cursor = conn.cursor()

# cursor.execute('''CREATE TABLE Pokemons
# (id INTEGER PRIMARY KEY AUTOINCREMENT,
# pokemon VARCHAR(100),
# ability_name VARCHAR(50));''')
#
cursor.execute("INSERT INTO Pokemons (pokemon, ability_name) VALUES (?, ?)", (pokemon, pokemon_ability_name))
conn.commit()

conn.close()

def anime_quote():
    toast = win10toast.ToastNotifier()
    url = "https://animechan.vercel.app/api/random"
    response = requests.get(url)
    res_json = response.text
    respo = json.loads(res_json)
    result = response.json()
    res = json.dumps(result, indent=5)
    current_date = str(datetime.now().date())

    toast.show_toast(title=f"Today's quoute is: {respo['quote']}", msg=f"anime: {respo['anime']}, character: {respo['character']}", duration=10)
    print(current_date, respo['quote'])

anime_quote()


