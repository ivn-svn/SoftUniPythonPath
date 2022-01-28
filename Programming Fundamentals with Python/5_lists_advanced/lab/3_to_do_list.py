# You will be receiving to-do notes until you get the command "End". The notes will be in the format:
# "{importance}-{note}". Return the list of to-do notes sorted by importance.
# The importance value will always be an integer between 1 and 10 (inclusive).
import re
notes2 = []
notes = [0] * 10
notes1 = []
command = ''
commands = []
counter = 0
while command != 'End':
    command = input()
    if command != 'End':
        notes[counter] = command
        counter += 1
    else:
        break

notes1 = [nt for nt in notes if nt != 0]

notes1 = sorted(notes1)
for note in notes1:
    rem = re.findall(r"\d*-", str(note))
    rem = ''.join(rem)
    #print(rem)
    note = note.replace(rem, '')
    notes2.append(note)
print(notes2)
