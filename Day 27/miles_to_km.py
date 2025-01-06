from tkinter import *
window = Tk()
FONT = ("Arial", 12)
window.title("Mile to Km Converter")
window.minsize(width=100, height=100)
window.config(padx=100, pady=100)
def calculate():
    miles = float(input.get())
    km = round(miles * 1.609)
    km_label.config(text=f"{km}")
    
#Entry
input = Entry(font=FONT)
input.grid(column=1, row=0)

#Miles_label
miles_label = Label(text="Miles", font=FONT)
miles_label.grid(column=2, row=0)


#Is_Equal_To
is_equal_to = Label(text="is equal to", font=FONT)
is_equal_to.grid(column=0, row=1)

#Label
km_label = Label(text="0", font=FONT)
km_label.grid(column=1, row=1)

#Km
label_km = Label(text="Km", font=FONT)
label_km.grid(column=2, row=1)

#Button
button = Button(text="Calculate", command=calculate, font=FONT)
button.grid(column=1, row=2)



window.mainloop()