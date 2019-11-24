import requests
url = "http://opendata.epa.gov.tw/webapi/Data/REWIQA/?$orderby=SiteName&$skip=0&$top=1000&format=json"
html = requests.get(url).text.encode('utf-8-sig')
print(html)