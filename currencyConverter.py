# European Central Bank : Currency Exchange Rate
# https://www.ecb.europa.eu/stats/policy_and_exchange_rates/euro_reference_exchange_rates/html/index.en.html


from currency_converter import CurrencyConverter
from currency_converter import ECB_URL
from tkinter import *
from tkinter import messagebox
from datetime import date

# Variable
c = CurrencyConverter(ECB_URL)

# Color
co1 = 'mediumpurple'
co2 = 'lavender'

# Create Tk()
root = Tk()
root.title("Currency Converter System")

# Create Variable
money = IntVar()

# Create Frame
frame1 = Frame(root)
frame1.grid(row=0, column=0, columnspan=2)
frame2 = Frame(root)
frame2.grid(row=1, column=0)

# Title Label
lb_title = Label(frame1, text="Currency Convert", bg=co1, fg=co2, width=20, height=2, font=('tahoma', 24, 'bold'))
lb_title.grid(row=0, column=0, columnspan=2)

# Create Function : currencyConvert
def currenConvert():
    et_value_from = et_cv_from.get()
    uppercase_from = et_value_from.upper()
    et_value_to = et_cv_to.get()
    uppercase_to = et_value_to.upper()

    currency_convert = c.convert(float(et_cv_amount.get()), str(uppercase_from), str(uppercase_to))

    currency_convert_str = "{:.3f}".format(currency_convert)
    lb_cv_result.configure(text=currency_convert_str)

# Create Function : dateCheck
def dateCheck():
    try:
        et_value_from = et_cv_from.get()
        uppercase_from = et_value_from.upper()
        et_value_to = et_cv_to.get()
        uppercase_to = et_value_to.upper()

        date_check_convert = c.convert(float(et_cv_amount.get()), str(uppercase_from), str(uppercase_to), date=date(int(et_date_year.get()), int(et_date_month.get()), int(et_date_date.get())))

        date_check_convert_str = "{:.3f}".format(date_check_convert)
        lb_date_result.configure(text=float(date_check_convert_str))
    except ValueError:
        messagebox.showerror("Converter" ,"Invalid date time input")

# Create Function : deleteConvertText
def deleteConvertText():
    et_cv_from.delete(0, END)
    et_cv_to.delete(0, END)
    et_cv_amount.delete(0, END)
    lb_cv_result.config(text="")

# Create Function : deleteDateText
def deleteDateText():
    et_date_year.delete(0, END)
    et_date_month.delete(0, END)
    et_date_date.delete(0, END)
    lb_date_result.config(text="")

# Create Label & Entry Currency Convert
lb_cv_from = Label(frame2, text="Convert from : ", font=('tahoma', 14), width=15, anchor=E)
lb_cv_from.grid(row=1, column=0, pady=5, sticky=E)
et_cv_from = Entry(frame2, font=('tahoma', 14), width=15)
et_cv_from.grid(row=1, column=1, sticky=W)

lb_cv_to = Label(frame2, text="Convert to : ", font=('tahoma', 14), width=15, anchor=E)
lb_cv_to.grid(row=2, column=0, pady=5, sticky=E)
et_cv_to = Entry(frame2, font=('tahoma', 14), width=15)
et_cv_to.grid(row=2, column=1, sticky=W)

lb_cv_amount = Label(frame2, text="Amount : ", font=('tahoma', 14), width=15, anchor=E)
lb_cv_amount.grid(row=3, column=0, pady=5, sticky=E)
et_cv_amount = Entry(frame2, font=('tahoma', 14), width=15, textvariable=money)
et_cv_amount.grid(row=3, column=1, sticky=W)

# Create Label Result
lb_cv_result = Label(frame2, text="", font=('tahoma', 16))
lb_cv_result.grid(row=4, column=1, columnspan=2, sticky=W)

# Create Button
btn_convert = Button(frame2, text="Convert", bg=co1, fg=co2, font=16, width=10, height=2, command=currenConvert)
btn_convert.grid(row=5, column=0, padx=10, pady=10, sticky=E)
btn_clear = Button(frame2, text="Clear", bg=co1, fg=co2, font=16, width=10, height=2, command=deleteConvertText)
btn_clear.grid(row=5, column=1, padx=10, pady=10, sticky=W)

# Create Date of the rate
lb_date_rate = Label(frame2, text="Check the date of the rate.'For Example Y2013 M03 D21'")
lb_date_rate.grid(row=6, column=0, columnspan=2)

# Create Label & Entry Date
lb_date_year = Label(frame2, text="Year :")
lb_date_year.grid(row=7, column=0, sticky=E, pady=5)
et_date_year = Entry(frame2, width=20)
et_date_year.grid(row=7, column=1, sticky=W)

lb_date_month = Label(frame2, text="Month :")
lb_date_month.grid(row=8, column=0, sticky=E, pady=5)
et_date_month = Entry(frame2, width=20)
et_date_month.grid(row=8, column=1, sticky=W)

lb_date_date = Label(frame2, text="Date :")
lb_date_date.grid(row=9, column=0, sticky=E, pady=5)
et_date_date = Entry(frame2, width=20)
et_date_date.grid(row=9, column=1, sticky=W)

# Label Date Result
lb_date_result = Label(frame2, text="", font=20)
lb_date_result.grid(row=10, column=1, columnspan=2, sticky=W)

# Button Check & Clear
btn_check = Button(frame2, text="Check", width=10, height=1, command=dateCheck)
btn_check.grid(row=11, column=0, sticky=E, padx=5, pady=10)
btn_clear2 = Button(frame2, text="Clear", width=10, height=1, command=deleteDateText)
btn_clear2.grid(row=11, column=1, sticky=W, padx=5, pady=10)

root.mainloop()