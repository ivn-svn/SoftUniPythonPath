# You will be receiving to-do notes until you get the command "End". The notes will be in the format:
# "{importance}-{note}". Return the list of to-do notes sorted by importance.
# The importance value will always be an integer between 1 and 10 (inclusive).
import re

notes = [0] * 10
notes1 = []
command = ''
commands = []
counter = 0
cycle = False
while command != 'End' and cycle == False:
    command = input()
    if command != 'End':
        notes[counter] = command
        counter += 1
    else:
        cycle = True

notes = notes.sort()
print(notes)
for note in notes:
    if note != 0:
        rem = re.search(r"\d*-", note)
        note.replace(rem, '')
        notes1.append(note)
print(notes1)
