from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.service import Service



# website
web = 'https://www.lazada.sg/#'
path = r'C:\Users\shahe\Downloads\chromedriver-win64\chromedriver.exe'  
service = Service(executable_path=path)
driver = webdriver.Chrome(service=service)


driver.get(web)


timeout = 30
try:
    WebDriverWait(driver, timeout).until(EC.visibility_of_element_located((By.ID, "Level_1_Category_No1")))
except TimeoutException:
    driver.quit()


category_element = driver.find_element(By.ID,'Level_1_Category_No1').text
#result -- Electronic Devices as the first category listing

list_category_elements = driver.find_element(By.XPATH,'//*[@id="J_icms-5000498-1511516689962"]/div/ul')
links = list_category_elements.find_elements(By.CLASS_NAME,"lzd-site-menu-root-item")
for i in range(len(links)):
    print("element in list ", links[i].text)
#result {Electronic Devices, Electronic Accessories, etc}


element = driver.find_elements_by_class_name('J_ChannelsLink')[1]
webdriver.ActionChains(driver).move_to_element(element).click(element).perform()


product_titles = driver.find_elements_by_class_name('title')
for title in product_titles:
    print(title.text)



# product_containers = driver.find_elements_by_class_name('product_container')
# for container in product_containers:    
#     product_titles.append(container.find_element_by_class_name('title').text)
#     pack_sizes.append(container.find_element_by_class_name('pack_size').text)    product_prices.append(container.find_element_by_class_name('product_price').text)
#     rating_counts.append(container.find_element_by_class_name('ratings_count').text)


# data = {'product_title': product_titles, 'pack_size': pack_sizes,'product_price': product_prices, 'rating_count': rating_counts}

