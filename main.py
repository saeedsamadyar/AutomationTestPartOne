from selenium import webdriver

driver = webdriver.Chrome(executable_path="/Users/saeed/Downloads/chromedriver")
#driver.get("https://www.google.com/")
driver.get("https://www.play1.automationcamp.ir/forms.html")

#search_field = driver.find_element('name','q')
#search_field.send_keys("Keep it simple")
#search_field.send_keys(Keys.RETURN)
#--------------------------------------------------
driver.find_element('id','check_python').click()
check1 = driver.find_element('id', 'check_validate').text
assert check1 == 'PYTHON'

text1 = "Hello automation world!"
driver.find_element('id','notes').send_keys(text1)
check2 = driver.find_element('id','area_notes_validate').text
assert check2 == text1



#---------------------------------------------------








