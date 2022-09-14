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
    'https://careers.wiley.com/en/position/associate-content-services-pune-ind-1')
# Upload your resume to the upload resume button.
# browser.find_element(By.ID, "resume-upload-input").send_keys(
#     '/Users/ericlantz/Library/Mobile Documents/com~apple~CloudDocs/GeneralAssembly/Outcomes 2/Resumes/PDFs/Eric_Lantz_Resume.pdf')

# Enter your name, email, phone. All in input boxes on page.
# Checks for full name or if not that, than first and last name.
# is_button_visible = browser.find_element(
#     By.CSS_SELECTOR, "[input='first_name']").is_displayed()

# personalInfo = find_element(By.)
inputItemsList = []
text_boxes = browser.find_elements(By.CSS_SELECTOR, '[type="text"]')
for text_box in text_boxes:
    inputItemsList.append(text_box.get_attribute("id"))


# TRY: Doing search in your inputItemsList for a specific word and then once you have that word, (like first), have the program use the item at that spot in the list as the item to find in the DOM. So searching for less specific in list and then use the list item it finds to have the exact value to use when identifying an item to type in.
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
