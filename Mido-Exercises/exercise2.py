import mido

# load midi file
midi_file = mido.MidiFile("../data/liebesleid.mid")

# print midi file (used for debugging)
# for i, track in enumerate(midi_file.tracks):
#     print('Track {}: {}'.format(i, track.name))
#     for j, event in enumerate(track):
#         print('{}: {}'.format(j, event))

for i, track in enumerate(midi_file.tracks):  # for each track...
    for event in track:  # for each event in the track
        if event.type == "note_on" or event.type == "note_off":  # if that event turns a note on or turns a note off
            event.note += 2  # transpose its note up a major 2nd

# save the altered midi file
midi_file.save("../data/exercise2_output.mid")
