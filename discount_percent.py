def calculate_discount(price, discount_percent):
  """
  Calculates the final price after applying a discount (if applicable).

  Args:
      price: The original price of the item.
      discount_percent: The discount percentage (0-100).

  Returns:
      The final price after applying the discount, or the original price if no discount is applied.
  """

  discount = discount_percent / 100
  if discount >= 0.2:  # Apply discount only if 20% or higher
    final_price = price * (1 - discount)
  else:
    final_price = price
  return final_price

# Get user input
original_price = float(input("Enter the original price of the item: "))
discount_percent = float(input("Enter the discount percentage (0-100): "))

# Calculate final price
final_price = calculate_discount(original_price, discount_percent)

# Print the result
if discount_percent >= 0.2:
  print(f"Final price after applying {discount_percent:.1f}% discount: ${final_price:.2f}")
else:
  print(f"No discount applied. Original price: ${original_price:.2f}")
