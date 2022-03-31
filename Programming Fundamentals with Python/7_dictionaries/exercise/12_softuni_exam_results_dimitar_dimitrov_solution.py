def banned(languages, info):
    for key, value in languages.items():
        for x, y in value.items():
            if x == info[0]:
                languages[key][x] = "banned"
    return languages


def print_results(languages, submissions):

    print("Results:")
    for key, value in languages.items():
        for x, y in value.items():
            if y != "banned":
                print(f"{x} | {y}")
    print("Submissions:")
    for key, value in languages.items():
        print(f"{key} - {submissions[key]}")


languages = dict()
submissions = dict()
while True:
    info = input()
    if info == "exam finished":
        break
    info = info.split("-")
    if "banned" not in info:
        name = info[0]
        language = info[1]
        points = int(info[2])

        if language not in languages:
            languages[language] = dict()
        if name not in languages[language]:
            languages[language][name] = points
        else:
            if languages[language][name] < points:
                languages[language][name] = points
        if language not in submissions:
            submissions[language] = 1
        else:
            submissions[language] += 1
    if "banned" in info:
        banned(languages, info)

print_results(languages, submissions)