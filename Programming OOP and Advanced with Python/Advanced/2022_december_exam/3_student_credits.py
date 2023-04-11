

def students_credits(*args):

    total_credits = 0
    credits_needed = 0
    credits_dict = dict()
    # Used to finally print the results
    output = ""

    for course in args:
        course_name = course.split("-")[0]
        course_credits = int(course.split("-")[1])
        max_test_points = int(course.split("-")[2])
        diyan_points = int(course.split("-")[3])
        # Calculate the credits Diyan gains from the course
        percentage = diyan_points / max_test_points
        diyan_course_credits = course_credits * percentage
        total_credits += diyan_course_credits
        # Add them to the dictionary
        if course_name not in credits_dict:
            credits_dict[course_name] = diyan_course_credits

    if total_credits >= 240:
        output += (f"Diyan gets a diploma with {total_credits:.1f} credits.\n")
    else: 
        credits_needed = 240 - total_credits
        output += (f"Diyan needs {credits_needed:.1f} credits more for a diploma.\n")

  
  
    # Sort the dictionary in descending order by Diyan's credits    
    sorted_dict = sorted(credits_dict.items(), key=lambda x: x[1], reverse=True)
    for (course_name, credit) in sorted_dict:
        output += (f"{course_name} - {credit:.1f}\n")
    output = output.strip()
    return output

print(
    students_credits(
        "Computer Science-12-300-250",
        "Basic Algebra-15-400-200",
        "Algorithms-25-500-490"
    )
)

print(
    students_credits(
        "Discrete Maths-40-500-450",
        "AI Development-20-400-400",
        "Algorithms Advanced-50-700-630",
        "Python Development-15-200-200",
        "JavaScript Development-12-500-480",
        "C++ Development-30-500-405",
        "Game Engine Development-70-100-70",
        "Mobile Development-25-250-225",
        "QA-20-300-300",
    )
)

