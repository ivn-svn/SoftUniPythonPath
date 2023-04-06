

def start_spring(**kwargs):
    type_dict = {}
    output_dict = {}
    print("Object | Type")
    for obj_key in kwargs.keys():
        obj_type = kwargs[obj_key]
        if obj_type in type_dict.keys():
            type_dict[obj_type].append(obj_key)
        else:
            type_dict[obj_type] = list()
            type_dict[obj_type].append(obj_key)
            





        print(f"{obj_key} | {obj_type}")
   # type_dict = type_dict[type_dict.keys()].sort(key=lambda x: len(x[0]))
    print(type_dict)


example_objects = {"Water Lilly": "flower",
                   "Swifts": "bird",
                   "Callery Pear": "tree",
                   "Swallows": "bird",
                   "Dahlia": "flower",
                   "Tulip": "flower",}


start_spring(**example_objects)

