def mean(value):
    if type(value) == dict:
        return sum(value.values()) / len(value)
    else:
        return sum(value) / len(value)


print(mean([1, 2, 3]))
print(mean({"Marry": 9.1, "Sim": 8.8, "John": 7.5}))


