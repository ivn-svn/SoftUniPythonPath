user_input = "George,Peter,William,Paid,Michael,Oscar,Olivia,Linda,End,"
lst_user_input = user_input.split(",")
top_queue = 0
lst_idx = 0
serve_list = []
for item in lst_user_input:
    if item == "Paid":
        end_queue = lst_user_input.index(item) - 1
        pop_names = lst_user_input[top_queue:end_queue]
        top_queue = lst_idx
        for name in pop_names:
            lst_user_input.pop(name)

    for customer in lst_user_input:
        if customer != "Paid":
            serve_list.append(customer)
    lst_idx += 1

print(len(serve_list) + " people remaining")
        