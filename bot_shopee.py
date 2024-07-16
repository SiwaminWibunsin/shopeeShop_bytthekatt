from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import random

def login(driver, username, password):
    driver.get('https://shopee.com/login')
    time.sleep(2)
    
    username_input = driver.find_element(By.NAME, 'loginKey')
    password_input = driver.find_element(By.NAME, 'password')
    
    username_input.send_keys(username)
    password_input.send_keys(password)
    
    login_button = driver.find_element(By.XPATH, '//button[@type="button"]')
    login_button.click()
    time.sleep(5)

def add_to_cart(driver, product_url, quantity):
    driver.get(product_url)
    time.sleep(2)
    for _ in range(quantity):
        add_button = driver.find_element(By.XPATH, '//button[contains(text(), "Add to Cart")]')
        add_button.click()
        time.sleep(random.uniform(0.5, 1.5))

def checkout(driver, card_number, expiry_date, cvv):
    cart_url = 'https://shopee.com/cart'
    driver.get(cart_url)
    time.sleep(2)
    
    checkout_button = driver.find_element(By.XPATH, '//button[contains(text(), "Checkout")]')
    checkout_button.click()
    time.sleep(2)
    
    card_number_input = driver.find_element(By.NAME, 'card_number')
    card_number_input.send_keys(card_number)
    
    expiry_date_input = driver.find_element(By.NAME, 'expiry_date')
    expiry_date_input.send_keys(expiry_date)
    
    cvv_input = driver.find_element(By.NAME, 'cvv')
    cvv_input.send_keys(cvv)
    
    confirm_button = driver.find_element(By.XPATH, '//button[contains(text(), "Confirm Payment")]')
    confirm_button.click()

def run_bot(username, password, product_url, quantity, card_number, expiry_date, cvv):
    driver = webdriver.Chrome(executable_path='/path/to/chromedriver')
    
    try:
        login(driver, username, password)
        add_to_cart(driver, product_url, quantity)
        checkout(driver, card_number, expiry_date, cvv)
    finally:
        driver.quit()
