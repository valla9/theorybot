import random

songs = [
    "He's a pirate",
    "Rosanna",
    "How To Train Your Dragon",
    "Piano Man",
    "Du bist immer da",
    "Adeste Fidelis",
    "Deutsche Nationalhymne",
    "Hallelujah"
]

keys = [
    "F#",
    "H",
    "E",
    "A",
    "D",
    "G",
    "C",
    "F",
    "Bb",
    "Eb",
    "Ab",
    "Db"
]

print("\033[96m" + random.choice(songs) + "\033[0m in \033[92m" + random.choice(keys) + "\033[0m")