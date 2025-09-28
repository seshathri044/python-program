age=18
has_licsense ="Yes"

if age >= 18:
    if has_licsense == "Yes":
        print("You can Drive")
    else:
        print("Go and take License")
else:
    print("You are too Young to drive")
#Another Case
mark =60
if mark >=80:
    print("A+ Grade")
elif mark >=70:
    print("A Grade")
elif mark>=60:
    print("B Grade")
else:
    print("Fail")
#UseCase
recharge_amount=200
data_balance=1.5
if recharge_amount >= 399 or data_balance >= 1:
    print("Your Eligible for bonus data")
else:
    print("Your not eligible")
#UseCase 2
order_amount=1000
days="Sat"
membership="no"

if (order_amount>=1000 and days in["Sat", "Sun"]) or membership == "Gold":
    print("20% Discount")
else:
    print("No Discount")