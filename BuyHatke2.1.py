
#BuyHatke2
import re
import urllib
search = input("Enter the product name you want to search: ")
amazon = "https://www.amazon.in/s/?ref=nb_sb_noss_2?url=search-alias%3Daps&field-keywords="
flipkart = "https://www.flipkart.com/search?q="
amazon = amazon + search
flipkart = flipkart + search
data1 = urllib.request.urlopen(amazon).read()
data2 = urllib.request.urlopen(flipkart).read()
data11 = data1.decode("utf-8")
data22 = data2.decode("utf-8")
m = re.search('<span class="currencyINR">&nbsp;&nbsp;',data11)
start = m.end()+7
end = start + 10
x = data11[start:end]

m = re.search('</',x)
end = m.start()
x = x[:end]
print("Price in Amazon is " + x)

a = re.search('<div class="_1vC4OE',data22)

st = a.end()
en = st +20
q = data22[st:en]
a = re.search('">',q)
st = a.end()+1
en = st +10
q = q[st:en]
a = re.search('</',q)
en = a.start()
q = q[:en]
print("Price in Flipkart is " + q)
x = x.replace(",","")
q = q.replace(",","")
x = int(x)
q = int(q)
if x>q:
    print("Flipkart is better than Amazon")
elif q>x:
    print("Amazon is better than Flipkart")
else:
    print("Amazon and Flipkart are selling at same price")