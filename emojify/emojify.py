#!/usr/bin/env python3

import json
import random

import typer

app = typer.Typer()


@app.command()
def emojify(string: str):

    # Open the emoji→text mapping json
    with open("mappings.json") as json_file:
        data = json.load(json_file)
        alphabet = data["alphabet"]
        compounds = data["compounds"]

    # Replace compounds first
    for text, emoji in compounds.items():
        string = string.replace(text, emoji)

    # Replace single letters
    for text, emoji in alphabet.items():

        for letter in list(string):

            if type(emoji) is list:
                string = string.replace(text, random.choice(emoji), 1)

            elif type(emoji) is str:
                string = string.replace(text, emoji)

    print(string)

    # Print mappings for debug purposes
    # for mapping in [compounds, alphabet]:
    #     for text, emoji in mapping.items():
    #         print(f'{text} = {"".join(emoji)}')


if __name__ == "__main__":
    app()
