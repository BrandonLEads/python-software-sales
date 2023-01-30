#Brandon Eads

#prompts the user for the quantity of packages purchased
quantity = input('What is the quantity of packages purchased? ')

quantity_as_num = float(quantity)

#retail price
starting_price = 99

#total - quantity_as_num * price
total_price_before_discount = quantity_as_num * 99
discount = 0.00
total_after_discount = 0.00

#if, elif and else statements providing 10%, 20%, 30% and 40% discounts
if(quantity_as_num >= 10 and quantity_as_num <= 19):
  discount = total_price_before_discount * 0.1
  total = (total_price_before_discount) - (discount)
elif(quantity_as_num >= 20 and quantity_as_num <= 49):
  discount = total_price_before_discount * 0.2
  total = (total_price_before_discount) - (discount)
elif(quantity_as_num >= 50 and quantity_as_num <= 99):
  discount = total_price_before_discount * 0.3
  total = (total_price_before_discount) - (discount)
else:
  discount = total_price_before_discount * 0.4
  total = (total_price_before_discount) - (discount)
  
#prints discount amount and total after discount
print('Your discount total was:', discount)
print('Your total after discount is: ', total)

