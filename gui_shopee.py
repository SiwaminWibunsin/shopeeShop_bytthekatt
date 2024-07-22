import tkinter as tk
from tkinter import ttk
from bot_shopee import login_shopee, check_product_availability, add_to_cart, select_payment_method, confirm_purchase
from selenium import webdriver

def start_bot():
    username = username_entry.get()
    password = password_entry.get()
    product_url = product_url_entry.get()
    payment_method = payment_method_combobox.get()

    driver = webdriver.Chrome()
    if login_shopee(username, password, driver):
        if check_product_availability(product_url, driver):
            if add_to_cart(driver):
                if select_payment_method(driver, payment_method):
                    confirm_purchase(driver)
    driver.quit()

root = tk.Tk()
root.title("Shopee Bot")

tk.Label(root, text="Shopee Username:").grid(row=0, column=0)
username_entry = tk.Entry(root)
username_entry.grid(row=0, column=1)

tk.Label(root, text="Shopee Password:").grid(row=1, column=0)
password_entry = tk.Entry(root, show="*")
password_entry.grid(row=1, column=1)

tk.Label(root, text="Product URL:").grid(row=2, column=0)
product_url_entry = tk.Entry(root)
product_url_entry.grid(row=2, column=1)

tk.Label(root, text="Payment Method:").grid(row=3, column=0)
payment_method_combobox = ttk.Combobox(root, values=["ShopeePay", "CreditCard", "BankTransfer"])
payment_method_combobox.grid(row=3, column=1)

start_button = tk.Button(root, text="Start Bot", command=start_bot)
start_button.grid(row=4, column=0, columnspan=2)

root.mainloop()
