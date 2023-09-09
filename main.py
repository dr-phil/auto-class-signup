from selenium import webdriver
from dotenv import load_dotenv
import os

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
driver.implicitly_wait(0.5)

driver.get("https://sdb.admin.uw.edu/students/uwnetid/register.asp")

if (driver.title == "UW NetID sign-in"):


# Selecting the table where we mark classes DROP
drops_table = driver.find_element_by_css_selector("table.sps_table update")
for row in drops_table.find_elements_by_css_selector("tr"):
    for cell in row.find_elements_by_css_selector("input"):
        if (cell.name == "sln1"):
            print(cell.value)

driver.quit()