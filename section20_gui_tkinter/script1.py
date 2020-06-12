from tkinter import *

window = Tk()


def kt_to_miles():
    miles = float(e1_value.get()) * 1.6
    round_miles = "{:.2f}".format(round(miles, 2))
    t1.delete("1.0", END)
    t1.insert(END, round_miles)


b1 = Button(master=window, text="Execute", command=kt_to_miles)
b1.grid(row=0, column=0)

e1_value = StringVar()
e1 = Entry(window, textvariable=e1_value)
e1.grid(row=0, column=1)


t1 = Text(window, height=1, width=20)
t1.grid(row=0, column=2)

window.mainloop()