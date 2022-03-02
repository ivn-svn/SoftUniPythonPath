class Storage:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = []

    def add_product(self, product):
        if capacity < len(storage) + 1:
            storage.append(product)
    def get_products(self):
        print(storage)


st = Storage(4)
st.add_product("apple")

st.get_products()