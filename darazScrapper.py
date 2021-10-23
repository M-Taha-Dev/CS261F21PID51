from selenium import webdriver 
from bs4 import BeautifulSoup
import csv
driver = webdriver.Chrome(executable_path='C:\\Program Files\\Google\\Chrome\\chromedriver.exe')
def get_url(item_name):
    template = 'https://www.daraz.pk/catalog/?page={}&q='
    item_name = item_name.replace(' ','%20')
    url = template + item_name
    return url
d = get_url('gaming laptops')
print(d.format(2))
def get_product_details(item):
    price = item.span.text
    description = item.find_all('a')[1].text
    reviews = 'None'
    company = description.split(' ')[0]
    model = description.split(' ')[1:]
    href = 'https://www.daraz.pk'
    try:
        rating = item.find('span',{'class':'c3XbGJ'}).text
    except AttributeError:
        rating = ''
    return (company,model,description,price,rating,reviews,href)
data1 = []
listofitems = ['apple watch','hp omen','dell inspiron','dell xps','redmagic phones','realme phones','razor laptops','hp elitebook','probooks','chromebooks','ipods','airpods max','imac','air cooler for cpus','phone cases','laptop bags','wireless keyboards','computer adapters','usb hub','laptop covers','selfie sticks','s21 ultra','note 20 ultra','mac mini','android tablets']
for items in listofitems:
    for page in range(1,102):
        url = get_url(items)
        url = url.format(page)
        print(url)
        driver.get(url)
        soup = BeautifulSoup(driver.page_source,'html.parser')
        results = soup.find_all('div',{'class':'c2prKC'})
        for item in results:
            a = get_product_details(item)
            data1.append(a)
    with open('data.csv','a',newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Manufacturer','Model','Description','Price','Rating','no. of reviews','url'])
        writer.writerows(data1)