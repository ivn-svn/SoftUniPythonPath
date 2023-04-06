def start_spring(**kwargs):
    type_dict = {}
    
    # Organize the objects by their type
    for obj_name, obj_type in kwargs.items():
        if obj_type in type_dict:
            type_dict[obj_type].append(obj_name)
        else:
            type_dict[obj_type] = [obj_name]
    
    # Sort the objects in each collection alphabetically
    for obj_type in type_dict:
        type_dict[obj_type].sort()
    
    # Sort the collections by their number of elements and type name
    sorted_collections = sorted(type_dict.items(), key=lambda x: (-len(x[1]), x[0]))

    # Format the output
    result = ""
    for obj_type, objects in sorted_collections:
        result += f"{obj_type}:\n"
        for obj_name in objects:
            result += f"-{obj_name}\n"
    
    return result.strip()

example_objects = {"Water Lilly": "flower",
                   "Swifts": "bird",
                   "Callery Pear": "tree",
                   "Swallows": "bird",
                   "Dahlia": "flower",
                   "Tulip": "flower",}


start_spring(**example_objects)

