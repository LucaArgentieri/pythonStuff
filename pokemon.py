import requests
import inquirer


firstGen = requests.get('https://pokeapi.co/api/v2/pokemon?limit=151',
                        headers={"User-Agent": "Hello, again"})

firstGenData = firstGen.json()


def singlePkmnFunction():
    singlePkm = requests.get(f'https://pokeapi.co/api/v2/pokemon/{query}',
                             headers={"User-Agent": "Hello"})

    singlePkmData = singlePkm.json()
    print(f'Hai cercato: {singlePkmData["name"]}')
    print(f'Il suo id è: {singlePkmData["id"]}')


# Pkmn primi 151
pkmns = []

for result in firstGenData['results']:
    pkmn = result['name']
    pkmns.append(pkmn)


# Domande
questions = [
    inquirer.List('risposte',
                  message="Hey, cosa vuoi fare?",
                  choices=['Voglio cercare un Pokémon',
                           'Voglio vedere tutti i Pokémon della prima generazione']),
]
answers = inquirer.prompt(questions)

i = 1
if (answers['risposte'] == 'Voglio vedere tutti i Pokémon della prima generazione'):
    print('Ecco a te i Pokèmon della prima generazione:')
    print("\n".join(pkmns))
else:
    print('Cerca')
    query = input()
    singlePkmnFunction()
