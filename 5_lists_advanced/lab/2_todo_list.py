# You will receive a todo-notes until you get the
#  command "End".
#  The notes will be in the format:
#  "{importance}-{value}".
#  Return the list of todo-notes sorted by importance.
#  The maximum importance will be 10
notes = []
importance_eval = 0
sorted_notes = []
while True:
    command = input().split("-")
    if command == "End":
        break
    else:
        importance_eval = command[0]
        notes = command[1]
        while 10 >= importance_eval >= 0:
            sorted_notes.append(importance_eval + notes)
            [x for x in range(1, 10)]
