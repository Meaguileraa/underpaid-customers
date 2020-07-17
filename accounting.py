def invoices(file):

  orders = open(file)
  cost = 1.00

  for line in orders: 
    order = line.split('|')

    name = order[1]
    melons = float(order[2])
    paid = float(order[3])

    customer_expected = melons * cost 
    if customer_expected != paid:
      print(f"{name} paid ${paid:.2f},",
      f"expected ${customer_expected:.2f}")

  orders.close()
invoices("customer-orders.txt")