import pandas as pd 
import requests 
from bs4 import BeautifulSoup



Product_name = []
Product_price = []
Product_rating = []
Product_description = []
# Product_name = []
# Product_name = []


for i in range(1,3):
    url = "https://www.flipkart.com/search?q=mobiles+under+50000&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page="+str(i)


    r = requests.get(url)

    soup = BeautifulSoup(r.text, "lxml")
    box = soup.find('div',class_ = "_1YokD2 _3Mn1Gg")


    names = box.find_all('div',class_ = "_4rR01T")


    for i in names:
        name = i.text
        Product_name.append(name)


    # print(Product_name)


    prices = box.find_all('div',class_ = "_30jeq3 _1_WHN1")

    for i in prices:
        name = i.text
        Product_price.append(name)


    # print(Product_price)

    desc = box.find_all('ul', class_ = "_1xgFaf")

    for i in desc:
        name = i.text
        Product_description.append(name)


    # print(Product_description)


    rating = box.find_all('div', class_ = "_3LWZlK")

    for i in rating:
        name = i.text
        print(name,end = "  ")
        Product_rating.append(name)

    # print(Product_rating)
    print(len(names))
    print(len(prices))
    print(len(rating))
    print(len(desc))






df = pd.DataFrame({"Product_name": Product_name,"Product_Price": Product_price, "Product_Rating": Product_rating, "Product_Description": Product_description})

print(df)