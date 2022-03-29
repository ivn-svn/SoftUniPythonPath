# Given two lists of strings print a new list of the strings that contains words from the first
# list which are substrings of any of the strings in the second list (only unique values)
search_items = input().split(", ")
substr_list = input().split(", ")
items_contained = []
for search_item in search_items:
    for substr_item in substr_list:
        if search_item in substr_item and search_item not in items_contained:
            items_contained.append(search_item)
print(items_contained)