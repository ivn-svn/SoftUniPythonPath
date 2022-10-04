import io 

file = open('text.txt', 'r')

def print_contents(file_path):
    print(f'... Openning(file_path) ... ')
    file = open(file_path)
    print(file.read())

print_contents('./text.txt')
