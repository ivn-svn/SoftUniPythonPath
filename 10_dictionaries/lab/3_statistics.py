# https://softuni.bg/downloads/svn/soft-tech/May-2020/Python/07-Dictionaries/07.%20Dictionaries-Lab.docx
# 3. Statistics
# # You seem to be doing great at your first job. You have now successfully completed the first 2 of your tasks and your
# # boss decides to give you as your next task something more challenging. You have to accept all the new products coming
# # in the bakery and finally gather some statistics.
# # You will be receiving key-value pairs on separate lines separated by ": " until you receive the command "statistics".
# # Sometimes you may receive a product more than once. In that case you have to add the new quantity to the existing one.
# # When you receive the "statistics" command, print the following:
# # "Products in stock:
# # - {product1}: {quantity1}
# # - {product2}: {quantity2}
# # …
# # Total Products: {count_all_products}
# # Total Quantity: {sum_all_quantities}"
def solve(products_quantity_str, products_str):
    values = products_quantity_str.split(" ")
    n = len(values)
    products_quantities_dict = {values[i]: int(values[i + 1]) for i in range(0, n, 2)}
    #
    for product in products_str.split(" "):
        if product in products_quantities_dict:
            quantity = products_quantities_dict[product]
            print(f'We have {quantity} of {product} left')
        else:
            print(f'Sorry, we don\'t have {product}')


solve(input(), input())
