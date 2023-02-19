# This website use prompt to get your e-transfer answers. 
import requests
import time
import random
import string
from selenium import webdriver
from selenium.webdriver.common.by import By

# get word list
word_site = "https://www.mit.edu/~ecprice/wordlist.10000"
response = requests.get(word_site)
word_list = response.content.splitlines()

# some parameters
url = "https://confirm-my-interac.com/en"
question = 'password?'

driver = webdriver.Firefox()
driver.get(url)

while(True):
    index = random.randint(0, len(word_list) - 1)
    num = random.randint(10, 1000)
    letters = string.ascii_lowercase
    answers = ''.join(random.choice(str(letters)) for i in range(20))

    # fill out form
    driver.find_element(By.NAME, "wpforms[fields][0]").send_keys(str(word_list[index])[2:-1])
    index = random.randint(0, len(word_list) - 1)
    driver.find_element(By.NAME, "wpforms[fields][3]").send_keys(str(num))
    index = random.randint(0, len(word_list) - 1)
    driver.find_element(By.NAME, "wpforms[fields][4]").send_keys(str(word_list[index])[2:-1])
    index = random.randint(0, len(word_list) - 1)
    driver.find_element(By.NAME, "wpforms[fields][5]").send_keys(str(word_list[index][2:-1]))
    driver.find_element(By.NAME, "wpforms[fields][6]").send_keys(answers)

    # click button
    driver.find_element(By.ID, "wpforms-submit-108").click()

    # go back to previous form page
    
    # driver.back()
    # driver.execute_script("window.history.go(-1)")

    # time.sleep(2)
    # clear out form
    # driver.find_element(By.NAME, "wpforms[fields][0]").clear()
    # driver.find_element(By.NAME, "wpforms[fields][3]").clear()
    # driver.find_element(By.NAME, "wpforms[fields][4]").clear()
    # driver.find_element(By.NAME, "wpforms[fields][5]").clear()
    # driver.find_element(By.NAME, "wpforms[fields][6]").clear()
    time.sleep(4)
    driver.get(url)