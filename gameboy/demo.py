import random
from gameboy import GameBoy

gb = GameBoy('pokemon-rosso.gb', window_scale=3, sound=False)
while not gb.tick():
    buttons = ["a", "b", "start", "select"]
    random_button = random.choice(buttons)
    print(f"Premo {random_button}")
    gb.press(random_button)