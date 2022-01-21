# Write a program that reads the path to a file and subtracts the file name and its extension.
# Input
# C:\Internal\training-internal\Template.pptx
# C:\Projects\Data-Structures\LinkedList.cs
# Output
# File name: Template
# File extension: pptx
file = ''
file_path = input()
file_name = ''
file_extension = ''
folder_list = file_path.split("\\")
for x in folder_list:
    for y in x:
        if y == '.':
            file_name = x
            file_name = file_name.split('.')
            file = file_name[0]
            file_extension = file_name[1]

print(f'File name: {file}')
print(f'File extension: {file_extension}')
