import csv
from bs4 import BeautifulSoup
from selenium import webdriver
def getUrl(item):
    template = 'https://www.amazon.com/s?k={}&ref=nb_sb_noss_2'
    link = item.replace(' ','+')
    url = template.format(link)
    return url
def extract_data(item):
    description = item.h2.a.text
    atag = item.h2.a
    href = atag.get('href')
    link ='https://www.amazon.com' + href
    try:
        price_parent = item.find('span','a-price')
        price = price_parent.find('span','a-offscreen').text
    except AttributeError:
        return
    try:
        rating = item.i.text
        reviews = item.find('span','a-size-base').text
    except AttributeError:
        rating = ''
        reviews = ''
    
    result = (description,price,rating,reviews,link)
    return result
driver = webdriver.Chrome(executable_path='C:\\Program Files\\Google\\Chrome\\chromedriver.exe')
url = getUrl('gaming laptops')
driver.get(url)
soup = BeautifulSoup(driver.page_source,'html.parser')
results = soup.find_all('div',{'data-component-type':'s-search-result'})
print(len(results))
"""item = results[0]
result = extract_data(item)
print(result)"""
item_list = []
for item in results:
    extracted_data = extract_data(item)
    if extracted_data:
        item_list.append(extracted_data)
for i in item_list:
    print(i)
#save data to a csv file
with open('data.csv','w',newline='',encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Description','Price','Rating','no. of reviews','url'])
    writer.writerows(item_list)

