customer = input("Enter customer name: ")
items = ["rice","sugar","salt","oil","flour"]
prices = [300,400,100,350,500]

cart = []
for i in items:
   print(f"{i} - {prices[items.index(i)]}")

customer = input("Enter customer name: ")

items = ["rice","sugar","salt","oil","flour"]
prices = [300,400,100,350,500]

cart = []

# show menu
for i in items:
    print(f"{i} - {prices[items.index(i)]}")

# take items until done
while True:
    user_input = input("Enter item (or type 'done'): ")
    user_input = user_input.lower()

    if user_input == "done":
        break

    if user_input in items:
        index = items.index(user_input)
        cart.append([items[index], prices[index]])
        print(f"{user_input} added to cart ✅")
    else:
        print("Item not available ❌")

print("Your cart:", cart)

total = 0

for item in cart:
    total += item[1]

print("Total Amount:", total)

average = total / len(cart) if cart else 0


if total > 1000:
   discount = total * 0.1
   total_after_discount = total - discount
   print(f"Total after 10% discount: {total_after_discount}")
elif total > 500:
   discount = total * 0.05
   total_after_discount = total - discount
   print(f"Total after 5% discount: {total_after_discount}")
else:
    print("No discount applied.")

final_bill = total_after_discount if total > 500 else total
print(f"Final Bill: {final_bill}")