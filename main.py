from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import logging
import time
import pyautogui


logging.basicConfig(level=logging.INFO)

def create_driver_with_roblox():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.get("https://web.roblox.com/home")
    return driver

def set_cookie(driver: webdriver.Chrome, value_cook: str):
    cookie = {'name': '.ROBLOSECURITY', 'value': value_cook, 'domain': '.roblox.com', 'path': '/'}
    driver.add_cookie(cookie)


def check_exists_by_class(driver: webdriver.Chrome, class_name: str):
    try:
        driver.find_element(By.CLASS_NAME, class_name)
    except NoSuchElementException:
        return False
    return True


if __name__ == "__main__":
    with open("all_accounts.txt", encoding="utf-8") as file:
        all_accounts = [line.strip() for line in file.readlines()]
    logging.info(f"Найденно аккаунтов - {len(all_accounts)}")
    for i, account in enumerate(all_accounts, 1):
        logging.info(f"Аккаунт №{i}")
        driver = create_driver_with_roblox()
        url_roblox, cookie_roblox = account.split(";")
        set_cookie(driver, cookie_roblox)
        driver.get(url_roblox)
        time.sleep(3)
        pyautogui.press('tab', presses=2)  # navigate to open button
        pyautogui.press('enter') 
        while check_exists_by_class(driver, "simplemodal-wrap") is True:
            time.sleep(2)
        driver.quit()
