import re


def validator(nummatch, lowmatch, upmatch, symbmatch, stmatches, enmatches):
    invalid = False
    if len(stmatches) == len(enmatches) and stmatches == enmatches:
        invalid = False
    else:
        invalid = True
        return invalid

    if nummatch != [] and lowmatch != [] and upmatch != []  and symbmatch != []:
        x = nummatch[0].isnumeric()
        if x:
            invalid = False
        else:
            invalid = True
            return invalid
        if lowmatch[0].isalpha():
            if lowmatch[0].islower():
                invalid = False
            else:
                invalid = True
                return invalid
        if upmatch[0].isalpha():
            if upmatch[0].isupper():
                invalid = False
            else:
                invalid = True
                return invalid
        if "<" and ">" not in symbmatch:
            invalid = False
        else:
            invalid = True
            return invalid

    else:
        invalid = True
        return invalid

    return invalid


n = int(input())
password = ""
group1 = ">"
group2 = "<"

numbers = ""
lower_case = ""
upper_case = ""
symbols = ""

start_pattern = r"(.+)>"
end_pattern = r"\<(.+)"
#
nums_pattern = r"\>(\d+)\|"
lower_pattern = r"\|([a-z]+)\|"
upper_pattern = r"\|([A-Z]+)\|"
symbols_pattern = r"\|(\W+)\<"

for inp in range(0, n):
    line = input()
    start_syms = re.findall(start_pattern, line)
    end_syms = re.findall(end_pattern, line)
    #
    start_matches = re.findall(start_pattern, line)
    end_matches = re.findall(end_pattern, line)
    #
    nums_matches = re.findall(nums_pattern, line)
    lower_matches = re.findall(lower_pattern, line)
    upper_matches = re.findall(upper_pattern, line)
    symbols_matches = re.findall(symbols_pattern, line)

    if validator(nums_matches, lower_matches, upper_matches, symbols_matches, start_matches, end_matches) == False:
        password = nums_matches + lower_matches + upper_matches + symbols_matches
        password = "".join(password)
        print(f"Password: {password}")
    else:
        print(f"Try another password!")
