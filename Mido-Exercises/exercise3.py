import mido

# load midi file
midi_file = mido.MidiFile("../data/exercise3_input.mid")

# print midi file (used for debugging)
# for i, track in enumerate(midi_file.tracks):
#     print('Track {}: {}'.format(i, track.name))
#     for j, event in enumerate(track):
#         print('{}: {}'.format(j, event))

for event in midi_file.tracks[1]:  # for each event in track 1 (1st instrument)
    if event.type == "note_on" or event.type == "note_off":  # if that event turns a not on or turns a note off

        if event.time == 480:  # if the note is a quarter note
            event.time = 240  # change it to an eighth note

        elif event.time == 240:  # otherwise, if the note is an eighth note
            event.time = 480  # change it to a quarter note

midi_file.tracks[2][18].time += 960  # delay the first chord in track 2 by a half note
midi_file.tracks[2][21].time = 480  # make the first chord in track 2 a quarter note long

# save the altered midi file
midi_file.save("../data/exercise3_output.mid")
