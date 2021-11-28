income = float(input())
average_score = float(input())
minimum_wage = float(input())
# calculating social and excellence scholarship allowances \/
social_scholarship: int = int(minimum_wage * 0.35)
excellent_scholarship: int = int(average_score * 25)
if average_score >= 5.5:
    if social_scholarship <= excellent_scholarship:
       print(f"You get a scholarship for excellent results {excellent_scholarship} BGN")
elif average_score >= 4.5:
    if income <= minimum_wage:
       print(f"You get a Social scholarship {social_scholarship} BGN")
    else:
       print("You cannot get a scholarship!")
else:
    print("You cannot get a scholarship!")