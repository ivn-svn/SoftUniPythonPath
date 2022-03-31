# Write a program that keeps the information about companies and their employees.
# You will be receiving company names and an employees' id until you receive the command "End" command. ' \
#     Add each employee to the given company. Keep in mind that a company cannot have two employees with the same id.
# Print the company name and each employee's id in the following format:
# "{company_name}
# -- {id1}
# -- {id2}
# …
# -- {idN}"
# Input / Constraints
#     • Until you receive the "End" command, you will be receiving input in the format:
# "{company_name} -> {employee_id}".
#     • The input always will be valid.
cmd = input()

employee_id_db = dict()
while cmd != 'End':
    company_employee = cmd.split(' -> ')
    company = company_employee[0]
    employee = company_employee[1]
    if company in employee_id_db.keys():
        if employee not in employee_id_db[company]:
            employee_id_db[company].append(employee)
        else:
            pass
    else:
        employee_id_db[company] = list()
        employee_id_db[company].append(employee)

    cmd = input()

for (k, v) in employee_id_db.items():
    print(k)
    if len(v) > 1:
        for id in v:
            print(f"-- {id}")
    else:
        print(f"-- {v[0]}")
