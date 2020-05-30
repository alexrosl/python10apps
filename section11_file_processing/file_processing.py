myfile = open("fruits.txt", mode='r')
content = myfile.read()
myfile.close()
print(content)


with open("fruits.txt") as myfile:
    content2 = myfile.read()

print(content2)

open("files/fruits_inside.txt")

with open("files/vegetables.txt", "w") as myfile:
    myfile.write("Tomato\nCucumber\nOnion\n")
    myfile.write("Garlic")

def foo(character, filepath):
    with open(filepath) as myfile:
        return myfile.read().count(character)


with open("files/vegetables.txt", "a+") as myfile3:
    myfile3.seek(0)
    content3 = myfile3.read()
    myfile3.seek(0)
    myfile3.write("\n" + content3)
