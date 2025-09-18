from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
import pandas as pd
import time

opsi = webdriver.ChromeOptions()
opsi.add_argument('--headless')
servis = Service('chromedriver.exe')
driver = webdriver.Chrome(service = servis, options = opsi)


produk_list = []

i = 1
for page in range(1, 32): # Karena ada 31 halaman 
    url_sociolla = f"https://www.sociolla.com/139-makeup?sort=-best-seller&limit=50&page={page}"
    driver.get(url_sociolla)
    time.sleep(5)

    content = driver.page_source
    data = BeautifulSoup(content, 'html.parser')
    #print(data.encode("utf-8"))

    for area in data.find_all('div', {'class' : 'product product--v3'}):
        
        # Bagian yang ingin di ambil
        produk_brand = area.find('a', {'class' : 'product__brand'}).get_text(strip=True)
        produk_name = area.find('a', {'class' : 'product__name'}).get_text(strip=True)
        harga = area.find('h2', {'class' : 'product__price'}).get_text(strip=True)

        #Mengatasi produk yang tidak ada ratingnya
        rating_tag = area.find('span', {'class' : 'product__stars'})
        if rating_tag: 
            rating = rating_tag.get_text(strip=True)
        else:
            rating = "No Rating"

        review_tag = area.find('span', {'class' : 'product__reviews'})
        if review_tag:
            review = review_tag.get_text(strip=True)
        else:
            review = "No Review"

        print(i)
        print(produk_brand)
        print(produk_name)
        print(harga)
        print(rating)
        print(review)
        print("----")

        # Simpan ke list
        produk_list.append({
            'Brand': produk_brand,
            'Name': produk_name,
            'Harga': harga,
            'Rating': rating,
            'Review': review
        })
        i += 1


driver.quit()

# Save data as csv
#df = pd.DataFrame(produk_list)
#df.to_csv('sociolla_makeup_data.csv', index=False, encoding='utf-8-sig')