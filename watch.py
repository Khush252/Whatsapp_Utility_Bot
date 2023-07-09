from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(ChromeDriverManager().install())
# Replace below path with the absolute path
# to chromedriver in your computer
# driver = webdriver.Chrome('/Users/khush___bajaj/Desktop/code/chromedriver')


driver.get("https://web.whatsapp.com/")

wait = WebDriverWait(driver, 600)
 
# Replace 'Friend's Name' with the name of your friend
# or the name of a group
target = 'Shubhhhh'
# Replace the below string with your own message
string = "hellooooo"

# x_arg = '//span[contains(@title,' + target + ')]'
# group_title = wait.until(EC.presence_of_element_located((
#     By.XPATH, x_arg)))
search_xpath='//div[@contenteditable="true"][@data-tab="3"]' 
# group_box=WebDriverWait(driver,500).until(
# 	EC.presence_of_element_located((By.XPATH,group_xpath))
# 	)

search_title=WebDriverWait(driver,500).until(EC.presence_of_element_located((
    By.XPATH, search_xpath))
)
search_title.send_keys(target)

time.sleep(2)

group_xpath=f'//span[@title="{target}"]'
group_title=driver.find_element_by_xpath(group_xpath)

group_title.click()

time.sleep(1)




inp_xpath = '//div[@class="_13NKt copyable-text selectable-text"][@data-tab="10"]'

input_box=driver.find_element_by_xpath(inp_xpath)


for i in range(60):
    input_box.send_keys(string + Keys.ENTER)
    time.sleep(0.01)