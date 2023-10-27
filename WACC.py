from tkinter import *
from tkinter import ttk
from ttkthemes import ThemedTk

prozor = ThemedTk()

prozor.geometry("300x300")
frejm = LabelFrame(prozor)
# Izgled
style = ttk.Style(prozor)
style.theme_use("equilux")
frejm.configure(background="grey")
prozor.configure(background="grey")


# funkcija za izracunavanje
def Wacc():
    wacc = 0
    equity = int(entry1.get())
    debt = int(entry2.get())
    total_value = equity + debt
    Re = float(entry3.get())
    Rd = float(entry4.get())
    Tax = float(entry5.get())
    print(equity)
    wacc = (equity / total_value * Re) + (debt / total_value * Rd * (1 - Tax))
    Label6 = ttk.Label(frejm, text="{wacc:.2f}%".format(wacc=(wacc * 100)))
    Label6.grid(row=5, column=1)


def waccframe():
    frejm.grid(padx=10, pady=10)


# Unos

Label1 = ttk.Label(frejm, text="Equity: ")
entry1 = ttk.Entry(frejm)

Label2 = ttk.Label(frejm, text="Debt: ")
entry2 = ttk.Entry(frejm)

Label3 = ttk.Label(frejm, text="Cost of equity: ")
entry3 = ttk.Entry(frejm)

Label4 = ttk.Label(frejm, text="Cost of debt: ")
entry4 = ttk.Entry(frejm)

Label5 = ttk.Label(frejm, text="Corporate tax rate: ")
entry5 = ttk.Entry(frejm)

CalButton = ttk.Button(frejm, text="Izracunaj WACC: ", command=Wacc)
WaccButton = ttk.Button(prozor, text="WACC", command=waccframe)
quit_button = ttk.Button(
    prozor, text="Quit", command=lambda: (prozor.destroy(), prozor.quit())
)


Label1.grid(row=0, column=0)
entry1.grid(row=0, column=1)

Label2.grid(row=1, column=0)
entry2.grid(row=1, column=1)

Label3.grid(row=2, column=0)
entry3.grid(row=2, column=1)

Label4.grid(row=3, column=0)
entry4.grid(row=3, column=1)

Label5.grid(row=4, column=0)
entry5.grid(row=4, column=1)

WaccButton.grid()

CalButton.grid(row=5, column=0, pady=30)
quit_button.grid()


prozor.mainloop()
