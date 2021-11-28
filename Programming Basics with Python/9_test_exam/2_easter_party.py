# Ако покани:
#     • Между 10 (вкл.) и 15 (вкл.) човека -> 15 % отстъпка от куверта за един човек
#     • Между 15 и 20 (вкл.) човека -> 20 % отстъпка от куверта за един човек
#     • Над 20 човека -> 25 % отстъпка от куверта за един човек
guests_count = int(input())
voucher_price = float(input())
desi_budget = float(input())

if guests_count >= 10 and guests_count <= 15:
    voucher_price = voucher_price * 0.85
elif guests_count > 15 and guests_count <= 20:
    voucher_price = voucher_price * 0.8
elif guests_count > 20:
    voucher_price = voucher_price * 0.75

cake_price = desi_budget * 0.1
total_amount_party = guests_count * voucher_price + cake_price
if total_amount_party >= desi_budget:
    print(f"It is party time! {desi_budget - total_amount_party:.2f} leva left.")
else:
    print(f"No party! {total_amount_party - desi_budget:.2f} leva needed.")