from selenium import webdriver
from dotenv import load_dotenv
from selenium.webdriver.common.by import By
import os
import time

load_dotenv()
user = os.getenv("USER")    
pwrd = os.getenv("PWRD")

options = webdriver.FirefoxOptions()

'''
TODO: When putting this on the server,it'll make sense to 
enable headless. unecessary for now.

options.add_argument("--headless=new")
'''

driver = webdriver.Firefox(options=options)
driver.implicitly_wait(1)

driver.get("https://sdb.admin.uw.edu/students/uwnetid/register.asp")

# If we aren't logged in, go through the login process
if (driver.title == "UW NetID sign-in"):
    user_field = driver.find_element(By.ID, "weblogin_netid")
    user_field.clear()
    user_field.send_keys(user)
    pwrd_field = driver.find_element(By.ID, "weblogin_password")
    pwrd_field.clear()
    pwrd_field.send_keys(pwrd)
    driver.find_element(By.ID, "submit_button").click()


# Gimme some time to do the 2FA (shouldn't be a problem as I'll have remember me on, but just in case)
while (driver.title == "UW NetID sign-in"):
    time.sleep(5)

print("We're free! Time to actually do the class signup!")

# Selecting the table where we mark classes DROP
# drops_table = driver.find_element_by_css_selector("table.sps_table update")
# for row in drops_table.find_elements_by_css_selector("tr"):
#     for cell in row.find_elements_by_css_selector("input"):
#         if (cell.name == "sln1"):
#             print(cell.value)

driver.quit()