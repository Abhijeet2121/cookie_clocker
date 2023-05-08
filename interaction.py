# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys

# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
# driver.get("https://en.wikipedia.org/wiki/Main_Page")
# driver.implicitly_wait(10)

# count = driver.find_element(By.CSS_SELECTOR, "#articlecount a")
# # article_count = count.text.split(" ")[0]
# # print(article_count)
# # print(count.text)

# link = driver.find_element(By.LINK_TEXT, "English")
# # print(link.text)
# # link.click()
# search = driver.find_element(By.NAME, "search")
# search.send_keys("Python")
# search.send_keys(Keys.ENTER)