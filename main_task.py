shoping_list = {
   "Piekarnia": ['Chleb', 'Pączek', 'Bułki'],
   "Warzywniak": ['Marchew', 'Seler', 'Rukola'] 
}
product_count = 0
for product in shoping_list:
    print(f"Idę do {product} kupuję tu następujące rzeczy: {shoping_list.get(product.capitalize())}")
    product_count = product_count + len(shoping_list.get(product))
print(f"W sumie kupuję {product_count} produktów.")
