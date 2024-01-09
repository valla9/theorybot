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

def get_scale_audio():
    """
    returns a scale name and the matching audio file
    HOT TO GENERATE SUCH A FILE:
    -> Open Nexus-Synth 
    -> Preset: Nexus Grandpiano
    -> Disable Reverb
    -> 140 BPM
    -> Quarter-Notes
    -> Play with Octave (VIII. Step)
    """
    # generate random scale
    scale_index = int(random.random() * 7)

    scale_name = scales[scale_index]
    scale_audio = open('res/audio/scales/' + scale_name + '.wav', 'rb')
    return [scale_audio, scale_name]


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
    print("Scale Index: " + str(scale_index))
    # randomize, if the system is flat(f, b, eb, ab, db) or sharp(g, d, a, e, h)
    if scale_index != 0:
        n_harmonic_system = random.choice([SYSTEM_SHARP, SYSTEM_FLAT])
    else:
        n_harmonic_system = SYSTEM_SHARP

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
        # setting the notes to sharp notes
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
    """
    if guess == scale:
        print("\033[92mRichtig!\033[0m das ist " + harmonic_system_notes[key_index] + " " + scale)
    else:
        print("\033[91mFalsch...\033[0m das ist " + harmonic_system_notes[key_index] + " " + scale)
   
    print("NOTES: " + str(notes) + "   ---    Scale: " + scale)
    print("NOTES: " + str(harmonic_system_notes))
    print("STEPS: " + str(harmonic_system_step))
    """
    return [notes, scale]