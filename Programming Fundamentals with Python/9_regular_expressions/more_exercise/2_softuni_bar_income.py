import re
def is_float(a_string):
    try:
        float(a_string)
        return True
    except ValueError:
        return False
line = input()
valid_lines = []
person_pattern = r'\%([A-z][a-z]+)\%'
product_pattern = r'\<([a-zA-Z]+)\>'
count_pattern = r'\|(\d{1,2})\|'
float_pattern = r'\|(\d{1,3}\.\d{1,3})\$|\|\w+(\d+\d+)|(\d+)\$'
allvalid = False
budget = 0
while line != "end of shift":
    valid_line = ""
    person_match = re.findall(person_pattern, line)
    product_match = re.findall(product_pattern, line)
    count_match = re.findall(count_pattern, line)
    float_match = re.findall(float_pattern, line)
    for digit in float_match:
        for fl in digit:
            if is_float(fl):
                float_match = float(fl)
    # print('____________________________________')
    # print(f"Person match: {person_match}")
    # print(f"Product match: {product_match}")
    # print(f"Count match: {count_match}")
    # print(f"Float match: {float_match}")
    # print('____________________________________')
    line = input()
    if len(person_match) > 0 and len(product_match) > 0 and len(count_match) > 0 and float_match:
        customer_name = person_match[0]
        product = product_match[0]
        total_price = float_match * int(count_match[0])
        print(f"{customer_name}: {product} - {total_price:.2f}")
        budget += total_price
print(f"Total income: {budget:.2f}")
