def calculate_total(price, tax_rate=0.05, discount=0) -> float:
    # Calculates final price from:
        # Price before taxes and discount.
        # Applies discount before calculating taxes.
        # Returns net_price after applying taxes to remaining amount
    gross_price = price - discount
    net_price = gross_price - (gross_price*tax_rate/100)
    return net_price


item_price = float(input("Please enter price before taxes and discounts: "))
item_discount = float(input("Please enter amount in $ for discounts: "))
item_tax = input("Please enter tax percentage: ").strip()
item_tax = float(item_tax.removesuffix('%'))

final_amount = calculate_total(item_price,item_tax, item_discount)
print(f'{final_amount:>10}')  # pad to right, left filled with 0s
print(f'{final_amount:^10}')  # Pad center within 10 spaces
print(f'{final_amount:.2f}')  # 2 decimal places: 1234.57
print(f'{final_amount:.2%}')  # Accuracy: 87.30%




