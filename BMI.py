import tkinter
import math

window = tkinter.Tk()
window.title("BMI")
window.minsize(300, 300)


def calculate_bmi():
    kg = float(weight_entry.get())
    cm = float(height_entry.get())

    BMI = kg / (cm ** 2)
    print(BMI)
    label = tkinter.Label()
    if BMI < 16.0:
        label.config(text="Severely Underweight ")
    elif 16.0 < BMI < 18.4:
        label.config(text="Underweight")
    elif 18.5 < BMI < 24.9:
        label.config(text="Normal")
    elif 25.0 < BMI < 29.9:
        label.config(text="Overweight")
    elif 30.0 < BMI < 34.9:
        label.config(text="Moderately Obese")
    elif 35.0 < BMI < 39.9:
        label.config(text="Severally Obese")
    elif BMI > 40.0:
        label.config("Morbidly Obese")

    label.pack()


#Weight
weight_label = tkinter.Label(text="Enter your Weight(kg)")
weight_label.pack()
weight_entry = tkinter.Entry()
kg = weight_entry.get()
weight_entry.pack()
#height
height_label = tkinter.Label(text="Enter your Height(cm)")
height_label.pack()
height_entry = tkinter.Entry()
cm = height_entry.get()
height_entry.pack()

#Button
calculate_button = tkinter.Button(text="Calculate", command=calculate_bmi)
calculate_button.pack()

window.mainloop()
