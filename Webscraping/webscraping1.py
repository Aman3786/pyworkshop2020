import requests
from requests_html import HTMLSession
import csv
 
session =HTMLSession()
r =session.get("https://www.imdb.com/chart/top/?ref_=nv_mv_250")

print(r)

lister =r.html.find(".titleColumn")

rate =r.html.find(".imdbRating strong")

image = r.html.find(".posterColumn a img")

for i in range(0,len(lister)):
    print(lister[i].text)
    print(rate[i].text)
    print(image[i].attrs["src"])
    print("")

header = ["Title","Rating","Poster"]
data =open("imdb.csv","w")
writer =csv.writer(data)
writer.writerow(header)

for i in range(0,len(lister)):
    a =[lister[i].text,rate[i].text,image[i].attrs["src"]]
    writer.writerow(a)
    


    
