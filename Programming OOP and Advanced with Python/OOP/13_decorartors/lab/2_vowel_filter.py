def vowel_filter(function):
    def wrapper():
        # TODO: Implement
        returnable = []
        vowels = "aeouyi"
        for i in function():
            if i in vowels:
                returnable.append(i)
        return returnable
    return wrapper

@vowel_filter
def get_letters():
    return ["a", "b", "c", "d", "e"]

print(get_letters())