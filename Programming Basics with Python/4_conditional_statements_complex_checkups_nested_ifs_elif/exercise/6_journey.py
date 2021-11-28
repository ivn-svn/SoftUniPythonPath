# Напишете програма, която да приема
# на входа бюджета и сезона, а на изхода да изкарва къде ще почива програмистът и колко ще похарчи.
# Бюджетът определя дестинацията, а сезонът - колко от бюджета ще изхарчи. Ако е лято ще почива на къмпинг, а зимата
# в хотел. Ако е в Европа, независимо от сезона, ще почива в хотел. Всеки къмпинг или хотел, според дестинацията,
# има собствена цена, която отговаря на даден процент от бюджета:
#     • При 100 лв. или по-малко – някъде в България:
#         ◦ Лято – 30% от бюджета;
#         ◦ Зима – 70% от бюджета.
#     • При 1000 лв. или по малко – някъде на Балканите:
#         ◦ Лято – 40% от бюджета;
#         ◦ Зима – 80% от бюджета.
#     • При повече от 1000 лв. – някъде из Европа:
#         ◦ При пътуване из Европа, независимо от сезона, ще похарчи 90% от бюджета.
# Вход
# Входът се чете от конзолата и се състои от два реда, въведени от потребителя:
#     • Бюджет - реално число;
#     • Един от двата възможни сезона - „summer” или “winter”.
# Изход
# На конзолата трябва да се отпечатат два реда:
#     •  „Somewhere in [дестинация]“ измежду “Bulgaria", "Balkans” и ”Europe”
#     • “{Вид почивка} – {Похарчена сума}“:
#         ◦ Почивката може да е между „Camp” и „Hotel”;
#         ◦ Сумата трябва да е закръглена с точност до вторият знак след запетаята.
budget = float(input())
season = str(input().lower())
# Hotel price \/
destination = ""
place_of_stay = ["Hotel", "Camp"]
if season == "summer":
    place_of_stay = place_of_stay[1]
elif season == "winter":
    place_of_stay = place_of_stay[0]
# end of summer/winter check-up
# Check if budget is appropriate for expensive trip:
else:
    pass
hotel_price = 0
if budget <= 100:
   if season == "summer":
       destination = "Bulgaria"
       hotel_price = budget * 0.3
   elif season == "winter":
       destination = "Bulgaria"
       hotel_price = budget * 0.7
   else:
       pass
elif 100 <= budget <= 1000:
    if season == "summer":
        destination = "Balkans"
        hotel_price = budget * 0.4
    elif season == "winter":
        destination = "Balkans"
        hotel_price = budget * 0.8
    else:
        pass
elif budget > 1000:
    destination = "Europe"
    hotel_price = budget * 0.9
#
else:
    pass
print(f"Somewhere in {destination}")
print(f"{place_of_stay} - {hotel_price:.2f}")

