from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
# options.add_argument("--headless")
options.page_load_strategy = "none"

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.get("http://orteil.dashnet.org/experiments/cookie/")
driver.implicitly_wait(10)

cookie = driver.find_element(By.CSS_SELECTOR, '#cookie')
items = driver.find_elements(By.CSS_SELECTOR, "#store div")

item_ids = [item.get_attribute("id") for item in items]

timeout = time.time() + 5
five_min = time.time() + 60*5 

while True:
    cookie.click()

    """Every 5 secc"""
    if time.time() > timeout:

        """finding all b tags"""
        all_prices = driver.find_elements(By.CSS_SELECTOR, "#store b")
        item_prices = []

        """Convering b text to integers"""
        for price in all_prices:
            # print(price.text)
            element_text = price.text
            if element_text != "":
                cost = int(element_text.split("-")[1].strip().replace(",", ""))
                print(cost)
                item_prices.append(cost)
            
        """creating dict to save items and prices """
        cookie_upgrade = {}
        for n in range(len(item_prices)):
            cookie_upgrade[item_prices[n]] = item_ids[n]
        
        """Get current cookie count"""
        money_element = driver.find_element(By.ID, "money").text
        if "," in money_element:
            money_element = money_element.replace(",", "")
        cookie_count = int(money_element)

        """find affordable upgrades"""
        affordable_upgrades = {}
        for cost, id in cookie_upgrade.items():
            if cookie_count > cost :
                affordable_upgrades[cost] = id
                # print(affordable_upgrades[cost])
    

        """purchase the most expensive upgrade"""
        highest_price_affordable_upgrade = max(affordable_upgrades)
        print(highest_price_affordable_upgrade)
        to_purchase_id = affordable_upgrades[highest_price_affordable_upgrade]
        print(to_purchase_id)

        # driver.find_element(By.ID, "to_purchase_id").click()

        # add another 5 sec 
        timeout = time.time() + 5

    # After 5 mins check the bot check the cookies count per sec 
    if time.time() > five_min:
        cookie_per_sec = driver.find_element(By.ID, "cps").text
        # print(cookie_per_sec)

        break

driver.close()