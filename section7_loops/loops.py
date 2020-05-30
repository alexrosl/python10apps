monday_temperatures = [9.1, 8.8, 7.6]

for temperature in monday_temperatures:
    print(temperature)

for letter in 'hello':
    print(letter.title())

phone_numbers = {"John Smith": "+37682929928", "Marry Simpons": "+423998200919"}

for key, value in phone_numbers.items():
    print("{} has as phone number {}".format(key, value))

a = 3
while a > 0:
    print(a)
    a += 1
    if a >= 10:
        break
    else:
        continue
