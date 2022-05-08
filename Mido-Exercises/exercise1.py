import mido

# load midi file
midi_file = mido.MidiFile("../data/c_major_scale.mid")

# print midi file (used for debugging)
# for i, track in enumerate(midi_file.tracks):
#     print('Track {}: {}'.format(i, track.name))
#     for j, event in enumerate(track):
#         print('{}: {}'.format(j, event))

# change the third note in the scale to Eb
midi_file.tracks[1][22].note = 51
midi_file.tracks[1][23].note = 51

# change the sixth note in the scale to Ab
midi_file.tracks[1][28].note = 56
midi_file.tracks[1][29].note = 56

# change the seventh note in the scale to Bb
midi_file.tracks[1][30].note = 58
midi_file.tracks[1][31].note = 58

# save the altered midi file
midi_file.save("../data/exercise1_output.mid")
