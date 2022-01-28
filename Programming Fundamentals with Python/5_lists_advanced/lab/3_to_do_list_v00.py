# You will be receiving to-do notes until you get the command "End". The notes will be in the format:
# "{importance}-{note}". Return the list of to-do notes sorted by importance.
# The importance value will always be an integer between 1 and 10 (inclusive).

notes = [0] * 10
notes_list = []
command = ''
commands = []
counter = 0
while command != 'End':
    command = input()
    if command != 'End':

        notes.pop(counter)
        notes.insert(counter, command)
        counter += 1
    else:
        break
notes1 = []
for note in notes:
    if type(note) != int:
        notes1.append(note)


notes_list = sorted(notes1)
final = []
for note in notes_list:
    # print(note)
    note = note.split("-")[1]
    final.append(note)
print(final)