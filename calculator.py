def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        # Calculate discount amount
        discount_amount = (discount_percent / 100) * price
        # Caculate final price after discount
        final_price = price - discount_amount
        return final_price
    else:
        return price
    
# Get user input
price = float(input("Enter the price of the item: "))
discount_percent = float(input("Enter the discount percentage: "))

# Get the final price
final_price = calculate_discount(price, discount_percent)

print(f"The final price after discount is: ${final_price:.2f}")