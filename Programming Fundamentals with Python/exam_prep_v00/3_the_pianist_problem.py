# Problem 3 - The Pianist
# Problem for exam preparation for the Programming Fundamentals Course @SoftUni.
# Submit your solutions in the SoftUni judge system at https://judge.softuni.org/Contests/Practice/Index/2525#2.

# You are a pianist, and you like to keep a list of your favorite piano pieces. Create a program to help you organize 
# it and add, change, remove pieces from it!
# On the first line of the standard input, you will receive an integer n – the number of pieces you will initially have. 
# On the next n lines, the pieces themselves will follow with their composer and key, 
# separated by "|" in the following format: "{piece}|{composer}|{key}".
#
# Then, you will be receiving different commands, each on a new line, separated by 
# "|", until the "Stop" command is given:
# "Add|{piece}|{composer}|{key}":
# You need to add the given piece with the information about it to the other pieces and print:
# "{piece} by {composer} in {key} added to the collection!"
# If the piece is already in the collection, print:
# "{piece} is already in the collection!"
# "Remove|{piece}":
# If the piece is in the collection, remove it and print:
# "Successfully removed {piece}!"
# Otherwise, print:
# "Invalid operation! {piece} does not exist in the collection."
# "ChangeKey|{piece}|{new key}":
# If the piece is in the collection, change its key with the given one and print:
# "Changed the key of {piece} to {new key}!"
# Otherwise, print:
# "Invalid operation! {piece} does not exist in the collection."
# Upon receiving the "Stop" command, you need to print all pieces in your collection, sorted by their name and 
# by the name of their composer in alphabetical order, in the following format:
# "{Piece} -> Composer: {composer}, Key: {key}"
n = int(input())

end = False

add = 'add'
change = 'change'
remove = 'remove'
# dicts
composer_key = {}
composer_piece = {}

# lists``
printable = []

for idx in range(n):
    
    pieces = input().split('|')
    piece = pieces[0]
    composer = pieces[1]
    key = pieces[2]

    composer_piece[composer] = piece
    composer_key[composer] = key


while end == False:
    commands = input()
    if commands != 'Stop':
        commands = commands.split('|')
        command = commands[0]        
        piece = commands[1]
        composer = commands[2]
        key = commands[3]
        # TODO: finish up if elif block with statements
        if command.lower() == add:
            pass
        elif command.lower() == remove:
            pass
        elif command.lower() == change:
            pass
    else:
        end = True
        break
