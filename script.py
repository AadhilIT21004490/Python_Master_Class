amount = 2400


def calculate_bill(amount):

    tax = amount * 0.0
    total = amount + tax

    if amount > 1000:
        discount = amount * 0.30
        total = total - discount
        print(f"Your total amount is : {total}")
    else:
        print(f"Your total amount is : {total}")

calculate_bill(amount)
calculate_bill(amount)
calculate_bill(amount)