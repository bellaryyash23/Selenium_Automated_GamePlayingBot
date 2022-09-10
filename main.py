import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys

chrome_webdriver_path = "C:\Development\chromedriver_win32\chromedriver.exe"

ser = Service(executable_path=chrome_webdriver_path)

driver = webdriver.Chrome(service=ser)
driver.get("http://orteil.dashnet.org/experiments/cookie/")

cookie = driver.find_element(by="id", value="cookie")

timeout_start = time.time()
timeout = 240
timeout_sec = time.time() + 5

while time.time() < timeout_start + timeout:
    cookie.click()
    money = int(driver.find_element(by="id", value="money").text.strip(" ").replace(",", ""))
    if time.time() > timeout_sec:
        categories = [categories.text for categories in
                      driver.find_elements(by="css selector", value="#rightPanel b")]
        amount = [int(categories[i].split("-")[1].strip(" ").replace(",", "")) for i in
                  range(0, len(categories) - 1)]
        categorie_names = [categories[i].split("-")[0].strip(" ") for i in range(0, len(categories) - 1)]
        upgardes = [{"name": categorie_names[i], "amount": amount[i]} for i in range(0, len(amount))]
        for value in upgardes:
            if money >= value["amount"]:
                driver.find_element(by="id", value=f"buy{value['name']}").click()

cps = driver.find_element(by="id", value="cps").text.split(":")[1]
print(f"This is my cookie/second score: {cps}")

driver.quit()
