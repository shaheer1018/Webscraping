from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import time



# initialize a list to store empty dataframes
df_list = []
NUM_PAGES = 3



for i in range(NUM_PAGES):

    # website = 'https://www.lazada.com.my/'
    website = f'https://www.lazada.com.my/catalog/?spm=a2o4k.searchlist.0.0.3cf15dcae3if2I&q=disposable%20vape&page={i}'
    path = r'C:\Users\shahe\Downloads\chromedriver-win64\chromedriver.exe'  # Ensure the full path to chromedriver.exe
    service = Service(executable_path=path)
    driver = webdriver.Chrome(service=service)



    driver.get(website)
    # Wait for the page to load
    time.sleep(10)


    # # Search for 'disposable vape'
    # search_box = driver.find_element(By.ID, 'q')
    # search_box.send_keys('disposable vape')
    # search_box.submit()


    # Bypass age verification popup if it appears
    # try:
    #     # Locate and click the "Over 18" button by text content
    #     over_18_button = driver.find_element_by_xpath('//button[contains(span, "Over 18")]')
    #     over_18_button.click()
    #     time.sleep(2)
    # except:
    #     pass  # No age verification popup appeared




    time.sleep(10)
    # Scroll down to load more products


    items = WebDriverWait(driver,30).until(EC.presence_of_all_elements_located((By.XPATH, '//div[contains(@class, "Bm3ON")]')))


    print(len(items))

    product_name = []
    product_price = []
    product_sold_count = []

    for item in items:
        name = item.find_element(by = 'xpath', value = './/div[@class="RfADt"]').text
        product_name.append(name)
        price = item.find_element(by = 'xpath', value = './/div[@class="aBrP0"]').text
        product_price.append(price)
        sold_count = item.find_element(by = 'xpath', value = './/div[@class="_6uN7R"]').text
        sold_count = sold_count.split('\n')[0]
        product_sold_count.append(sold_count)

        time.sleep(2)

    df_temp = pd.DataFrame({'name': product_name, 'price': product_price, 'sold_count': product_sold_count})
    df_list.append(df_temp)
    time.sleep(5)




df_data = pd.concat(df_list)
df_data.to_csv('data.csv', index = False)