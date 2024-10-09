

import os
import time
import requests

import bs4

from selenium import webdriver
from selenium.webdriver.common.by import By


from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


chromeDriverPath = r'C:\Users\Jilen\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe'

options = Options()

options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

service = Service(chromeDriverPath)
driver = webdriver.Chrome(service=service, options=options)



def download_image(url, folder_name, num):


    response = requests.get(url)

    if response.status_code == 200:
        file_path = os.path.join(folder_name, f"{num+150}.jpg")
        if os.path.exists(file_path):
            os.remove(file_path)
            
        with open(os.path.join(folder_name, f"{num+150}.jpg"), 'wb') as file:
            file.write(response.content)
        print(f"Image {num}.jpg downloaded successfully.")
    else:
        print(f"Failed to download image {num}.jpg. Status code: {response.status_code}")



search_url = 'https://www.google.com/search?q=tight+dress+long+sleeve&uds=lnms&udm=2'
driver.get(search_url)

a = input("Waiting for the user input to start")

driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

page_html = driver.page_source

pageSoup = bs4.BeautifulSoup(page_html, 'html.parser')
containers = pageSoup.findAll('div', {'class': "eA0Zlc WghbWd FnEtTd mkpRId m3LIae RLdvSe qyKxnc ivg-i PZPZlf GMCzAd"})
print(len(containers))


for i in range(1,len(containers)+1):
    if i % 25 == 0:
        continue
    xPath = f'//*[@id="rso"]/div/div/div[1]/div/div/div[{i}]'
    try:
        element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, xPath)))
        element.click()
        time.sleep(2)


        previewImageXPath = '//*[@id="Sva75c"]/div[2]/div[2]/div/div[2]/c-wiz/div/div[3]/div[1]/a/img[1]'
        imageElement = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, previewImageXPath)))
        imageURL = imageElement.get_attribute('src')

        print(f"Actual URL for element {i}: {imageURL}")
        start_time = time.time()

        download_image(imageURL, r'C:\Users\Jilen\PycharmProjects\Size Recommendation\src\Data2\Not_oversize\long', i)

    except Exception as e:
        print(f"Error: {str(e)}")











