courses = {'java': 'magi', 'python': 'svetlin', 'html': 'nobody'}
new = 'new'
courses = {v: [k] for k,v in courses.items()}
print(courses)
for k,v in courses.items():
    courses[k] = courses[k] + [new]
print(courses)