# Format specifiers = {value:flags} format a value based on what flags are inserted

price1 =3.14159
price2 = -983.53283
price3 = 23.5313

print(f"price 1 is ${price2 :+,.2f}")
print(f"price 3 is ${price3 :+,.2f}")