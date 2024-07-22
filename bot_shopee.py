from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException, ElementClickInterceptedException

def login_shopee(username, password, driver):
    driver.get("https://shopee.co.th/buyer/login")
    try:
        username_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "loginKey"))
        )
        password_input = driver.find_element(By.NAME, "password")
        login_button = driver.find_element(By.XPATH, "//button[contains(text(), 'เข้าสู่ระบบ')]")

        username_input.send_keys(username)
        password_input.send_keys(password)
        driver.execute_script("arguments[0].click();", login_button)

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[contains(text(), 'บัญชีของฉัน')]"))
        )
        return True
    except (TimeoutException, NoSuchElementException, ElementClickInterceptedException) as e:
        print(f"Login failed: {e}")
        return False

def check_product_availability(product_url, driver, quantity):
    driver.get(product_url)
    try:
        buy_now_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[contains(text(), 'ซื้อสินค้า')]"))
        )
        quantity_input = driver.find_element(By.CLASS_NAME, "product-quantity-input")
        quantity_input.clear()
        quantity_input.send_keys(str(quantity))
        return True
    except (TimeoutException, NoSuchElementException) as e:
        print(f"Product not available: {e}")
        return False

def add_to_cart(driver, quantity):
    try:
        add_to_cart_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[contains(text(), 'เพิ่มลงรถเข็น')]"))
        )
        add_to_cart_button.click()
        return True
    except (TimeoutException, NoSuchElementException) as e:
        print(f"Failed to add product to cart: {e}")
        return False

def select_payment_method(driver, payment_method):
    try:
        payment_method_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, f"//label[contains(text(), '{payment_method}')]"))
        )
        payment_method_button.click()
        return True
    except (TimeoutException, NoSuchElementException) as e:
        print(f"Failed to select payment method: {e}")
        return False

def confirm_purchase(driver):
    try:
        confirm_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[contains(text(), 'สั่งซื้อสินค้า')]"))
        )
        confirm_button.click()
        return True
    except (TimeoutException, NoSuchElementException) as e:
        print(f"Failed to confirm purchase: {e}")
        return False
