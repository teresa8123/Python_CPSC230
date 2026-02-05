# Calculate the total price with tax

initial_price = float(input('What is the price:'))
tax_rate = float(input('What is the sales tax rate:'))

precent_tax = tax_rate / 100
total_tax = initial_price * precent_tax
total_price = float(total_tax) + float(initial_price)

print('Total price is:', float(total_price))
