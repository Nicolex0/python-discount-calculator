def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        # Calculate discount amount
        discount_amount = (discount_percent / 100) * price
        # Caculate final price after discount
        final_price = price - discount_amount
        return final_price
    else:
        return price