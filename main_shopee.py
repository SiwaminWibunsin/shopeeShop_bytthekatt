import os
import tempfile
import tkinter as tk
from tkinter import ttk
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def start_bot():
    username = username_entry.get()
    password = password_entry.get()
    product_url = product_url_entry.get()
    quantity = quantity_entry.get()
    payment_method = payment_method_combobox.get()
    browser_choice = browser_choice_combobox.get()

    # Let user open the browser and login manually, then use the session
    if browser_choice == "Chrome":
        options = webdriver.ChromeOptions()
        user_data_dir = os.path.join(os.getenv("LOCALAPPDATA"), "Google", "Chrome", "User Data")
        options.add_argument(f"user-data-dir={user_data_dir}")
        driver = webdriver.Chrome(options=options)
    elif browser_choice == "Edge":
        options = webdriver.EdgeOptions()
        user_data_dir = os.path.join(os.getenv("LOCALAPPDATA"), "Microsoft", "Edge", "User Data")
        options.add_argument(f"user-data-dir={user_data_dir}")
        driver = webdriver.Edge(options=options)
    else:
        options = webdriver.ChromeOptions()
        user_data_dir = os.path.join(os.getenv("LOCALAPPDATA"), "Google", "Chrome", "User Data")
        options.add_argument(f"user-data-dir={user_data_dir}")
        driver = webdriver.Chrome(options=options)  # Default to Chrome if none selected

    driver.get('https://shopee.co.th')

    input("Please log in manually and press Enter here after logging in and completing CAPTCHA...")

    driver.get(product_url)
    
    if check_product_availability(driver, product_url):
        proceed_to_checkout(driver, quantity, payment_method)
    else:
        print("Product not available.")

def check_product_availability(driver, product_url):
    try:
        driver.get(product_url)
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "btn-buy"))
        )
        return True
    except Exception as e:
        print(f"Product not available: {e}")
        return False

def proceed_to_checkout(driver, quantity, payment_method):
    try:
        print("Proceeding to checkout...")
        # Add your logic to proceed to checkout here
    except Exception as e:
        print(f"Checkout failed: {e}")

root = tk.Tk()
root.title("Shopee Bot")
root.geometry("350x250")

tk.Label(root, text="Username:").grid(row=0, column=0, padx=5, pady=5)
username_entry = tk.Entry(root)
username_entry.grid(row=0, column=1, padx=5, pady=5)

tk.Label(root, text="Password:").grid(row=1, column=0, padx=5, pady=5)
password_entry = tk.Entry(root, show="*")
password_entry.grid(row=1, column=1, padx=5, pady=5)

tk.Label(root, text="Product URL:").grid(row=2, column=0, padx=5, pady=5)
product_url_entry = tk.Entry(root)
product_url_entry.grid(row=2, column=1, padx=5, pady=5)

tk.Label(root, text="Quantity:").grid(row=3, column=0, padx=5, pady=5)
quantity_entry = tk.Entry(root)
quantity_entry.grid(row=3, column=1, padx=5, pady=5)

tk.Label(root, text="Payment Method:").grid(row=4, column=0, padx=5, pady=5)
payment_method_combobox = ttk.Combobox(root, values=["SPayLater", "QR พร้อมเพย์", "ShopeePay", "บัตรเครดิต/บัตรเดบิต", "การผ่อนชำระผ่านบัตรเครดิต"])
payment_method_combobox.grid(row=4, column=1, padx=5, pady=5)

tk.Label(root, text="Browser Choice:").grid(row=5, column=0, padx=5, pady=5)
browser_choice_combobox = ttk.Combobox(root, values=["Chrome", "Edge"])
browser_choice_combobox.grid(row=5, column=1, padx=5, pady=5)

start_button = tk.Button(root, text="Start Bot", command=start_bot)
start_button.grid(row=6, column=0, columnspan=2, padx=5, pady=5)

root.mainloop()
