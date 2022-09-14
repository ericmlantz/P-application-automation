from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

# Collect URL from user on the page the application needs to be filled out on.
# application_url = input(
#     "What is the url of the application page you are applying to: ")
# resume_url = input("What is the path to your resume (Absolute Path Required?")
# Create an instance of the chrome browser to use for the automation.
browser = webdriver.Chrome()
# In the new chrome instance, go to the web address that the user inputted earlier
browser.get(
    'https://careers.aristocrat.com/au/en/apply?jobSeqNo=ARISAUR0011297EXTERNALENAU&utm_source=linkedin&utm_medium=phenom-feeds&step=1')
# Application 1: 'https://jobs.lever.co/fast/2c4ce205-83ef-47f1-ba64-a2ab1fd9725b/apply'
# Application 2: 'https://careers.aristocrat.com/au/en/apply?jobSeqNo=ARISAUR0011297EXTERNALENAU&utm_source=linkedin&utm_medium=phenom-feeds&step=1'


# Upload your resume to the upload resume button.
# browser.find_element(By.ID, "resume-upload-input").send_keys(
#     '/Users/ericlantz/Library/Mobile Documents/com~apple~CloudDocs/GeneralAssembly/Outcomes 2/Resumes/PDFs/Eric_Lantz_Resume.pdf')

# Enter your name, email, phone. All in input boxes on page.
# Checks for full name or if not that, than first and last name.
# is_button_visible = browser.find_element(
#     By.CSS_SELECTOR, "[input='first_name']").is_displayed()

# ------------------------------------------------------
# This will find the first ul element on the page, then find all the inputs inside of that 'ul' element. Each of those 'ul' elements will be added to a list named inputItemsList. In that list, the inputs will be looped over and just the name for each will be found.
inputItemsList = []
element = browser.find_element(By.TAG_NAME, 'form')
elements = element.find_elements(By.TAG_NAME, 'label')
for e in elements:
    inputItemsList.append(e.text)
print('Input Items List:', inputItemsList)
# ------------------------------------------------------

# ------------------------------------------------------
# Getting a list of all the input items and filtering to only the ones that have an astrik by their label, aka required items.
# requiredList = []
# astrik = "*"
# for item in inputItemsList:
#     item.replace('\n', '')
#     if '*' in str(item):
#         requiredList.append(item)
# print('Required List:', str(requiredList))
# assert 'First Name' in browser.page_source


# full_name = 0
# first_name = 0
# if 'name' in inputItemsList:
#     full_name = inputItemsList.index('name')
# print(full_name)

# assert "first" in inputItemsList
# print("it's there!")

# TRY: Doing search in your inputItemsList for a specific word and then once you have that word, (like first), have the program use the item at that spot in the list as the item to find in the DOM. So searching for less specific in list and then use the list item it finds to have the exact value to use when identifying an item to type in.
# if 'first' in inputItemsList:
#     print("it's there")

# if 'name' in inputItemsList:
#     browser.find_element(By.ID, 'name').send_keys('Eric Lantz')
# if 'first_name' in inputItemsList:
#     browser.find_element(By.ID, 'first_name').send_keys('Eric')
# if 'last_name' in inputItemsList:
#     browser.find_element(By.ID, 'last_name').send_keys('Lantz')


# if first_name in inputItemsList:
#     browser.find_element(
#         By.CSS_SELECTOR, "").send_keys('Eric')

# if is_button_visible:
#     browser.find_element(
#         By.CSS_SELECTOR, "[input='first_name']").send_keys('Eric')
# elif browser.find_element(By.NAME, 'name'):
#     browser.find_element(By.NAME, 'name').send_keys('Eric Lantz')
# else:
#     pass
# browser.find_element(By.NAME, 'email').send_keys('ericmlantz@gmail.com')
# browser.find_element(By.NAME, 'phone').send_keys('6783158626')

# # Insert Links for Github, Portfolio, and LinkedIn
# browser.find_element(By.NAME, 'urls[LinkedIn]').send_keys(
#     "https://www.linkedin.com/in/eric-lantz/")
# browser.find_element(By.NAME, 'urls[GitHub]').send_keys(
#     "https://github.com/ericmlantz")
# browser.find_element(By.NAME, 'urls[Portfolio]').send_keys(
#     "http://ericlantz.tech")

# # Gender Select Dropdown
# select_element = browser.find_element(By.NAME, 'eeo[gender]')
# select_object = Select(select_element)
# select_object.select_by_value('Male')

# # Race Select Dropdown
# select_element = browser.find_element(By.NAME, 'eeo[race]')
# select_object = Select(select_element)
# select_object.select_by_value('White (Not Hispanic or Latino)')

# # Veteran Status Select Dropdown
# select_element = browser.find_element(By.NAME, 'eeo[veteran]')
# select_object = Select(select_element)
# select_object.select_by_value('I am not a veteran')
