creadit_number = "1234-5677-8901-2345"

# print(creadit_number[2])
# print(creadit_number[0:4])
# print(creadit_number[5:9])
creadit_number = creadit_number[::-1]
print(creadit_number)

print(creadit_number[5:])
print(creadit_number[:9])
print(creadit_number[-1])
print(creadit_number[-4])
print(creadit_number[-3])
print(creadit_number[0:19:3])
print(creadit_number[::3])


last_digits = creadit_number[-4:]
print(f"XXXX-XXXX-XXXX-{last_digits}")
