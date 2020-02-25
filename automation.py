from selenium import webdriver

driver = webdriver.Chrome('./chromedriver')

driver.maximize_window()
driver.get('https://www.seleniumeasy.com/test/basic-first-form-demo.html')

assert 'Selenium Easy Demo' in driver.title
show_message_btn = driver.find_element_by_class_name('btn-default')
# print(show_message_btn.get_attribute('innerHTML'))

assert 'Show Message' in driver.page_source

user_message = driver.find_element_by_id('user-message')
# user_message = driver.find_elements_by_css_selector('#user-message')
user_message.clear()
user_message.send_keys('smth new')

show_message_btn.click()

output_message = driver.find_element_by_id('display')

assert 'smth new' in output_message.text

driver.close()