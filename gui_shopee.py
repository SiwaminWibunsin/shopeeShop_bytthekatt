import tkinter as tk
from tkinter import messagebox

def start_bot():
    try:
        username = username_entry.get()
        password = password_entry.get()
        product_url = url_entry.get()
        quantity = int(quantity_entry.get())
        card_number = card_number_entry.get()
        expiry_date = expiry_date_entry.get()
        cvv = cvv_entry.get()
        
        # เรียกใช้ฟังก์ชันหลักเพื่อเริ่มต้นบอท
        from bot_shopee import run_bot
        run_bot(username, password, product_url, quantity, card_number, expiry_date, cvv)
        messagebox.showinfo("Success", "Bot has successfully completed the task!")
    except Exception as e:
        messagebox.showerror("Error", str(e))

app = tk.Tk()
app.title("Shopee Bot")

tk.Label(app, text="Username").grid(row=0)
tk.Label(app, text="Password").grid(row=1)
tk.Label(app, text="Product URL").grid(row=2)
tk.Label(app, text="Quantity").grid(row=3)
tk.Label(app, text="Card Number").grid(row=4)
tk.Label(app, text="Expiry Date").grid(row=5)
tk.Label(app, text="CVV").grid(row=6)

username_entry = tk.Entry(app)
password_entry = tk.Entry(app, show="*")
url_entry = tk.Entry(app)
quantity_entry = tk.Entry(app)
card_number_entry = tk.Entry(app)
expiry_date_entry = tk.Entry(app)
cvv_entry = tk.Entry(app)

username_entry.grid(row=0, column=1)
password_entry.grid(row=1, column=1)
url_entry.grid(row=2, column=1)
quantity_entry.grid(row=3, column=1)
card_number_entry.grid(row=4, column=1)
expiry_date_entry.grid(row=5, column=1)
cvv_entry.grid(row=6, column=1)

tk.Button(app, text='Start Bot', command=start_bot).grid(row=7, column=1, pady=4)

app.mainloop()
