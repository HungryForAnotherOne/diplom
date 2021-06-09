from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random
import os

# options
from settings import CHROME_PATH


options = webdriver.ChromeOptions()
options.add_experimental_option("useAutomationExtension", False)
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_argument("--kiosk")
p = "Test{}".format(random.randint(1, 255))
# user-agent
options.add_argument("user-agent=Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:84.0) Gecko/20100101 Firefox/84.0")

driver = webdriver.Chrome(
    executable_path=CHROME_PATH,
    options=options
)

# "C:\\users\\selenium_python\\chromedriver\\chromedriver.exe"
# r"C:\users\selenium_python\chromedriver\chromedriver.exe"

try:
    driver.get("http://91.242.35.147/security/authenticate")
    time.sleep(3)

    email_input = driver.find_element_by_xpath("//input[@type='text']")
    email_input.clear()
    email_input.send_keys("hiARTER1")
    time.sleep(1)

    password_input = driver.find_element_by_xpath("//input[@type='password']")
    password_input.clear()
    password_input.send_keys("hiARTER1")
    time.sleep(1)
    password_input.send_keys(Keys.ENTER)
    time.sleep(4)

    driver.find_element_by_xpath("/html/body/section/div[3]/div[1]/div/div[1]/div/ul/li[2]/a/div").click()
    time.sleep(4)

    driver.find_element_by_xpath("/html/body/section/div[3]/div[1]/div/div[2]/div[2]/div[2]/"
                                 "div[2]/div/div/div/div/div/div[1]").click()
    time.sleep(4)

    driver.find_element_by_xpath("/html/body/section/div[3]/div[1]/div/div[5]/div[1]/div/button/div/span").click()
    time.sleep(4)

except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()