# You will be receiving to-do notes until you get the command "End". The notes will be in the format:
# "{importance}-{note}". Return the list of to-do notes sorted by importance.
# The importance value will always be an integer between 1 and 10 (inclusive).
notes = [0] * 10
command = input()
if command == 'End':
    