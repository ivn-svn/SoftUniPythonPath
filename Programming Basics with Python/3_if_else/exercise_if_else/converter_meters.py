input_number = float(input())
input_text = str(input())
output_text = str(input())
#
result_converter = 0
#
if input_text == "mm":
    if output_text == "cm":
        result_converter = input_number / 10
        print(f"{result_converter:.3f}")
    elif output_text == "m":
        result_converter = input_number / 1000
        print(f"{result_converter:.3f}")
    elif output_text == "mm":
        result_converter = input_number
        print(f"{result_converter:.3f}")
#
if input_text == "m":
    if output_text == "cm":
        result_converter = input_number * 100
        print(f"{result_converter:.3f}")
    elif output_text == "m":
        result_converter = input_number
        print(f"{result_converter:.3f}")
    elif output_text == "mm":
        result_converter = input_number * 1000
        print(f"{result_converter:.3f}")
#
if input_text == "cm":
    if output_text == "cm":
        result_converter = input_number
        print(f"{result_converter:.3f}")
    elif output_text == "m":
        result_converter = input_number / 100
        print(f"{result_converter:.3f}")
    elif output_text == "mm":
        result_converter = input_number * 10
        print(f"{result_converter:.3f}")
#

