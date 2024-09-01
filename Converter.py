from tkinter import *
from tkinter import messagebox

def validate_input(input_value):
    try:
        float(input_value)
        return True
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number.")
        return False

def lengthopen():
    lwn = Toplevel(win)
    lwn.title("Length Converter")
    lwn.configure(bg="#f0f8ff")
    lwn.geometry("400x350")

    def lengthcov():
        if validate_input(e2_v1.get()):
            meters = float(e2_v1.get())
            km = meters / 1000
            mm = meters * 1000
            cm = meters * 100

            t1.delete('1.0', END)
            t1.insert(END, km)
            t2.delete('1.0', END)
            t2.insert(END, mm)
            t3.delete('1.0', END)
            t3.insert(END, cm)

    e1 = Label(lwn, text="Enter the length in meters", bg="#4682b4", fg="white")
    e2_v1 = StringVar()
    e2 = Entry(lwn, textvariable=e2_v1, bg="white")
    e3 = Label(lwn, text="Km", bg="#4682b4", fg="white")
    e4 = Label(lwn, text="Mm", bg="#4682b4", fg="white")
    e5 = Label(lwn, text="Cm", bg="#4682b4", fg="white")
    t1 = Text(lwn, height=1, width=15, bg="#e6f7ff")
    t2 = Text(lwn, height=1, width=15, bg="#e6f7ff")
    t3 = Text(lwn, height=1, width=15, bg="#e6f7ff")
    b1 = Button(lwn, text="Convert", command=lengthcov, bg="#5f9ea0", fg="white")

    e1.grid(row=0, column=0, padx=10, pady=10)
    e2.grid(row=0, column=1, padx=10, pady=10)
    e3.grid(row=2, column=0, padx=10, pady=10)
    e4.grid(row=3, column=0, padx=10, pady=10)
    e5.grid(row=4, column=0, padx=10, pady=10)
    t1.grid(row=2, column=1, pady=10, padx=10)
    t2.grid(row=3, column=1, pady=10, padx=10)
    t3.grid(row=4, column=1, pady=10, padx=10)
    b1.grid(row=1, column=1, padx=10, pady=10)

    et = Button(lwn, text="Exit", command=lwn.destroy, bg="#cd5c5c", fg="white")
    et.grid(row=5, column=1, padx=10, pady=10)

def tempopen():
    tw = Toplevel(win)
    tw.configure(bg="#f0f8ff")
    tw.geometry("400x350")
    tw.title("Temperature Converter")

    def tempconv():
        if validate_input(e2_vl.get()):
            temp = float(e2_vl.get())
            so = op.get()
            if so == "F":
                cov1 = (temp - 32) * 5/9 + 273.15  # Fahrenheit to Kelvin
                cov2 = (temp - 32) * 5/9           # Fahrenheit to Celsius
                cov3 = temp                         # Fahrenheit
            elif so == "K":
                cov1 = temp                         # Kelvin
                cov2 = temp - 273.15                # Kelvin to Celsius
                cov3 = (temp - 273.15) * 9/5 + 32   # Kelvin to Fahrenheit
            elif so == "C":
                cov1 = temp + 273.15                # Celsius to Kelvin
                cov2 = temp                         # Celsius
                cov3 = temp * 9/5 + 32              # Celsius to Fahrenheit

            t1.delete("1.0", END)
            t1.insert(END, cov1)
            t2.delete("1.0", END)
            t2.insert(END, cov2)
            t3.delete("1.0", END)
            t3.insert(END, cov3)

    e1 = Label(tw, text="Temperature->", bg="#4682b4", fg="white")
    e2_vl = StringVar()
    op = StringVar()
    op.set("F")
    ops = ["F", "K", "C"]
    opmn = OptionMenu(tw, op, *ops)
    e2 = Entry(tw, textvariable=e2_vl, bg="white")
    e3 = Label(tw, text="Fahrenheit", bg="#4682b4", fg="white")
    e4 = Label(tw, text="Kelvin", bg="#4682b4", fg="white")
    e5 = Label(tw, text="Celsius", bg="#4682b4", fg="white")

    t1 = Text(tw, height=1, width=15, bg="#e6f7ff")
    t2 = Text(tw, height=1, width=15, bg="#e6f7ff")
    t3 = Text(tw, height=1, width=15, bg="#e6f7ff")
    b1 = Button(tw, text="Convert", command=tempconv, bg="#5f9ea0", fg="white")

    e1.grid(row=0, column=0, padx=10, pady=10)
    e2.grid(row=0, column=1, padx=10, pady=10)
    opmn.grid(row=0, column=2, padx=10, pady=10)
    e3.grid(row=2, column=0, padx=10, pady=10)
    e4.grid(row=3, column=0, padx=10, pady=10)
    e5.grid(row=4, column=0, padx=10, pady=10)

    t1.grid(row=2, column=1, pady=10, padx=10)
    t2.grid(row=3, column=1, pady=10, padx=10)
    t3.grid(row=4, column=1, pady=10, padx=10)
    b1.grid(row=1, column=1, padx=10, pady=10)

    et = Button(tw, text="Exit", command=tw.destroy, bg="#cd5c5c", fg="white")
    et.grid(row=5, column=1, padx=10, pady=10)

