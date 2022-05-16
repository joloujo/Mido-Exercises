import mido

# load midi file
midi_file = mido.MidiFile("../data/exercise5_input.mid")


# print midi track[number] (used for debugging)
def print_track(n):
    for i, this_event in enumerate(midi_file.tracks[n]):
        print('{}: {}'.format(i, this_event))


# print midi file (used for debugging)
def print_file():
    for i, this_track in enumerate(midi_file.tracks):
        print('Track {}: {}'.format(i, this_track.name))
        print_track(i)


# ---------- TRACK 1 ----------

# map for notes in the first track. All notes in the track will be mapped according to this dictionary. Right now, it
# maps a rising C major to a falling C major scale
track_1_map = {
    48: 60,  # C3 to C4
    50: 59,  # D3 to B3
    52: 57,  # E3 to A3
    53: 55,  # F3 to G3
    55: 53,  # G3 to F3
    57: 52,  # A3 to E3
    59: 50,  # B3 to D3
    60: 48  # C4 to C3
}

for event in midi_file.tracks[1]:  # for each event in track 1
    if event.type == "note_on" or event.type == "note_off":  # if that event turns a note on or turns a note off
        event.note = track_1_map[event.note]  # change the note to the one the original note maps to

# Change the third quarter note in the scale (A3) to two eighth notes
midi_file.tracks[1][23].time = 240
midi_file.tracks[1].insert(24, mido.Message('note_on', note=57, velocity=127, time=0))
midi_file.tracks[1].insert(25, mido.Message('note_off', note=57, velocity=127, time=240))

# Change the fourth quarter note in the scale (G3) to two eighth notes
midi_file.tracks[1][27].time = 240
midi_file.tracks[1].insert(28, mido.Message('note_on', note=55, velocity=127, time=0))
midi_file.tracks[1].insert(29, mido.Message('note_off', note=55, velocity=127, time=240))

# Change the seventh quarter note in the scale (D3) to two eighth notes
midi_file.tracks[1][35].time = 240
midi_file.tracks[1].insert(36, mido.Message('note_on', note=50, velocity=127, time=0))
midi_file.tracks[1].insert(37, mido.Message('note_off', note=50, velocity=127, time=240))


# ---------- TRACK 2 ----------

# the length that the notes in track two should be changed to. Quarter note is 0.25, eighth note is 0.125
track_2_note_lengths = [
    0.25,
    0.25,
    0.125,
    0.125,
    0.125,
    0.125,
    0.25,
    0.25,
    0.125,
    0.125,
    0.25
]

note_num = 0
for event in midi_file.tracks[2]:  # for each event in track 2
    if event.type == "note_off":  # if that event turns a note off
        # change the length of the note based on track_2_note_lengths
        event.time = int(track_2_note_lengths[note_num] * 1920)
        note_num += 1  # move to the next index in track_2_note_lengths

# ---------- TRACK 3 ----------

midi_file.tracks[3][17].program = 13  # change instrument to xylophone

for event in midi_file.tracks[3]:  # for each event in track 3
    # if that event turns a note on or turns a note off and isn't a C5 (last note)
    if (event.type == "note_on" or event.type == "note_off") and event.note != 72:
        # change the time to 240. This will delay all notes by an eighth note and make them and eighth note long.
        event.time = 240

# save the altered midi file
midi_file.save("../data/exercise5_output.mid")
