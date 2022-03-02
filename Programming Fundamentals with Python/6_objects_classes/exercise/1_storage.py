from numpy import product


class Storage:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = []
        self.product = product

    def add_product(product, capacity, storage):
        if capacity < len(storage) + 1:
            storage.append(product)
    def get_products():
        print(storage)


st = Storage(4)
st.add_product("apple")

st.get_products()