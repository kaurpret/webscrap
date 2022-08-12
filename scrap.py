from bs4 import *
import requests
import pandas as pd
nm=[]
pr=[]
delivery=[]
rating=[]
discount=[]
img=[]
page_num=input('enter the number of pages : ')
for i in range(1,int(page_num)+1):
   res=requests.get('https://www.meesho.com/wedding-party-wear-saree/pl/m818u?page='+str(i))
   soup=BeautifulSoup(res.content,'html.parser')
   saree_name=soup.find_all('p',class_='Text__StyledText-sc-oo0kvp-0 cPgaBh NewProductCard__ProductTitle_Desktop-sc-j0e7tu-4 hofZGw NewProductCard__ProductTitle_Desktop-sc-j0e7tu-4 hofZGw')
   for i in saree_name:
    nm.append(i.text)
   saree_prize=soup.find_all('h5',class_='Text__StyledText-sc-oo0kvp-0 dLSsNI')
   for i in saree_prize:
    pr.append(i.text)
   saree_delivery=soup.find_all('span',class_='Text__StyledText-sc-oo0kvp-0 jfPftu')
   for i in saree_delivery:
    # print(i.text)
    delivery.append(i.text)
   saree_rating=soup.find_all('span',class_='Text__StyledText-sc-oo0kvp-0 kPhFPP')
   for i in saree_rating:
    # print(i.text)
    rating.append(i.text)
   saree_discount=soup.find_all('span',class_='Text__StyledText-sc-oo0kvp-0 juYkyc')
   for i in saree_discount:
    # print(i.text)
    discount.append(i.text)
   saree_img=soup.find_all('img')
   for i in saree_img:
    # print(i.get('src'))
    img.append(i.get('src'))

data={'Name':nm,'Prize':pr,'Discount':discount,"Delivery":delivery}
df=pd.DataFrame(data)
print(df)
df.to_csv('saree.csv')
