print("Beckett Pizza Plaza 4-for-3 Offer")
print("=================================\n")

prices = []
pizza_number = 1

# Keep asking until we have four valid prices
while len(prices) < 4:
    try:
        price = float(input(f"Enter Price of Pizza #{pizza_number}: "))
        
        if price <= 0:
            print("Please enter a valid price!")
            continue
        
        prices.append(price)
        pizza_number += 1
    
    except ValueError:
        print("Please enter a valid price!")

# Calculate totals
original_total = sum(prices)
cheapest_pizza = min(prices)
discounted_total = original_total - cheapest_pizza

# Calculate discount percentage
discount_percentage = round((cheapest_pizza / original_total) * 100)

# Display result
print(f"\nOrder Total is £{discounted_total:.2f}, a fabulous discount of {discount_percentage}%!")