def wtopen():
    w = Toplevel(win)
    w.title("Weight Converter")
    w.configure(bg="#f0f8ff")
    w.geometry("400x350")

    def weightcov():
        if validate_input(e2_v1.get()):
            grams = float(e2_v1.get())
            kg = grams / 1000
            mg = grams * 1000
            cg = grams * 100

            t1.delete('1.0', END)
            t1.insert(END, kg)
            t2.delete('1.0', END)
            t2.insert(END, mg)
            t3.delete('1.0', END)
            t3.insert(END, cg)

    e1 = Label(w, text="Enter the weight in grams", bg="#4682b4", fg="white")
    e2_v1 = StringVar()
    e2 = Entry(w, textvariable=e2_v1, bg="white")
    e3 = Label(w, text="Kg", bg="#4682b4", fg="white")
    e4 = Label(w, text="Mg", bg="#4682b4", fg="white")
    e5 = Label(w, text="Cg", bg="#4682b4", fg="white")
    t1 = Text(w, height=1, width=15, bg="#e6f7ff")
    t2 = Text(w, height=1, width=15, bg="#e6f7ff")
    t3 = Text(w, height=1, width=15, bg="#e6f7ff")
    b1 = Button(w, text="Convert", command=weightcov, bg="#5f9ea0", fg="white")

    e1.grid(row=0, column=0, padx=10, pady=10)
    e2.grid(row=0, column=1, padx=10, pady=10)
    e3.grid(row=2, column=0, padx=10, pady=10)
    e4.grid(row=3, column=0, padx=10, pady=10)
    e5.grid(row=4, column=0, padx=10, pady=10)
    t1.grid(row=2, column=1, pady=10, padx=10)
    t2.grid(row=3, column=1, pady=10, padx=10)
    t3.grid(row=4, column=1, pady=10, padx=10)
    b1.grid(row=1, column=1, padx=10, pady=10)

    et = Button(w, text="Exit", command=w.destroy, bg="#cd5c5c", fg="white")
    et.grid(row=5, column=1, padx=10, pady=10)

win = Tk()
win.geometry("310x340+500+200")
win.title("UNIT CONVERTER")
win.configure(bg="#f0f8ff")

name = Label(win, text="UNIT CONVERTER", bg="#4682b4", fg="white", justify=CENTER, font="Arial 20 bold", padx=30, pady=24)
name.grid(row=0, column=0, columnspan=2)

e = Label(win, text="Choose one unit :", font="Poppins 18 bold", bg="#f0f8ff")
e.grid(row=1, column=0, pady=10, padx=0)

ut = StringVar()
ut.set("Temp")
units = ["Length", "Temp", "Weight"]
menu = OptionMenu(win, ut, *units)
menu.grid(row=1, column=1, pady=10, padx=0)

def conversion():
    so = ut.get()
    if so == "Length":
        lengthopen()
    elif so == "Temp":
        tempopen()
    elif so == "Weight":
        wtopen()

b = Button(win, text="Convert", command=conversion, bg="#5f9ea0", fg="white")
b.grid(row=2, column=1, padx=10, pady=10)

et = Button(win, text="Exit", command=win.destroy, bg="#cd5c5c", fg="white")
et.grid(row=3, column=1, padx=10, pady=10)

win.mainloop()
