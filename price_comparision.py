import re
import urllib.request
search = input("Enter the product name you want to search: ")
amazon = "https://www.amazon.in/s?k="
flipkart = "https://www.flipkart.com/search?q="
amazon = amazon + search
flipkart = flipkart + search
data1 = urllib.request.urlopen(amazon).read()
data2 = urllib.request.urlopen(flipkart).read()
data11 = data1.decode("utf-8")
data22 = data2.decode("utf-8")
#Searching Amazon Price
m = re.search('<span class="a-offscreen">₹',data11)
start = m.end()
end = start + 10
x = data11[start:end]
m = re.search('</',x)
end = m.start()
x=x[:end]
print("Price in Amazon is " + x)
x=x.replace(",","")
p_amazon=int(x)
#print(data22)
#Searching Flipkart Price
m = re.search("_1vC4OE",data22)
start = m.end()
end=start+22
x=data22[start:end]
#print(x)
m = re.search(">₹",x)
start = m.end()
end=start+9
x=x[start:end]
m=re.search("</",x)
end=m.start()
x=x[:end]
print("Price in Flipkart is " + x)
x=x.replace(",","")
p_flipkart=int(x)
#Comparing Prices
if (p_amazon>p_flipkart):
    print("Flipkart is better than Amazon")
elif (p_flipkart>p_amazon):
    print("Amazon is better than Flipkart")
else:
    print("Amazon and Flipkart are selling at same price")

k=input()
print(k)
