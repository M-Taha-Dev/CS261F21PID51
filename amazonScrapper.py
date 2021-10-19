import csv
from bs4 import BeautifulSoup
from selenium import webdriver
def getUrl(item):
    template = 'https://www.amazon.com/s?k={}'
    link = item.replace(' ','+')
    url = template.format(link)
    url += '&page={}'
    return url
def extract_data(item):
    description = item.h2.a.text
    atag = item.h2.a
    href = atag.get('href')
    link ='https://www.amazon.com' + href
    company = description.split(' ')[0]
    model = description.split(' ')[1:]
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
    
    result = (company,model,description,price,rating,reviews,link)
    return result
driver = webdriver.Chrome(executable_path='C:\\Program Files\\Google\\Chrome\\chromedriver.exe')
url = getUrl('gaming gpus')
item_list = []
for page in range(1,21):
    pg = url.format(page)
    driver.get(pg)
    print(pg)
    soup = BeautifulSoup(driver.page_source,'html.parser')
    results = soup.find_all('div',{'data-component-type':'s-search-result'})
    """item = results[0]
    result = extract_data(item)
    print(result)"""
    for item in results:
        extracted_data = extract_data(item)
        if extracted_data:
            item_list.append(extracted_data)
driver.close()
#save data to a csv file
with open('data.csv','a',newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Manufacturer','Model','Description','Price','Rating','no. of reviews','url'])
    writer.writerows(item_list)