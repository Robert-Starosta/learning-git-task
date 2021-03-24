shoping_list = {
   "Piekarnia": ['Chleb', 'Pączek', 'Bułki'],
   "Warzywniak": ['Marchew', 'Seler', 'Rukola'] 
}
product_count = 0
for product in shoping_list:
    print(f"Idę do {product} kupuję tu następujące rzeczy: {shoping_list.get(product)}")