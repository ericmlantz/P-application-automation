# Importing from 3rd party libraries
from selenium import webdriver
from selenium.webdriver.common.by import By
# Importing from this repo


# ----------------------------------------
# Create new web browser instance
driver = webdriver.Chrome()
driver.get('https://boards.greenhouse.io/lucidsoftware/jobs/4365607004')

# Get first name box filled.
labelsList = []
label_fields = driver.find_elements(
    By.TAG_NAME, 'label')
for label_field in label_fields:
    labelsList.append(str(label_field.text))

print(labelsList)
# Based on the location of the first input box, go to the next input box to fill out the next info.
# last_name = driver.find_element(
#     By.XPATH, '/html/body/div[1]/div/div/div[4]/form/div[1]/div[4]/input').send_keys('Lantz')
