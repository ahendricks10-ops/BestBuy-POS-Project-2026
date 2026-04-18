class POS_System:
  def __init__(self):
    self.product_catalog = {
        'Lamp': {'price': 50.99, 'stock': 50},
        'Refrigerator': {'price': 899.00, 'stock': 50},
        'Blender': {'price': 250.29, 'stock': 20},
        'Skillet': {'price': 169.75, 'stock': 60},
        'Dutch Pot': {'price': 149.99, 'stock': 60},
        'Broom': {'price': 40.00, 'stock': 65},
        'Vacuum': {'price': 129.00, 'stock': 38},
        'Sofa': {'price': 429.75, 'stock': 50},
        'Bookshelf': {'price': 299.00, 'stock': 40},
        'Dresser': {'price': 99.99, 'stock': 55},
        'Chair': {'price': 49.29, 'stock': 35}
    }

    self.shopping_cart = {}

    self.TAX_RATE = 0.10
    self.DISCOUNT_RATE = 0.05
    self.DISCOUNT_LIMIT = 500

    print('   --- Product Catalog ---\n')
    print('Items            Price    Stock')
    for name, values in self.product_catalog.items():
      price = values['price']
      stock = values['stock']
      print(f"{name:<15}  {price:^7.2f}  {stock:^6}")

  def add_to_cart(self):
    item = input('What item do you want to add to the cart? ')

    if item not in self.product_catalog:
      print('Product not in store.')
    else:
      print('Product available!')
      quantity = int(input('How many do you want? '))
      if self.product_catalog[item]['stock'] >= quantity:
        self.shopping_cart[item] = self.shopping_cart.get(item, 0) + quantity
        self.product_catalog[item]['stock'] -= quantity
        print(f'{quantity} {item}(s) added to your cart.')
      else:
        print('Not enough in stock.')

  def remove_from_cart(self):
    item = input('What do you want to remove from the cart? ')
    if item not in self.shopping_cart:
      print('Item not in cart.')
    else:
      quantity = int(input('How many do you want to remove? '))
      if quantity > self.shopping_cart[item]:
        print(f"You only have {self.shopping_cart[item]} {item}(s) in your cart.")
        return

      self.shopping_cart[item] -= quantity
      self.product_catalog[item]['stock'] += quantity # Return to stock
      if self.shopping_cart[item] == 0:
        del self.shopping_cart[item]
      print(f'{quantity} {item}(s) removed from your cart.')

  def view_cart(self):
    subtotal = 0
    if not self.shopping_cart:
      print('Your cart is empty.')
    else:
      print('\nYour Cart:')
      for item, quantity in self.shopping_cart.items():
        price = self.product_catalog[item]['price']
        total_item_price = quantity * price
        subtotal += total_item_price
        print(f"{item}: {quantity} x ${price:.2f} = ${total_item_price:.2f}")
    return subtotal

  def checkout(self):
    subtotal = self.view_cart()
    if subtotal == 0:
      return

    discount = subtotal * self.DISCOUNT_RATE if subtotal > self.DISCOUNT_LIMIT else 0
    taxed = (subtotal - discount) * self.TAX_RATE
    total = subtotal - discount + taxed

    print(f"Subtotal: ${subtotal:.2f}")
    print(f"Discount: -${discount:.2f}")
    print(f"Tax: ${taxed:.2f}")
    print(f"TOTAL: ${total:.2f}")

    while True:
      try:
        paid = float(input("Enter payment: $"))
        if paid < total:
          print("Not enough money.")
          continue

        change = paid - total
        items = list(self.shopping_cart.keys())
        quantities = list(self.shopping_cart.values())
        prices = [self.product_catalog[item]['price'] for item in items]
        generate_receipt(items, quantities, prices, paid)
        self.shopping_cart.clear()
        break
      except ValueError:
        print("Invalid input.")


def generate_receipt(items, quantities, prices, amount_paid):
    print("\n===== Best Buy Retail Store =====")
    print("=========== Receipt ===========")

    print("\nItem\tQty\tPrice\tTotal")

    subtotal = 0

    for i in range(len(items)):
        total = quantities[i] * prices[i]
        subtotal += total
        print(f"{items[i]}\t{quantities[i]}\t{prices[i]}\t{total}")

    tax = subtotal * 0.15
    total_due = subtotal + tax
    change = amount_paid - total_due

    print("\n-----------------------------")
    print(f"Subtotal:\t{subtotal:.2f}")
    print(f"Sales Tax:\t{tax:.2f}")
    print(f"Total Due:\t{total_due:.2f}")
    print("-----------------------------")

    print(f"Amount Paid:\t{amount_paid}")
    print(f"Change:\t\t{change:.2f}")

    print("\nThank you for shopping at Best Buy Retail Store!")

def display_menu():
  pos_system = POS_System()
  while True:
    print('\n1. Add to Cart')
    print('2. Remove from Cart')
    print('3. View Cart')
    print('4. Checkout')
    print('5. Exit Store')

    choice = input('Enter your choice: ')

    if choice == '1':
      pos_system.add_to_cart()
    elif choice == '2':
      print('Remove from Cart')
      pos_system.remove_from_cart()
    elif choice == '3':
      print('View Cart')
      pos_system.view_cart()
    elif choice == '4':
      print('Checkout')
      pos_system.checkout()
    elif choice == '5':
      print('Exiting Store')
      break
    else:
      print('Invalid choice. Please try again.')

display_menu()
