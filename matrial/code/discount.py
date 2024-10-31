def discount(products):
   total_discounted=0
   while True:
      product_name=input('enter prodect name:  ')
      if product_name not in map(lambda x:x['name'].lower(),products):
         print('prodectes not found in the taple . please enter a valid prodect. ')
         continue

      quantity_required=float(input('enter quantity required: '))
      product = next(p for p in products if p["name"].lower() == product_name)

 
    
      if quantity_required > product["quantity"]:
         print("Insufficient quantity. Please enter a new quantity.")
         continue

      discount_quantity = quantity_required // 250
      discount_percentage = 5.0 * discount_quantity
      total_discount = min(discount_percentage, 25.0) 
      discounted_price = quantity_required * product["price"] * (1 - total_discount / 100)
      product['quantity']-=quantity_required
      total_discount+= discounted_price

      print(f"Discounted Price: ${discounted_price:.2f}")
    
