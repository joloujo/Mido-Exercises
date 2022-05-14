import mido

# load midi file
midi_file = mido.MidiFile("../data/guitar_loop.mid")

# print midi file (used for debugging)
# for i, track in enumerate(midi_file.tracks):
#     print('Track {}: {}'.format(i, track.name))
#     for j, event in enumerate(track):
#         print('{}: {}'.format(j, event))

# change note C#3 to B2 in third measure
midi_file.tracks[1][27].note = 47
midi_file.tracks[1][33].note = 47

# change note F#4 to D#4 in third measure
midi_file.tracks[1][30].note = 63
midi_file.tracks[1][34].note = 63

# change note G#2 to E2 in fourth measure
midi_file.tracks[1][37].note = 40
midi_file.tracks[1][49].note = 40

# change note E4 to C#4 in fourth measure
midi_file.tracks[1][42].note = 61
midi_file.tracks[1][46].note = 61

# change note E4 to C#5 in sixth measure
midi_file.tracks[1][66].note = 73
midi_file.tracks[1][70].note = 73

# change note G#2 to E2 in eighth measure
midi_file.tracks[1][85].note = 40
midi_file.tracks[1][97].note = 40

# save the altered midi file
midi_file.save("../data/exercise4_output.mid")
