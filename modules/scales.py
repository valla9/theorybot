import random
import os
import time

notes_flat = ["c", "db", "d", "eb", "e", "f", "gb", "g", "ab", "a", "b", "h"]
notes_sharp = ["c", "c#", "d", "d#", "e", "f", "f#", "g", "g#", "a", "a#", "h"]
scales = ["ionisch",
          "dorisch",
          "phrygisch",
          "lydisch",
          "mixolydisch",
          "äolisch",
          "lokrisch"]
steps = [1, 1, 0, 1, 1, 1, 0]

SYSTEM_FLAT = "\033[92mFlat"
SYSTEM_SHARP = "\033[96mSharp"


def get_scale_from_name_and_key():
    """
    Returns the notes of a scale based on the key (e.g. c#, db or g) 
    and index in the scales list (e.g. 0 for ionic, 4 for mixolydian)
    """
    # this array is going to be filled with the actual scale notes
    notes = []

    # generate random scale
    scale_index = int(random.random() * 7)
    scale = scales[scale_index]

    # randomize, if the system is flat(f, b, eb, ab, db) or sharp(g, d, a, e, h)
    n_harmonic_system = random.choice([SYSTEM_SHARP, SYSTEM_FLAT])

    # define harmonic system dependent variables
    harmonic_system_step = 0
    harmonic_system_notes = []

    
    if n_harmonic_system == SYSTEM_FLAT:
        # for the flat system the iteration step is 5 semitones (c->f, f->b and so on)
        harmonic_system_step = 5
        # setting the notes to flat notes
        harmonic_system_notes = notes_flat
    else:     
        # for the sharp system the iteration step is 5 semitones (c->g, g->d and so on)
        harmonic_system_step = 7
        # setting the notes to flat notes
        harmonic_system_notes = notes_sharp

    # getting the random key index
    key_index = (int(random.random() * 6) * harmonic_system_step) % 12
    
    # extracting the key from notes list
    key = harmonic_system_notes[key_index]    

    # debug: print key and scale
    # print(n_harmonic_system + "\t" + key + " " + scale + "\033[0m")

    # index to get notes in order
    note_order_index = key_index
    # add first note
    notes = harmonic_system_notes[key_index]
    for i in range(7):
        note_order_index = (note_order_index + 1 + steps[(scale_index + i) % 7]) % 12
        notes += ", " + harmonic_system_notes[note_order_index]
    
    os.system('cls')
    print("Welche Tonart ist das?")
    print(notes)
    guess = input("")

    if guess == scale:
        print("\033[92mRichtig!\033[0m das ist " + harmonic_system_notes[key_index] + " " + scale)
    else:
        print("\033[91mFalsch...\033[0m das ist " + harmonic_system_notes[key_index] + " " + scale)
    
    input()

while True:
    get_scale_from_name_and_key()