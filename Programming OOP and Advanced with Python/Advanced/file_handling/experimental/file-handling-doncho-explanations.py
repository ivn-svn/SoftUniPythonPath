# Not existing file
# open ('. /demo. py')
# Not existing directory with fi
# open('./nested_dir/demo.txt')
# A directory, not a file

try:
    open('./')
    print ('File is found')
except FileNotFoundError:
    print ('File is not found')
except IsADirectoryError:
    print ('File is a directory')
    print_contents('./') # prints the contents of the current folder

except IsADirectoryError:
    print('File is a directory')

