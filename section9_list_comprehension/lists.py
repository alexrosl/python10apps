temps = [221, 234, 340, -9999, 230]

new_temps = [temp / 10 for temp in temps]
print(new_temps)

cond_new_temps = [temp / 10 for temp in temps if temp != -9999]
print(cond_new_temps)

cond_else_new_temps = [temp / 10 if temp != -9999 else 0 for temp in temps]
print(cond_else_new_temps)

def foo(input_list):
    return [value for value in input_list if type(value) is int]

def foo2(input_list):
    return [value for value in input_list if (type(value) is int and value > 0)]

def foo3(input_list):
    return [value if type(value) is int else 0 for value in input_list]

def foo4(input_list):
    return sum([float(value) for value in input_list])